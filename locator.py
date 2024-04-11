import pygeoip
import sys

def get_geo_info(ip):
    geo_ip = pygeoip.GeoIP('GeoLiteCity.dat')
    geo_info = geo_ip.record_by_addr(ip)
    for  key, value in geo_info.items():
        print('%s: %s'%(key, value))
    return geo_info

ip_addr = sys.argv[1]
get_geo_info(ip_addr)

