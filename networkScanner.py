from scapy.all import *
import scapy.all as scapy
import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range")
    arguments = parser.parse_args()
    return arguments

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request
    welcomed = scapy.srp(arp_broadcast, timeout=3, dest="target" verbose=False)[0]
    
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

arguments = parse()    
result = scan(arguments.target) 
print_result(result)   	