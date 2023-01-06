from misc import menu
import nmap3, os, json, ipaddress
nmap = nmap3.Nmap()

def scan_network():
    os.system("cls")
    ip_adress = input("Enter the IP address of the network you want to scan: ")
    if is_valid_ip(ip_adress):
        nmap = nmap3.NmapScanTechniques()
        result = nmap.nmap_tcp_scan(ipaddress, args=f"-p {input('Enter the ports you want to scan (0-65535): ')}")
    else:
        print("Invalid IP address.")
        scan_network()

def get_choice():
    choice = menu()
    match choice:
        case "1": scan_network()
        case "2": pass#scan_device()
        case "3": pass#save_results()
        case "4": exit()
        case _:   get_choice()


def is_valid_ip(ip_adress):
    try: 
        ipaddress.ip_network(ip_adress, strict=False)
        return True
    except ValueError: 
        return False
    


get_choice()


    
