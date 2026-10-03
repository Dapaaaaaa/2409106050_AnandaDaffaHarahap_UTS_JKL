#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: identitas.py
Tujuan: Menyimpan informasi identitas pengguna, kantor cabang, pembuat id perangkat, dan generator id perangkat
Pembuat: Ananda Daffa Harahap (2409106050)
"""

nim = "2409106050"
nama = "Ananda Daffa Harahap"
kode_cabang = nim[-3:] # Mengambil 3 digit terakhir dari NIM sebagai kode cabang sesuai perintah soal

# Fungsi untuk membuat ID perangkat
def buat_id_perangkat(jenis, nomor):
    return f"{jenis.upper()}-{kode_cabang}-{nomor:02d}"

# untuk menguji fungsi buat_id_perangkat
if __name__ == "__main__":
    print(nim, nama, kode_cabang, buat_id_perangkat("Rtr", 1))