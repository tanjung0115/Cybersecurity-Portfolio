import requests

# koordinat targer (perhatikan titik di akhit config.)
target_url = "http://127.0.0.1:8080/config."

# amunisi / peluru (daftar eksteni)
payloads = ["txt","zip", "bak", "php", "old"]

print("memulai serangan mini-intruder...")
print("-"*40)

# looping
for peluru in payloads:
        # menggabungkan target + peluru (misal : http://...../config. + txt)
        url_tebakan = target_url + peluru
        # mengirim request GET
        respon = requests.get(url_tebakan)
        # mengecek apakah status 200
        if respon.status_code == 200:
                print (f"[+] Ditemukan : {url_tebakan}")
        else:
                print (f"[-] Gagal (404): {url_tebakan}")

print ("-" *40)
print ("Serangan Selesai")
