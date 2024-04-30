import pygeoip
import sys
import argparse

# def args_main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-i', '--interface', help='IP address to lookup')
#     args = parser.parse_args()
#     return args

def get_geo_info(ip):
    try:
        geo_ip = pygeoip.GeoIP('./GeoLiteCity.dat')
        geo_info = geo_ip.record_by_addr(ip)
        if geo_info is None:
            return "No Information is avaliable in the IP"
        info = {
            'city': geo_info['city'],
            'country': geo_info['country_name'],
            'latitude': geo_info['latitude'],
            'longitude': geo_info['longitude']
        }
        return info
    except Exception as e:
        return f"An error has occured in this piece of code. Exiting"


# # ip = sys.argv[1]
# print(get_geo_info(ip))
