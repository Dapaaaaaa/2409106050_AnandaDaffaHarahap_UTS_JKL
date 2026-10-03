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
SSH_PORT = int(os.getenv("SSH_PORT", 22))
SSH_USERNAME = f"admin_{kode_cabang}"
SSH_PASSWORD = os.getenv("SSH_PASSWORD", "")
PERINTAH = ["hostname", "uname -a", "uptime"]

