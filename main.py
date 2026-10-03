#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: main.py
Tujuan: Integrasi seluruh modul dan mencetak laporan akhir cabang
Pembuat: Ananda Daffa Harahap (2409106050)
"""

import identitas
import netconf_modul
import snmp_modul
import ssh_modul
import telemetry_modul


class LaporanCabang:
    def __init__(self, nim, nama, kode_cabang):
        self.nim = nim
        self.nama = nama
        self.kode_cabang = kode_cabang

    def tampilkan_laporan(self, hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry):
        garis = "=" * 60
        print(f"\n{garis}\nLAPORAN AKHIR CABANG {self.kode_cabang}")
        print(f"{self.nama} - {self.nim}\n{garis}")

        print(f"[1] SSH     : {hasil_ssh['status']} ({hasil_ssh['host']})")
        for perintah, keluaran in hasil_ssh["output"].items():
            print(f"      {perintah}: {keluaran}")
        if hasil_ssh["error"]:
            print(f"      error: {hasil_ssh['error']}")

        print(f"[2] SNMP    : {hasil_snmp['status']} (sysName={hasil_snmp['sysName']})")
        if hasil_snmp["error"]:
            print(f"      error: {hasil_snmp['error']}")

        print("[3] NETCONF : pesan edit-config berhasil dibuat")
        print(pesan_netconf)

        print("[4] TELEMETRY:")
        for h in hasil_telemetry:
            print(f"      {h['perangkat']}: {h['cpuUsage']}% -> {h['status']}")
        print(garis)


def main():
    id_perangkat = identitas.buat_id_perangkat("rtr", 1)
    print(f"ID Perangkat: {id_perangkat}\n")

    hasil_ssh = ssh_modul.cek_ssh()
    hasil_snmp = snmp_modul.cek_snmp()
    pesan_netconf = netconf_modul.buat_pesan_netconf()
    hasil_telemetry = telemetry_modul.klasifikasi_telemetry()

    laporan = LaporanCabang(identitas.nim, identitas.nama, identitas.kode_cabang)
    laporan.tampilkan_laporan(hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry)


if __name__ == "__main__":
    main()