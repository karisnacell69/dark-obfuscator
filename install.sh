#!/data/data/com.termux/files/usr/bin/bash

# ANTI ERROR
set -e

clear

# WARNA
PURPLE='\033[1;35m'
GREEN='\033[1;32m'
RED='\033[1;31m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
NC='\033[0m'

# BANNER
echo -e "${PURPLE}"
echo "======================================"
echo " DARK OBFUSCATOR INSTALLER ULTRA PRO "
echo "======================================"
echo -e "${NC}"

sleep 1

# LOADING
loading() {
    echo -ne "${CYAN}Processing"
    for i in {1..5}; do
        echo -ne "${GREEN} ●"
        sleep 0.3
    done
    echo -e "${NC}"
}

loading

# CEK INTERNET
echo -e "${YELLOW}[+] Checking internet...${NC}"
if ! ping -c 1 google.com > /dev/null 2>&1; then
    echo -e "${RED}[!] No internet connection!${NC}"
    exit 1
fi

# UPDATE REPO
echo -e "${YELLOW}[+] Setting repository...${NC}"
termux-change-repo || true

echo -e "${YELLOW}[+] Updating system...${NC}"
pkg update -y && pkg upgrade -y

# INSTALL DEPENDENCY
echo -e "${YELLOW}[+] Installing dependencies...${NC}"
pkg install -y python git clang make libffi openssl termux-api curl

# FIX PIP TERMUX (SAFE)
echo -e "${YELLOW}[+] Fixing pip (Termux safe)...${NC}"
python -m ensurepip --upgrade > /dev/null 2>&1 || true

# INSTALL MODULE TANPA ERROR
echo -e "${YELLOW}[+] Installing Python modules...${NC}"
pip install requests --no-cache-dir
pip install pyarmor --no-cache-dir || pip install pyarmor==7.7.0 --no-cache-dir

# SETUP DIRECTORY
echo -e "${YELLOW}[+] Setting up workspace...${NC}"
mkdir -p ~/dark-obfuscator
cd ~/dark-obfuscator

# DEFAULT KEY
echo -e "${YELLOW}[+] Creating default key...${NC}"
echo "DARK-TRIAL" > key.txt

# CREATE TOOL
echo -e "${YELLOW}[+] Creating main tool...${NC}"

cat > tool.py << 'EOF'
# (script kamu tetap di sini, tidak diubah)
EOF

chmod +x tool.py

sleep 1

# DONE
echo -e "${GREEN}"
echo "======================================"
echo "     INSTALL SUCCESS - ULTRA READY    "
echo "======================================"
echo -e "${NC}"

echo -e "${CYAN}Run this command:${NC}"
echo -e "${PURPLE}cd ~/dark-obfuscator && python tool.py${NC}"
