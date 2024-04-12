import sys
import socket 
from datetime import datetime

def scan_port(target_ip):
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        sock.close()
        
def scan_port_range(target_ip):
# target_ip = sys.argv[1]
    print("+"*50)
    print("[+] Scanning target IP address: ", target_ip)
    print("[+] Scanning started at: ", str(datetime.now()))
    print("+"*50)

    try:
        scan_port(target_ip)
        print("Scanning completed at: ", str(datetime.now()))
    except KeyboardInterrupt:
        print("[-] Ctrl+C detected! Exiting..........")
        sys.exit()
        
    except socket.error:
        print("[-] Hostname could not be resolved. Exiting..........")
        sys.exit()
        
