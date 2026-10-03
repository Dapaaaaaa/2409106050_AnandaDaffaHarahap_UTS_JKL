#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: netconf_modul.py
Tujuan: Membangun pesan NETCONF <rpc><edit-config> untuk membuat VLAN
Pembuat: Ananda Daffa Harahap (2409106050)
"""

from identitas import kode_cabang

# TRANSPORT layer : NETCONF berjalan di atas SSH (port 830). Tidak tampil di
# string XML; ditangani oleh sesi SSH saat pesan dikirim.


def buat_pesan_netconf(vlan_id=None, message_id=101):
    vlan_id = vlan_id or kode_cabang
    nama_vlan = f"VLAN_{vlan_id}"

    pesan = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- MESSAGES layer: pembungkus <rpc> dengan message-id dan namespace base:1.0 -->
<rpc message-id="{message_id}" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <!-- OPERATIONS layer: operasi <edit-config> pada datastore running -->
  <edit-config>
    <target><running/></target>
    <!-- CONTENT layer: data konfigurasi VLAN (model YANG openconfig-vlan) -->
    <config>
      <vlans xmlns="http://openconfig.net/yang/vlan">
        <vlan>
          <vlan-id>{vlan_id}</vlan-id>
          <config>
            <vlan-id>{vlan_id}</vlan-id>
            <name>{nama_vlan}</name>
            <status>ACTIVE</status>
          </config>
        </vlan>
      </vlans>
    </config>
  </edit-config>
</rpc>"""
    return pesan


if __name__ == "__main__":
    print(buat_pesan_netconf())