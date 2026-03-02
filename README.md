#  Super Port Scanner (Python CLI Tool)

###  Author:Mija Tanjung
**Bootcamp Cybersecurity: The Toolmaker**

---

##  Deskripsi Singkat
**Super Port Scanner** adalah alat pemindai jaringan (Network Scanner) berbasis Command Line Interface (CLI) yang dibangun menggunakan Python murni. 

Alat ini dibuat untuk memahami cara kerja pemindaian jaringan (*Reconnaissance*) di dunia Cybersecurity. Berbeda dengan scanner tradisional yang lambat, tool ini telah dioptimalkan dengan algoritma **Multithreading** untuk memindai ribuan port dalam hitungan detik.

##  Fitur Utama (Key Features)
-  **Asynchronous/Multithreading:** Menggunakan `concurrent.futures` dengan 50 *workers* untuk memindai port (1-1024) secara bersamaan (Sangat Cepat!).
-  **Dynamic Target Parsing:** Mendukung input target dinamis dari terminal (mendukung IP Address maupun resolusi Hostname/Domain).
-  **Banner Grabbing:** Tidak hanya mendeteksi port yang terbuka, tapi secara aktif mengirim *HTTP payload* untuk mengidentifikasi layanan (service) yang berjalan di baliknya.
-  **Pro UI/UX:** Dilengkapi dengan ASCII Art, ANSI Color Codes (Warna terminal), dan output log yang bersih.
-  **Graceful Error Handling:** Tahan terhadap *crash*. Mampu menangani *Timeout*, koneksi terputus, dan *Keyboard Interrupt* (Ctrl+C) dengan aman.

##  Prasyarat (Prerequisites)
- Python 3.x
- Tidak memerlukan *library* eksternal (Hanya menggunakan modul bawaan Python: `socket`, `sys`, `datetime`, `concurrent.futures`).

##  Cara Penggunaan (Usage)

1. **Clone repository ini:**
   ```bash
   git clone [https://github.com/tanjung0115/network-tools-python.git](https://github.com/tanjung0115/Cybersecurity-Portfolio.git)
   cd network-tools-python

##  Fuzzer Direktori & Ekstensi

Selain Port Scanner, repositori ini sekarang dilengkapi dengan **Python Fuzzer** kustom untuk mencari file tersembunyi (seperti `.bak`, `.env`, atau direktori admin) di server target.

**Fitur Utama Fuzzer:**
- Membaca target URL secara dinamis.
- Menggunakan *Wordlist* kustom untuk menembakkan *payload* secara otomatis.
- Dilengkapi dengan *Error Handling* (`try-except`) jika server target down atau input URL salah.

**Cara Penggunaan:**
```bash
python3 fuzzer.py

##  HTTP POST Brute-Forcer (v4.0)

Tool untuk melakukan simulasi serangan *brute-force* pada form login web menggunakan metode HTTP POST.

**Fitur Utama:**
- Membaca target form login secara dinamis.
- Menginjeksi *payload* dari *custom wordlist*.
- Dilengkapi dengan *Error Handling* dan deteksi indikator kegagalan yang akurat.

**Cara Penggunaan:**
```bash
python3 bruteforce.py

##  Banner Grabber (v5.0)

Tool *Information Gathering* berbasis *socket* tingkat rendah untuk mengekstrak identitas *software* dan sistem operasi dari *server* target sebelum masuk ke fase eksploitasi.

**Fitur Utama:**
- Mampu mengetuk *port* spesifik seperti SSH (22), HTTP (80), dan lainnya.
- Membaca *header* balasan server untuk mengetahui versi perangkat lunak (misal: OpenSSH, Apache, Ubuntu).
- Dilengkapi *timeout protection* agar skrip tidak *hang* saat target tidak merespons.

**Cara Penggunaan:**
```bash
python3 banner-grabber.py
