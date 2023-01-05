import nmap3
import os
from termcolor import colored, cprint
nmap = nmap3.Nmap()

ip_adress = "192.168.0.112" #input("Enter IP adress: ")

def logo():
    print(colored("                      __                ", "magenta"))
    print(colored("______   ____________/  |_  ___________ ", "magenta"))
    print(colored("\____ \ /  _ \_  __ \   __\/ __ \_  __ \\", "magenta"))
    print(colored("|  |_> >  <_> )  | \/|  | \  ___/|  | \/", "magenta"))
    print(colored("|   __/ \____/|__|   |__|  \___  >__|   ", "blue"))
    print(colored("|__|                           \/       ", "blue"))

def print_ports(ip_adress):
    os.system("cls");logo()
    print(colored("Scanning for ports...", "black"))
    results = nmap.scan_top_ports(ip_adress)
    os.system("cls");logo()
    print(colored("="*55, "black"))
    for x in range(len(results[ip_adress]["ports"])):
        ports = results[ip_adress]["ports"][x]
        protocol = ports['protocol']
        port = ports['portid']
        state = ports['state']
        service = ports['service']['name']
        fullip = f"{ip_adress}:{port}"
        if state == "open":
            print(colored(f"[+] {state.ljust(10)} {fullip.ljust(1)}      {service.center(20)}     ", "magenta"))
        elif state == "closed":
            print(colored(f"[-] {state.ljust(10)} {fullip.ljust(1)}      {service.center(20)}     ", "black"))
    print(colored("="*55, "black"))
    input(colored("\nPress enter to continue...", "black"))
    menu()
        
        
def print_open_ports(ip_adress):
    os.system("cls");logo()
    print(colored("Scanning for ports...", "black"))
    results = nmap.scan_top_ports(ip_adress)
    os.system("cls");logo()
    print(colored("="*55, "black"))
    for x in range(len(results[ip_adress]["ports"])):
        ports = results[ip_adress]["ports"][x]
        protocol = ports['protocol']
        port = ports['portid']
        state = ports['state']
        service = ports['service']['name']
        if state == "open":
            print(colored(f"[+] {state}   | {ip_adress}:{port} | {service}", "magenta"))
    print(colored("="*55, "black"))
    input(colored("\nPress enter to continue...", "black"))
    menu()
        
def menu():
    os.system("cls")
    logo()
    print(colored("="*55, "black"))
    print(colored("1. Print Common Ports", "magenta"))
    print(colored("2. Print Open Common Ports", "magenta"))
    print(colored("3. Exit", "magenta"))
    print(colored("="*55, "grey"))
    choice = input(colored("Enter your choice: ", "blue"))
    match choice:
        case "1": print_ports(ip_adress)
        case "2": print_open_ports(ip_adress)
        case "3": exit()
        case _:   menu()
        
menu()