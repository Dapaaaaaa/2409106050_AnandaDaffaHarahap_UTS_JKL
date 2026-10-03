# 2409106050_AnandaDaffaHarahap_UTS_JKL
Berisi tentang penugasan untuk Ujian Tengah Semester Jaringan Komputer Lanjut Semester 5

Nama: Ananda Daffa Harahap | NIM: 2409106050

## Syarat
Pastikan VM atau laptop yang ingin diuji aktif dan nyala
- SSH
- SNMP
- Port Forwarding

## Struktur Project
```
.
├── .gitignore
├── README.md
├── requirements.txt
├── identitas.py          # Bagian A
├── ssh_modul.py          # Bagian B
├── snmp_modul.py         # Bagian C
├── netconf_modul.py      # Bagian D
├── telemetry_modul.py    # Bagian E
└── main.py               # Bagian F (titik masuk program)
```

## Cara Menjalankan
1. Aktifkan dahulu venv (Virtual Environment) untuk python dengan kode dibawah ini
```bash
python -m venv venv

source venv/bin/activate
```

2. Kemudian install kebutuhan yang diperlukan (paramiko dan pysnmp)
```bash
pip install -r requirements.txt
```

3. Ada 2 cara yaitu pertama lakukan perintah dibawah ini untuk overriding data yang ada
```bash
# Linux / macOS
export SSH_HOST=192.168.1.10
export SSH_PASSWORD='password-kamu'
export SNMP_HOST=192.168.1.10

# Windows (PowerShell)
$env:SSH_HOST="192.168.1.10"
$env:SSH_PASSWORD="password-kamu"
$env:SNMP_HOST="192.168.1.10"
```
atau ubah pada bagian dalam code (hard code biar sekali run aja), seperti contohnya port forwardingnya dan juga password atau username
```python
SSH_HOST = os.getenv("SSH_HOST", "127.0.0.1")               # Ubah host SSH
SSH_PORT = int(os.getenv("SSH_PORT", 2222))                 # Ubah PORT
SSH_USERNAME = f"admin_{kode_cabang}"
SSH_PASSWORD = os.getenv("SSH_PASSWORD", "admin123")        # Ubah password
PERINTAH = ["hostname", "uname -a", "uptime"]               # Atur perintah
```

4. Kemudian jalankan perintah dibawah ini untuk menjalankan file

```bash
py main.py
```
atau
```bash
py namaFile.py
```

## Ringkasan Personalisasi
- Username SSH dan community string SNMP mengikuti pola dari kode cabang.
- VLAN ID pada pesan NETCONF diturunkan dari kode cabang.
- Sampel telemetry diturunkan dari digit NIM (3 sampel, 3 kategori berbeda).
- Kredensial dibaca dari environment variable, tidak disimpan di repository.