import pygeoip
import sys
import argparse

def args_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', help='IP address to lookup')
    args = parser.parse_args()
    ip_addr = args.ip_addr
    get_geo_info(ip_addr)
    return

def get_geo_info(ip):
    geo_ip = pygeoip.GeoIP('GeoLiteCity.dat')
    geo_info = geo_ip.record_by_addr(ip)
    for  key, value in geo_info.items():
        print('%s: %s'%(key, value))
    return geo_info

def ipaddress(ip_addr):
    argument = args_main()
    ip_addr = argument.ip_addr
    get_geo_info(ip_addr)

