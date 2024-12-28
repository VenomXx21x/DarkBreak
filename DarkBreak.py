import os
import time
from getpass import getpass

# Banner
def show_banner():
    print("""
    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
    ██████╔╝██████╔╝██║   ██║   ██║   █████╗  
    ██╔═══╝ ██╔═══╝ ██║   ██║   ██║   ██╔══╝  
    ██║     ██║     ╚██████╔╝   ██║   ███████╗
    ╚═╝     ╚═╝      ╚═════╝    ╚═╝   ╚══════╝
    """)
    print("Created by HacktifyDiaries\n")

# Check dependencies
def check_dependencies():
    try:
        import requests
    except ImportError:
        print("[!] Missing dependency: requests")
        print("Installing requests...")
        os.system("pip install requests")
        print("[+] Dependency installed.")

# Simulated brute force function
def brute_force(target_platform, username, password_list):
    print(f"[+] Starting brute force on {target_platform} for user: {username}")
    time.sleep(1)
    
    # Mock "password database" for simulation
    mock_password = "securepassword123"  # Correct password for simulation
    
    for password in password_list:
        print(f"[-] Trying password: {password.strip()}")
        time.sleep(0.5)  # Simulate delay
        
        if password.strip() == mock_password:
            print(f"[+] Correct password found: {password.strip()}")
            return True
    print("[-] Password not found in the provided list.")
    return False

# Main menu
def main():
    show_banner()
    check_dependencies()
    
    print("Select a platform to simulate brute force attack:")
    print("1. Facebook")
    print("2. Instagram")
    print("3. LinkedIn")
    print("4. Telegram")
    choice = input("Enter your choice (1-4): ")
    
    platforms = {1: "Facebook", 2: "Instagram", 3: "LinkedIn", 4: "Telegram"}
    target_platform = platforms.get(int(choice), None)
    
    if not target_platform:
        print("[!] Invalid choice. Exiting.")
        return
    
    username = input("Enter the target username: ")
    password_file = input("Enter the path to your password list file: ")
    
    try:
        with open(password_file, "r") as file:
            password_list = file.readlines()
    except FileNotFoundError:
        print("[!] Password file not found. Exiting.")
        return
    
    brute_force(target_platform, username, password_list)

if __name__ == "__main__":
    main()
