#Discord ; twiezbtw
#GitHub ; twiez
# <:

import os
import time
import requests

# Renk kodları
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# Başlık değiştirme
os.system('title Netseek * twiez')  # Burada istediğiniz başlığı yazabilirsiniz

# ASCII art başlıkd
def display_banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = YELLOW + r"""
 ███▄    █ ▓█████▄▄▄█████▓  ██████ ▓█████ ▓█████  ██ ▄█▀
 ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▒██    ▒ ▓█   ▀ ▓█   ▀  ██▄█▒ 
▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░░ ▓██▄   ▒███   ▒███   ▓███▄░ 
▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░   ▒   ██▒▒▓█  ▄ ▒▓█  ▄ ▓██ █▄ 
▒██░   ▓██░░▒████▒ ▒██▒ ░ ▒██████▒▒░▒████▒░▒████▒▒██▒ █▄
░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░▒ ▒▒ ▓▒
░ ░░   ░ ▒░ ░ ░  ░   ░    ░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░░ ░▒ ▒░
   ░   ░ ░    ░    ░      ░  ░  ░     ░      ░   ░ ░░ ░ 
         ░    ░  ░              ░     ░  ░   ░  ░░  ░   
""" + RESET
    print(banner)
    print(YELLOW + "Loading..." + RESET)
    time.sleep(2)  # Kullanıcıya Loading ekranı için süre tanıma
    os.system("cls" if os.name == "nt" else "clear")  # Loading yazısını kaldır
    print(banner)  # Sadece banner kalsın

# IP bilgilerini alma
def track_ip():
    ip_address = input(YELLOW + "\nEnter IP address: " + RESET)
    
    # Bilgileri ekrana yazmadan önce ekranı temizleme
    os.system("cls" if os.name == "nt" else "clear")
    
    try:
        response = requests.get(f"https://ipapi.co/{ip_address}/json/")
        data = response.json()
        
        # Çekilen bilgileri gösterme
        print(YELLOW + "IP Address Information:" + RESET)
        print(f"{YELLOW}IP Address:{RESET} {RED}{data.get('ip', 'Unknown')}{RESET}")
        print(f"{YELLOW}Network:{RESET} {RED}{data.get('network', 'Unknown')}{RESET}")
        print(f"{YELLOW}City:{RESET} {RED}{data.get('region', 'Unknown')}{RESET}")
        print(f"{YELLOW}Region:{RESET} {RED}{data.get('city', 'Unknown')}{RESET}")
        print(f"{YELLOW}Region Code:{RESET} {RED}{data.get('region_code', 'Unknown')}{RESET}")
        print(f"{YELLOW}Country:{RESET} {RED}{data.get('country_name', 'Unknown')}{RESET}")
        print(f"{YELLOW}Country Code:{RESET} {RED}{data.get('country', 'Unknown')}{RESET}")
        print(f"{YELLOW}Country Capital:{RESET} {RED}{data.get('country_capital', 'Unknown')}{RESET}")
        print(f"{YELLOW}Postal Code:{RESET} {RED}{data.get('postal', 'Unknown')}{RESET}")
        print(f"{YELLOW}Latitude:{RESET} {RED}{data.get('latitude', 'Unknown')}{RESET}")
        print(f"{YELLOW}Longitude:{RESET} {RED}{data.get('longitude', 'Unknown')}{RESET}")
        print(f"{YELLOW}Timezone:{RESET} {RED}{data.get('timezone', 'Unknown')}{RESET}")
        print(f"{YELLOW}Currency:{RESET} {RED}{data.get('currency', 'Unknown')}{RESET}")
        print(f"{YELLOW}Currency Code:{RESET} {RED}{data.get('currency_name', 'Unknown')}{RESET}")
        print(f"{YELLOW}Languages:{RESET} {RED}{data.get('languages', 'Unknown')}{RESET}")
        print(f"{YELLOW}Organization:{RESET} {RED}{data.get('org', 'Unknown')}{RESET}")
        print(f"{YELLOW}ASN:{RESET} {RED}{data.get('asn', 'Unknown')}{RESET}")
        print(f"{YELLOW}Continent Code:{RESET} {RED}{data.get('continent_code', 'Unknown')}{RESET}")
        print(f"{YELLOW}In EU:{RESET} {RED}{data.get('in_eu', 'Unknown')}{RESET}")
        print(f"{YELLOW}Country Population:{RESET} {RED}{data.get('country_population', 'Unknown')}{RESET}")
        print(f"{YELLOW}Calling Code:{RESET} {RED}+{data.get('country_calling_code', 'Unknown')}{RESET}")
        

    except Exception as e:
        print(RED + f"An error occurred: {e}" + RESET)

    # Menüye dönüş için kullanıcıdan giriş bekleme
    while True:
        back_to_menu = input(YELLOW + "\nTo return to the menu, type [ 0 ]: " + RESET)
        if back_to_menu == "0":
            break
        else:
            print(RED + "Invalid input. Please type [ 0 ] to return." + RESET)

# Menü
def menu():
    while True:
        print(f"{YELLOW}[ + ]{RESET} {RED}https://github.com/twiez{RESET}")
        print(YELLOW + "\n[ 1 ] Track IP" + RESET)
        print()
        print(YELLOW + "[ 2 ] Exit" + RESET)
        choice = input(YELLOW + "\nroot@netseek ~>: " + RESET)

        if choice == "1":
            track_ip()
        elif choice == "2":
            print(YELLOW + "Exiting program. Goodbye!" + RESET)
            break
        else:
            print(RED + "Invalid choice. Please try again." + RESET)

# Program başlangıcı
if __name__ == "__main__":
    display_banner()  # Banner ve loading ekranını göster
    menu()  # Menüye geçiş
