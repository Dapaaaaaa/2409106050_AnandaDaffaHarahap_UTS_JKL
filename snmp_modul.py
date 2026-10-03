#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: snmp_modul.py
Tujuan: Mengambil sysName (OID 1.3.6.1.2.1.1.5.0) via SNMPv2c (PySNMP)
Pembuat: Ananda Daffa Harahap (2409106050)
"""

import os

from identitas import kode_cabang

SNMP_HOST = os.getenv("SNMP_HOST", "127.0.0.1")
SNMP_PORT = 1161
COMMUNITY = f"comm_{kode_cabang}"
OID_SYSNAME = "1.3.6.1.2.1.1.5.0"


def _get_pysnmp_baru():
    import asyncio
    from pysnmp.hlapi.v3arch.asyncio import (
        CommunityData, ContextData, ObjectIdentity, ObjectType,
        SnmpEngine, UdpTransportTarget, get_cmd)

    async def _jalankan():
        engine = SnmpEngine()
        try:
            target = await UdpTransportTarget.create((SNMP_HOST, SNMP_PORT), timeout=3, retries=1)
            return await get_cmd(engine, CommunityData(COMMUNITY, mpModel=1),  # mpModel=1 = v2c
                                 target, ContextData(),
                                 ObjectType(ObjectIdentity(OID_SYSNAME)))
        finally:
            engine.close_dispatcher()

    return asyncio.run(_jalankan())


def _get_pysnmp_lama():
    from pysnmp.hlapi import (
        CommunityData, ContextData, ObjectIdentity, ObjectType,
        SnmpEngine, UdpTransportTarget, getCmd)
    return next(getCmd(SnmpEngine(), CommunityData(COMMUNITY, mpModel=1),
                       UdpTransportTarget((SNMP_HOST, SNMP_PORT), timeout=3, retries=1),
                       ContextData(), ObjectType(ObjectIdentity(OID_SYSNAME))))


def cek_snmp():
    hasil = {"status": "GAGAL", "host": SNMP_HOST, "sysName": None, "error": None}
    try:
        try:
            err_ind, err_stat, err_idx, var_binds = _get_pysnmp_baru()
        except ImportError:
            err_ind, err_stat, err_idx, var_binds = _get_pysnmp_lama()

        if err_ind:
            hasil["error"] = str(err_ind)
        elif err_stat:
            hasil["error"] = f"{err_stat.prettyPrint()} at {err_idx}"
        else:
            hasil["sysName"] = str(var_binds[0][1])
            hasil["status"] = "BERHASIL"
    except Exception as e:
        hasil["error"] = f"{type(e).__name__}: {e}"

    print(f"[SNMP] {SNMP_HOST} community={COMMUNITY} -> {hasil['status']}")
    if hasil["sysName"]:
        print(f"  sysName = {hasil['sysName']}")
    if hasil["error"]:
        print(f"  Error: {hasil['error']}")
    return hasil


if __name__ == "__main__":
    cek_snmp()