import pyfiglet
import subprocess
import sys

banner_for_scanner = pyfiglet.figlet_format("Network Scanner")
print(banner_for_scanner)

def networkScanner(ip):

    subprocess.run(["python", "networkScanner.py", "-t", ip], shell=True)

ip = input("Enter the IP address to scan: ")    
networkScanner(ip)