import pyfiglet
import subprocess
import sys
import portScanner
import locator
import spoofer

def networkScanner(ip):
    print("+" * 50)
    print("[*] Scanning the network for " + ip)
    subprocess.run(["python", "networkScanner.py", "-t",] + [ip])
    print("[+] Finished Scanning for MAC Addresses")
    print("+" * 50)

def Scanner(ip):
    print("+" * 50)
    print("[*] Scanning the network for " + ip)
    portScanner.scan_port_range(ip)
    print("[+] Finished Scanning for open ports")
    print("+" * 50)
    
def networkSniffer(ip):
    print("+" * 50)
    print("[*] Scanning the network for " + ip)
    subprocess.run(["python", "networkScanner.py", "-i", ] + [ip])
    print("[+] Finished Scanning for MAC Addresses")
    print("+" * 50) 
    
def Geo_locator(ip):
    print("+" * 50)
    print("[*] Scanning the network for " + ip)
    locator.get_geo_info(ip)
    print("[+] Finished Scanning for IP Location")
    print("+" * 50)
    
def MacSpoofer(target, gateway):
    print("+" * 50)
    print("[*] Scanning the network for " + ip)
    subprocess.run(["python", "networkScanner.py", "-t", ] + [target] + ["-g"] + [gateway])
    print("[+] Finished Spoofing MAC address")
    print("+" * 50)

banner_for_scanner = pyfiglet.figlet_format("Network Hacker")
print(banner_for_scanner)

ip = sys.argv[1]
print("-"*60)
print("What do you want to do: \n")
print("1. Scan MAC/IP Address \n ")
print("2. Scan Open Ports \n ")
print("3. Intercept Web traffic (MITM) \n ")
print("4. Find IP Location \n")
print("5. Spoof MAC Address \n")
print("-"*60)

print(ip)
selection = input("Select your option: ")

# match selection:
#     case '1':
#         networkScanner(ip)
#         break
#     case '2':
#         portScanner(ip)
#         break
#     case '3':
#         networkSniffer(ip)
#         break
#     case _:
#         print("[-] Command not found! exiting......")
#         sys.exit()

if selection == '1': 
    networkScanner(ip)

elif selection == '2':
    Scanner(ip)
    
elif selection == '3':
    networkSniffer(ip)
    
elif selection == '4':
    Geo_locator(ip)
elif selection == '5':
    MacSpoofer(target=ip, gateway=sys.argv[2])
else:
    print("[-] Command not found! exiting......")
    sys.exit()

   
