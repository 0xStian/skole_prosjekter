import socket
import subprocess

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    message = bytes(input("\n Command >").encode('utf-8'))
    socket.sendto(message,("localhost",6968))
    
    try:
        data, address = socket.recvfrom(4096)
        if data.decode("utf-8") in ["!q", ""]:
            quit()
        else:
            print("\n" + data.decode("utf-8"))
    except: 
        print("\n[!] Receiver is not listening for commands")
