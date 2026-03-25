import os, time, hashlib, requests, base64, platform, sys

API_URL = "https://premiumtools-enscript-descript.ct.ws/api.php"
DONASI_URL = "https://premiumtools-enscript-descript.ct.ws/donasi.php"
WA_URL = "https://wa.me/6283195664588"

PURPLE = "\033[1;35m"
GREEN = "\033[1;92m"
WHITE = "\033[0m"
RED = "\033[1;91m"

def banner():
    os.system("clear")
    print(PURPLE + "╔══════════════════════════════════════╗")
    print("║   DARK OBFUSCATOR - GOD MODE        ║")
    print("╠══════════════════════════════════════╣")
    print(GREEN + "║ 🔐 Secure Python Protection         ║")
    print("║ ⚡ License Online System           ║")
    print("║ 💰 Auto Selling Ready             ║")
    print("║ Developer : Dark User Subang       ║")
    print("╚══════════════════════════════════════╝" + WHITE)

def loading():
    print("Processing", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()

def get_device_id():
    base = platform.node() + platform.system() + platform.machine()
    return hashlib.sha256(base.encode()).hexdigest()

def check_license():
    try:
        if not os.path.exists("key.txt"):
            print("❌ key.txt tidak ada")
            return

        key = open("key.txt").read().strip()
        device = get_device_id()

        res = requests.get(f"{API_URL}?key={key}&device={device}", timeout=5).text.strip()

        if res == "VALID":
            print(GREEN + "✅ License OK" + WHITE)
        else:
            print(RED + "❌ License invalid / server error" + WHITE)

    except:
        print("⚠️ Gagal cek license (offline?)")

def obfuscate():
    f = input("File: ")
    if not os.path.exists(f):
        print("❌ File tidak ada")
        return

    loading()
    os.system(f"pyarmor gen -O dist {f}")
    print("✅ Berhasil! (folder dist/)")

def menu():
    while True:
        print("\n[1] Obfuscate")
        print("[2] Donasi")
        print("[3] Exit")

        p = input("Pilih: ")

        if p == "1":
            obfuscate()
        elif p == "2":
            os.system(f"termux-open-url {DONASI_URL}")
        else:
            break

if __name__ == "__main__":
    banner()
    check_license()
    menu()
