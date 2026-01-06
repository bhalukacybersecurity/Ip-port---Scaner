import socket
import os
import time

# Colors
RED    = '\033[1;31m'
GREEN  = '\033[1;32m'
YELLOW = '\033[1;33m'
CYAN   = '\033[1;36m'
WHITE  = '\033[1;37m'
RESET  = '\033[0m'

def my_tool():
    os.system('clear')
    print(f"{CYAN}" + "#" * 50)
    print(f"{CYAN}#{' ' * 48}#{RESET}")
    print(f"{CYAN}#{' ' * 23}{WHITE}🛡️{CYAN}{' ' * 23}#{RESET}")
    print(f"{CYAN}#{' ' * 10}{GREEN}X_SHUVO_X - IP & PORT SCANNER{CYAN}{' ' * 10}#{RESET}")
    print(f"{CYAN}#{' ' * 48}#{RESET}")
    print(f"{CYAN}#{' ' * 8}{YELLOW}MADE BY BHALUKA CYBER SECURITY{CYAN}{' ' * 8}#{RESET}")
    print(f"{CYAN}" + "#" * 50 + f"{RESET}")
    
    raw_target = input(f"\n{WHITE}Enter Target URL: {RESET}")
    
    
    target = raw_target.replace("https://", "").replace("http://", "").split('/')[0]

    try:
        print(f"\n{YELLOW}[+] Scanning IP for: {target}...{RESET}")
        time.sleep(1) 
        ip = socket.gethostbyname(target)
        print(f"{GREEN}[!] Target IP: {ip}{RESET}")

        port_input = input(f"\n{WHITE}Enter Port: {RESET}")
        port = int(port_input)
        
        print(f"{YELLOW}[+] Checking port {port} on {ip}...{RESET}")
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"\n{GREEN}[SUCCESS] Port {port} is OPEN! ✅{RESET}")
        else:
            print(f"\n{RED}[FAILED] Port {port} is CLOSED. ❌{RESET}")
        
        sock.close()

    except Exception as e:
        print(f"\n{RED}[ERROR] Invalid URL or Network Issue: {e}{RESET}")

    print("\n" + f"{CYAN}" + "-" * 50 + f"{RESET}")

if __name__ == "__main__":
    my_tool()
