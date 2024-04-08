import socket
socket.setdefaulttimeout(2)
sock = socket.socket()
ip_address = input("Enter IP address: ")
port = int(input("Enter port: "))
sock.connect((ip_address, port))
print("Connected to server" + sock.recv(1024))
sock.close()
