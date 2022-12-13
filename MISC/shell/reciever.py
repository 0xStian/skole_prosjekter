import socket
import subprocess



socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost',6968)
socket.bind(server_address)


while True:
    data, address = socket.recvfrom(4096)
    data_str = data.decode('utf-8')
    
    if data_str == "!q":
        
        socket.sendto(b"!q", address)
        quit()
        
    else:
        print(f"\n[!] Recieved Command '{data_str}' from ip[{address[0]}] on port[{address[1]}]\n")  
        
        try:
            output = subprocess.check_output(data_str, shell=True)
        except:
            output = b"\n[!] Invalid Command"
            
        print("-------------------------------------------------------------------------------") 
        socket.sendto(output, address)
        
