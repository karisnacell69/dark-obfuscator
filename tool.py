import os, time, hashlib, requests, base64, platform

# =========================
# CONFIG
# =========================
API_URL = "https://premiumtools-enscript-descript.ct.ws/api.php"
DONASI_URL = "https://premiumtools-enscript-descript.ct.ws/donasi.php"

# =========================
# COLOR
# =========================
PURPLE = "\033[1;35m"
GREEN = "\033[1;92m"
WHITE = "\033[0m"

# =========================
# DEVICE ID
# =========================
def get_device_id():
    base = platform.node() + platform.system() + platform.machine()
    return hashlib.sha256(base.encode()).hexdigest()

# =========================
# BANNER
# =========================
def banner():
    os.system("clear")
    print(PURPLE + "╔══════════════════════════════════════╗")
    print("║   DARK OBFUSCATOR - GOD MODE        ║")
    print("╠══════════════════════════════════════╣")
    print(GREEN + "║ 🔐 Secure Python Protection         ║")
    print("║ ⚡ Anti Sharing + License Online   ║")
    print("║ 💰 QRIS Payment Support            ║")
    print("║ Developer : Dark User Subang       ║")
    print("╚══════════════════════════════════════╝" + WHITE)

# =========================
# LOADING
# =========================
def loading():
    print(PURPLE + "Processing", end="")
    for i in range(5):
        print(GREEN + "●", end="", flush=True)
        time.sleep(0.3)
    print(WHITE)

# =========================
# LICENSE CHECK
# =========================
def check_license():
    try:
        if not os.path.exists("key.txt"):
            print("❌ key.txt tidak ditemukan!")
            exit()

        key = open("key.txt").read().strip()
        device = get_device_id()

        url = f"{API_URL}?key={key}&device={device}"
        res = requests.get(url, timeout=5).text.strip()

        if res == "VALID":
            print(GREEN + "✅ License Valid (Device Locked)" + WHITE)

        elif res == "EXPIRED":
            print("⏳ License Expired")
            exit()

        elif res == "BANNED":
            print("🚫 License dibanned admin")
            exit()

        elif res == "BANNED_DEVICE":
            print("🚫 Device berbeda! License diblokir")
            exit()

        else:
            print("❌ Invalid License")
            exit()

    except Exception as e:
        print("⚠️ Error license:", e)
        exit()

# =========================
# OBFUSCATE
# =========================
def obfuscate():
    file = input("📂 File Python: ")
    if not os.path.exists(file):
        print("❌ File tidak ditemukan!")
        return

    out = input("📁 Output Folder: ")
    loading()
    os.system(f"pyarmor gen -O {out} {file}")
    print(GREEN + "✅ Obfuscate berhasil!" + WHITE)
    input("Enter...")

# =========================
# ENCRYPT FILE
# =========================
def encrypt_file():
    file = input("📂 File: ")
    if not os.path.exists(file):
        print("❌ File tidak ditemukan!")
        return

    data = open(file, "rb").read()
    enc = base64.b64encode(data)

    out = file + ".enc"
    open(out, "wb").write(enc)

    print(GREEN + f"🔐 Encrypted: {out}" + WHITE)
    input("Enter...")

# =========================
# DECRYPT FILE
# =========================
def decrypt_file():
    file = input("📂 File .enc: ")
    if not os.path.exists(file):
        print("❌ File tidak ditemukan!")
        return

    data = base64.b64decode(open(file, "rb").read())
    out = file.replace(".enc", "_dec")

    open(out, "wb").write(data)

    print(GREEN + f"🔓 Decrypted: {out}" + WHITE)
    input("Enter...")

# =========================
# DONASI QRIS
# =========================
def donasi():
    banner()
    print(GREEN + "\n💰 MEMBUKA HALAMAN DONASI..." + WHITE)

    try:
        os.system(f"termux-open-url {DONASI_URL}")
    except:
        print("⚠️ Gagal membuka browser")

    input("\nEnter untuk kembali...")

# =========================
# MENU
# =========================
def menu():
    print(PURPLE + "\n════════ MENU ════════")
    print(GREEN + " [1] 🔐 Obfuscate Python")
    print(GREEN + " [2] 🧬 Encrypt File")
    print(GREEN + " [3] 🔓 Decrypt File")
    print(GREEN + " [4] 💰 Donasi QRIS")
    print(GREEN + " [5] ❌ Exit")
    print(PURPLE + "══════════════════════" + WHITE)

# =========================
# MAIN
# =========================
def main():
    banner()
    check_license()

    while True:
        banner()
        menu()

        c = input("➤ Select: ")

        if c == "1":
            obfuscate()
        elif c == "2":
            encrypt_file()
        elif c == "3":
            decrypt_file()
        elif c == "4":
            donasi()
        elif c == "5":
            print("👋 Exit...")
            break
        else:
            print("❌ Pilihan salah")
            time.sleep(1)

# =========================
# RUN
# =========================
if __name__ == "__main__":
    main()