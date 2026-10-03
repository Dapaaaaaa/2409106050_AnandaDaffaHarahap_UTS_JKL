#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: identitas.py
Tujuan: Untuk login SSH ke VM menggunakan paramiko dan menjalankan perintah diagnostik
Pembuat: Ananda Daffa Harahap (2409106050)
"""

import os
import paramiko

from identitas import kode_cabang

SSH_HOST = os.getenv("SSH_HOST", "127.0.0.1")
SSH_PORT = int(os.getenv("SSH_PORT", 2222))
SSH_USERNAME = f"admin_{kode_cabang}"
SSH_PASSWORD = os.getenv("SSH_PASSWORD", "admin123")
PERINTAH = ["hostname", "uname -a", "uptime"]

#  Fungsi cek koneksi SSH
def cek_ssh():
    hasil = {"status": "GAGAL", "host": SSH_HOST, "output": {}, "error": None}
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(SSH_HOST, port=SSH_PORT, username=SSH_USERNAME, password=SSH_PASSWORD, timeout=10)
        for perintah in PERINTAH:
            _, stdout, _ = client.exec_command(perintah, timeout=10)
            hasil["output"][perintah] = stdout.read().decode().strip()
        hasil["status"] = "BERHASIL"
    except Exception as e:
        hasil["error"] = f"{type(e).__name__}: {e}"
    finally:
        client.close()

    print(f"[SSH] {SSH_USERNAME}@{SSH_HOST}:{SSH_PORT} -> {hasil['status']}")
    for perintah, keluaran in hasil["output"].items():
        print(f"  $ {perintah}\n    {keluaran}")
    if hasil["error"]:
        print(f"  Error: {hasil['error']}")
    return hasil


if __name__ == "__main__":
    cek_ssh()