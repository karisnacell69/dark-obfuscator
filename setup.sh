#!/data/data/com.termux/files/usr/bin/bash

clear
echo "======================================"
echo " DARK OBFUSCATOR - FULL AUTO SETUP "
echo "======================================"
sleep 1

# =========================
# INSTALL DEPENDENCY
# =========================
echo "[1/4] Install system..."
pkg update -y && pkg upgrade -y
pkg install python git clang make libffi openssl -y

echo "[2/4] Install python module..."
pip install --upgrade pip setuptools wheel
pip install pyarmor requests

# =========================
# CREATE FOLDER
# =========================
echo "[3/4] Create project..."
mkdir -p dark-obfuscator
cd dark-obfuscator

# =========================
# CREATE KEY
# =========================
echo "DARK-TRIAL" > key.txt

# =========================
# CREATE TOOL.PY
# =========================
cat > tool.py << 'EOF'
import os, time, sys, hashlib, requests, base64, platform

API_URL = "https://premiumtools-enscript-descript.ct.ws/api.php?key="
SECRET = "dark_secret_123"

PURPLE = "\033[1;35m"
GREEN = "\033[1;92m"
WHITE = "\033[0m"

def banner():
    os.system("clear")
    print(PURPLE + "╔══════════════════════════════════════╗")
    print("║   DARK OBFUSCATOR - GOD MODE        ║")
    print("╠══════════════════════════════════════╣")
    print(GREEN + "║ 🔐 Secure Python Protection         ║")
    print("║ ⚡ Anti Sharing + Tracking Active  ║")
    print("║ Developer : Dark User Subang       ║")
    print("╚══════════════════════════════════════╝" + WHITE)

def loading():
    print(PURPLE + "Processing", end="")
    for i in range(5):
        print(GREEN + "●", end="", flush=True)
        time.sleep(0.3)
    print(WHITE)

def get_device_id():
    base = platform.node() + platform.system() + platform.machine()
    return hashlib.md5(base.encode()).hexdigest()

def check_license():
    try:
        key = open("key.txt").read().strip()
        device = get_device_id()

        res = requests.get(API_URL + key + "&device=" + device, timeout=5).text.strip()
        status, server_hash = res.split("|")

        local_hash = hashlib.sha256((status + SECRET).encode()).hexdigest()

        if local_hash != server_hash:
            print("🚫 License tampered!")
            exit()

        if status == "VALID":
            print(GREEN + "✅ License Valid (Locked)" + WHITE)
        elif status == "DIFFERENT_DEVICE":
            print("🚫 License dipakai di device lain!")
            exit()
        elif status == "EXPIRED":
            print("⏳ License Expired")
            exit()
        else:
            print("❌ Invalid License")
            exit()

    except:
        print("⚠️ License error")
        exit()

def obfuscate():
    f = input("File: ")
    o = input("Output: ")
    loading()
    os.system(f"pyarmor gen -O {o} {f}")

def encrypt_file():
    f = input("File: ")
    data = open(f,"rb").read()
    enc = base64.b64encode(data)
    open(f+".enc","wb").write(enc)
    print("Encrypted:", f+".enc")

def decrypt_file():
    f = input("File .enc: ")
    data = base64.b64decode(open(f,"rb").read())
    out = f.replace(".enc","_dec")
    open(out,"wb").write(data)
    print("Decrypted:", out)

def main():
    banner()
    check_license()

    while True:
        print("\n1. Obfuscate")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        c = input("Select: ")

        if c == "1":
            obfuscate()
        elif c == "2":
            encrypt_file()
        elif c == "3":
            decrypt_file()
        else:
            break

if __name__ == "__main__":
    main()
EOF

# =========================
# CREATE RUN SCRIPT
# =========================
cat > run.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd $(dirname $0)
python tool.py
EOF

chmod +x run.sh

echo "[4/4] DONE!"

echo ""
echo "======================================"
echo " ✅ INSTALL SELESAI"
echo "======================================"
echo ""
echo "Masuk folder:"
echo "cd dark-obfuscator"
echo ""
echo "Jalankan tools:"
echo "./run.sh"
echo ""