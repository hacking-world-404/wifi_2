from os import system as c
import time
import random

# Colors
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

# Logo Function
def logo():
    c('clear')
    print(f"""{R}
██╗    ██╗██╗███████╗██╗███████╗
██║    ██║██║██╔════╝██║██╔════╝
██║ █╗ ██║██║███████╗██║█████╗  
██║███╗██║██║╚════██║██║██╔══╝  
╚███╔███╔╝██║███████║██║███████╗
 ╚══╝╚══╝ ╚═╝╚══════╝╚═╝╚══════╝
{P}     HACKING WORLD - WIFI HACK  TOOL
{A}-------------------------------------------------
""")

# Wifi Cracker Function (non-root)
def wifi_crack():
    logo()
    c('espeak "Wifi Hacking Starting"')
    wifi_name = input(f"{G}[+] Enter Wifi Name: ")

    print(f"\n{G}[*] Scanning for {wifi_name}...")
    for i in range(1, 6):
        print(f"{G}[*] Signal Strength: {random.randint(70,100)}%")
        time.sleep(0.7)

    print(f"\n{G}[✓] Locked on {wifi_name}")
    time.sleep(1)
    print(f"{G}[*] Starting Password Bruteforce Attack...")
    time.sleep(2)

    passwords = ["ATIK SIR 77", "ATIK SIR 77", "ATIK SIR 77", "ATIK SIR 77", "ATIK SIR 77"]
    for pw in passwords:
        print(f"{G}[*] Trying Password: {pw}")
        time.sleep(1.3)

    found_pass = random.choice(passwords)
    print(f"\n{G}[✓] Password Found: {G}{found_pass}")
    print(f"{R}[!] Note: Connect manually from your settings.")
    input(f"\n{G}Press Enter To Exit...")

# Start Tool
wifi_crack()