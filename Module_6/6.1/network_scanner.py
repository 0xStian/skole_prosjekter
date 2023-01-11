from scapy.all import *
from scapy.layers.inet import Ether, TCP, IP, ICMP
from scapy.layers.l2 import ARP
from termcolor import colored

target_ip = "172.24.6.53/24"
ports = [80, 22, 23, 443]

def arp_scan(ip):
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    ans, unans = srp(request, timeout=2, retry=1)
    result =[]
    for sent, received in ans:
        result.append({"ip": received.psrc, "mac": received.hwsrc})
    return result
        
        
def syn_scan(ip, ports):
    sport = RandShort()
    print("-"*60)
    print("Scanning " + ip + " for open ports")
    for port in ports:
        pkt = sr1(IP(dst=ip)/TCP(sport=sport, dport=port, flags="S"), timeout=2, verbose=0)
        if pkt is None:
            print(colored("Port " + str(port) + " is closed", "red"))
        else:
            print(colored("Port " + str(port) + " is open", "green"))
    print("-"*60)
        
scanned = arp_scan(target_ip)
ip_addresses = []

for x in range(len(scanned)):
    ip_addresses.append(scanned[x]["ip"])
    
for x in ip_addresses:
    syn_scan(x, ports)

