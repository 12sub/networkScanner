import pyfiglet
import subprocess
import sys
import portScanner

banner_for_scanner = pyfiglet.figlet_format("Network Scanner")
print(banner_for_scanner)

def networkScanner(ip):
    print("+" * 50)
    print("[*] Scanning the network for " + ip)
    subprocess.run(["python", "networkScanner.py", "-t",] + [ip])
    print("[+] Finished Scanning for MAC Addresses")
    print("+" * 50)

def portScanner(ip):
    print("+" * 50)
    print("[*] Scanning the network for " + ip)
    portScanner.scan_port(ip)
    print("[+] Finished Scanning for open ports")
    print("+" * 50)

ip = sys.argv[1] 
networkScanner(ip)

portScanner(ip)