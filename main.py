import pyfiglet
import subprocess
import sys
import portScanner


def networkScanner(ip):
    print("+" * 50)
    print("[*] Scanning the network for " + ip)
    subprocess.run(["python", "networkScanner.py", "-t",] + [ip])
    print("[+] Finished Scanning for MAC Addresses")
    print("+" * 50)

# def portScanner(ip):
#     print("+" * 50)
#     print("[*] Scanning the network for " + ip)
#     portScanner.scan_port(ip)
#     print("[+] Finished Scanning for open ports")
#     print("+" * 50)
    
def networkSniffer(ip):
    print("+" * 50)
    print("[*] Scanning the network for " + ip)
    subprocess.run(["python", "networkScanner.py", "-i", ] + [ip])
    print("[+] Finished Scanning for MAC Addresses")
    print("+" * 50) 

banner_for_scanner = pyfiglet.figlet_format("Network Scanner")
print(banner_for_scanner)

print("-"*60)
print("What do you want to do: \n")
print("1. Scan MAC/IP Address \n ")
print("2. Scan Open Ports \n ")
print("3. Intercept Web traffic (MITM) \n ")
print("4. Find IP Location \n")
print("5. Spoof MAC Address \n")
print("-"*60)
ip = sys.argv[1]
print(ip)
selection = int(input("Select your option: "))

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

# elif selection == '2':
#     portScanner(ip)
    
elif selection == '3':
    networkSniffer(ip)
else:
    print("[-] Command not found! exiting......")
    sys.exit()

   
