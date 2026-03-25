#!/data/data/com.termux/files/usr/bin/bash

clear
echo "======================================"
echo " DARK OBFUSCATOR INSTALLER PRO FINAL "
echo "======================================"
sleep 1

termux-change-repo || true
pkg update -y && pkg upgrade -y

pkg install -y python git clang make libffi openssl termux-api curl

python -m ensurepip --upgrade || true
pip install --upgrade pip setuptools wheel --no-cache-dir

pip install requests --no-cache-dir
pip install pyarmor --no-cache-dir || pip install pyarmor==7.7.0

mkdir -p ~/dark-obfuscator
cd ~/dark-obfuscator

echo "DARK-TRIAL" > key.txt

cat > tool.py << 'EOF'
import os, time, hashlib, requests, base64, platform, sys

API_URL = "https://premiumtools-enscript-descript.ct.ws/api.php"
GEN_URL = "https://premiumtools-enscript-descript.ct.ws/generate.php?auto=1"
DONASI_URL = "https://premiumtools-enscript-descript.ct.ws/donasi.php"
WA_URL = "https://wa.me/6283195664588"

PURPLE = "\033[1;35m"
GREEN = "\033[1;92m"
WHITE = "\033[0m"
RED = "\033[1;91m"

def get_device_id():
    base = platform.node() + platform.system() + platform.machine()
    return hashlib.sha256(base.encode()).hexdigest()

def banner():
    os.system("clear")
    print(PURPLE + "╔══════════════════════════════════════╗")
    print("║   DARK OBFUSCATOR - GOD MODE        ║")
    print("╠══════════════════════════════════════╣")
    print(GREEN + "║ 🔐 Secure Python Protection         ║")
    print("║ ⚡ License Online + Anti Sharing    ║")
    print("║ 💰 Auto Selling System             ║")
    print("║ Developer : Dark User Subang       ║")
    print("╚══════════════════════════════════════╝" + WHITE)

def loading():
    print(PURPLE + "Processing", end="")
    for _ in range(5):
        print(GREEN + "●", end="", flush=True)
        time.sleep(0.3)
    print(WHITE)

def ambil_license():
    print("🔄 Mengambil license otomatis...")
    try:
        key = requests.get(GEN_URL, timeout=5).text.strip()
        open("key.txt","w").write(key)
        print("✅ License:", key)
        time.sleep(1)
        os.execv(sys.executable, ['python'] + sys.argv)
    except:
        print("❌ Gagal generate")

def menu_beli():
    print("\n[1] WhatsApp\n[2] Input Key\n[3] Auto Generate\n[4] Exit")
    p = input("Pilih: ")

    if p == "1":
        os.system(f"termux-open-url {WA_URL}")
        sys.exit()
    elif p == "2":
        key = input("Key: ")
        open("key.txt","w").write(key)
        os.execv(sys.executable, ['python'] + sys.argv)
    elif p == "3":
        ambil_license()
    else:
        sys.exit()

def check_license():
    try:
        key = open("key.txt").read().strip()
        device = get_device_id()
        url = f"{API_URL}?key={key}&device={device}"
        res = requests.get(url, timeout=5).text.strip()

        if res == "VALID":
            print(GREEN + "✅ License OK" + WHITE)
        else:
            print("❌ License:", res)
            menu_beli()
    except:
        print("⚠️ Server error")
        menu_beli()

def obfuscate():
    f = input("File: ")
    if not os.path.exists(f):
        print("❌ File tidak ada")
        return

    if os.system("command -v pyarmor > /dev/null") != 0:
        print("❌ pyarmor belum install")
        return

    o = input("Output: ")
    loading()
    os.system(f"pyarmor gen -O {o} {f}")
    print("✅ Done")

def encrypt_file():
    f = input("File: ")
    if not os.path.exists(f):
        print("❌ Tidak ada")
        return
    open(f+".enc","wb").write(base64.b64encode(open(f,"rb").read()))
    print("✅ Encrypt")

def decrypt_file():
    f = input("File .enc: ")
    if not os.path.exists(f):
        print("❌ Tidak ada")
        return
    open(f.replace(".enc","_dec"),"wb").write(base64.b64decode(open(f,"rb").read()))
    print("✅ Decrypt")

def donasi():
    os.system(f"termux-open-url {DONASI_URL}")

def main():
    banner()
    check_license()
    while True:
        print("\n1.Obfuscate\n2.Encrypt\n3.Decrypt\n4.Donasi\n5.Exit")
        c = input("Select: ")
        if c=="1": obfuscate()
        elif c=="2": encrypt_file()
        elif c=="3": decrypt_file()
        elif c=="4": donasi()
        else: break

if __name__ == "__main__":
    main()
EOF

cat > run.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd ~/dark-obfuscator
python tool.py
EOF

chmod +x run.sh

echo "✅ INSTALL SELESAI"
echo "Jalankan: cd ~/dark-obfuscator && ./run.sh"