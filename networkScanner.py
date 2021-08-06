from scapy.all import *
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request
    welcomed = scapy.srp(arp_broadcast, timeout=3, verbose=False)[0]
    
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
    
result = scan("172.16.180.0/24") 
print_result(result)   	