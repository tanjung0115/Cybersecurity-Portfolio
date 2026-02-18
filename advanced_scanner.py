import socket
import sys
from datetime import datetime

# --- WARNA (ANSI CODES) ---
# Biar terminal jadi warna-warni kayak di film hacker
HIJAU = '\033[92m'
MERAH = '\033[91m'
KUNING = '\033[93m'
BIRU = '\033[94m'
RESET = '\033[0m' # Untuk mengembalikan warna ke normal

def print_banner():
    # Logo ASCII Art (Bikin tool kelihatan pro)
    print(BIRU + """
    ========================================
     ⚡ SUPER PORT SCANNER v2.0 (Day 2) ⚡
         Code by: Tanjung0115
    ========================================
    """ + RESET)

def grab_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        
        # Pancingan HTTP
        pancingan = b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
        s.send(pancingan)
        
        banner = s.recv(1024)
        return banner.decode('utf-8', errors='ignore').strip()
    except:
        return "Tidak ada banner"
    finally:
        s.close()

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        
        if result == 0:
            # Jika TERBUKA -> Warna HIJAU
            # Kita coba ambil banner
            info = grab_banner(target, port)
            print(f"{HIJAU}[+] Port {port} OPEN : {info}{RESET}")
        else:
            # Jika TERTUTUP -> Tidak usah print apa-apa (Biar bersih)
            pass 
        s.close()
    except socket.error:
        print(f"{MERAH}[!] Server target mati / tidak bisa dihubungi.{RESET}")
        sys.exit()

# --- PROGRAM UTAMA ---
print_banner()

if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print(f"{MERAH}[!] Hostname tidak ditemukan! Cek koneksi internet.{RESET}")
        sys.exit()
else:
    print(f"{KUNING}[?] Cara pakai: python3 advanced_scanner.py <TARGET IP>{RESET}")
    sys.exit()

print("-" * 50)
print(f"🎯 Scanning Target: {target}")
print(f"🕒 Waktu mulai: {datetime.now()}")
print("-" * 50)

try:
    # Scan port penting (Common Ports)
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 8080, 9000]
    
    for port in ports:
        scan_port(target, port)

except KeyboardInterrupt:
    # Menangani CTRL+C biar keluarnya rapi
    print(f"\n{MERAH}[!] Scanning dibatalkan oleh user.{RESET}")
    sys.exit()

print("-" * 50)
print(f"{BIRU}Scanning Selesai.{RESET}")
