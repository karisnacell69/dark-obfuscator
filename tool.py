import os, time, hashlib, requests, base64, platform, sys

# =========================
# CONFIG
# =========================
API_URL = "https://premiumtools-enscript-descript.ct.ws/api.php"
DONASI_URL = "https://premiumtools-enscript-descript.ct.ws/donasi.php"
WA_URL = "https://wa.me/6283195664588"

# =========================
# COLOR
# =========================
PURPLE = "\033[1;35m"
GREEN = "\033[1;92m"
WHITE = "\033[0m"
RED = "\033[1;91m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"

# =========================
# DEVICE ID
# =========================
def get_device_id():
    base = platform.node() + platform.system() + platform.machine()
    return hashlib.sha256(base.encode()).hexdigest()

# =========================
# CLEAR + BANNER
# =========================
def banner():
    os.system("clear")
    print(PURPLE + "╔══════════════════════════════════════╗")
    print("║   DARK OBFUSCATOR - GOD MODE        ║")
    print("╠══════════════════════════════════════╣")
    print(GREEN + "║ 🔐 Secure Python Protection         ║")
    print("║ ⚡ Anti Sharing + License Online    ║")
    print("║ 💰 QRIS Payment Support            ║")
    print("║ 🤖 Auto System Premium             ║")
    print("║ Developer : Dark User Subang       ║")
    print("╚══════════════════════════════════════╝" + WHITE)

# =========================
# LOADING ANIMASI
# =========================
def loading(msg="Processing"):
    print(PURPLE + msg, end="")
    for _ in range(5):
        print(GREEN + " ●", end="", flush=True)
        time.sleep(0.3)
    print(WHITE)

# =========================
# LICENSE CHECK
# =========================
def check_license():
    try:
        if not os.path.exists("key.txt"):
            print(RED + "❌ key.txt tidak ditemukan!" + WHITE)
            sys.exit()

        key = open("key.txt").read().strip()
        device = get_device_id()

        url = f"{API_URL}?key={key}&device={device}"
        res = requests.get(url, timeout=5).text.strip()

        if res == "VALID":
            print(GREEN + "✅ License Valid (Device Locked)" + WHITE)

        elif res == "EXPIRED":
            print(RED + "⏳ License Expired" + WHITE)
            sys.exit()

        elif res == "BANNED":
            print(RED + "🚫 License dibanned admin" + WHITE)
            sys.exit()

        elif res == "BANNED_DEVICE":
            print(RED + "🚫 Device berbeda! License diblokir" + WHITE)
            sys.exit()

        else:
            print(RED + "❌ Invalid License" + WHITE)
            sys.exit()

    except Exception as e:
        print(RED + "⚠️ Server error: " + str(e) + WHITE)
        sys.exit()

# =========================
# OBFUSCATE
# =========================
def obfuscate():
    file = input("📂 File Python: ")
    if not os.path.exists(file):
        print(RED + "❌ File tidak ditemukan!" + WHITE)
        return

    out = input("📁 Output Folder (default: dist): ") or "dist"

    loading("Obfuscating")
    os.system(f"pyarmor gen -O {out} {file}")

    print(GREEN + f"✅ Berhasil! Output: {out}/" + WHITE)
    input("Enter untuk kembali...")

# =========================
# ENCRYPT BASE64
# =========================
def encrypt_file():
    file = input("📂 File: ")
    if not os.path.exists(file):
        print(RED + "❌ File tidak ditemukan!" + WHITE)
        return

    with open(file, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    out = "enc_" + os.path.basename(file)

    with open(out, "w") as f:
        f.write(f"import base64\nexec(base64.b64decode('{data}'))")

    print(GREEN + f"✅ Encrypted: {out}" + WHITE)
    input("Enter...")

# =========================
# DONASI
# =========================
def donasi():
    print(CYAN + "Membuka halaman donasi..." + WHITE)
    os.system(f"termux-open-url {DONASI_URL}")

# =========================
# MENU UI
# =========================
def menu():
    while True:
        banner()

        print(YELLOW + "\n[ MENU UTAMA ]" + WHITE)
        print("1. 🔐 Obfuscate Python")
        print("2. 🔒 Encrypt Base64")
        print("3. 💰 Donasi")
        print("4. 📞 Contact Dev")
        print("5. ❌ Exit")

        pilih = input("\nPilih menu: ")

        if pilih == "1":
            obfuscate()
        elif pilih == "2":
            encrypt_file()
        elif pilih == "3":
            donasi()
        elif pilih == "4":
            os.system(f"termux-open-url {WA_URL}")
        elif pilih == "5":
            print("Bye!")
            break
        else:
            print(RED + "❌ Pilihan tidak valid!" + WHITE)
            time.sleep(1)

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    banner()
    check_license()
    time.sleep(1)
    menu()
