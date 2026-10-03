#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: telemetry_modul.py
Tujuan: Klasifikasi sampel data telemetry cpuUsage (in-uti) hasil decode GPB
Pembuat: Ananda Daffa Harahap (2409106050)
"""

from identitas import nim

# sampel_1: 2 digit terakhir NIM       -> 0-49  (NORMAL)
# sampel_2: 2 digit sebelumnya         -> 50-80 (WASPADA)
# sampel_3: 2 digit sebelumnya lagi    -> 81-99 (KRITIS)
data_telemetry = {
    "rtr-sampel-1": {"cpuUsage": int(nim[-2:]) % 50},
    "rtr-sampel-2": {"cpuUsage": 50 + int(nim[-4:-2]) % 31},
    "rtr-sampel-3": {"cpuUsage": 81 + int(nim[-6:-4]) % 19},
}


def klasifikasi_telemetry():
    hasil = []
    for perangkat, sampel in data_telemetry.items():
        cpu = sampel["cpuUsage"]
        if cpu > 80:
            status = "KRITIS"
        elif cpu >= 50:
            status = "WASPADA"
        else:
            status = "NORMAL"
        hasil.append({"perangkat": perangkat, "cpuUsage": cpu, "status": status})
        print(f"[TELEMETRY] {perangkat}: cpuUsage={cpu}% -> {status}")
    return hasil


if __name__ == "__main__":
    klasifikasi_telemetry()