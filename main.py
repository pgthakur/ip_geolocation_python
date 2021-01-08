# coded by : Prabhat Gaurav
import os
import urllib.request as urllib2
import json
import socket
from pip._vendor.distlib.compat import raw_input
import logging

print(os.name)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)
try:
    while True:
        ip = raw_input("what is your target ip: ")
        url = "http://ip-api.com/json/"
        response = urllib2.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)
        print("IP: " + values['query'])
        print("City: " + values['city'])
        print("ISP: " + values['isp'])
        print("Country: " + values['country'])
        print("Region: " + values['region'])
        print("Time Zone: " + values['timezone'])
        print("Country Code: " + values['countryCode'])
        print("Zip Code: " + values['zip'])
        print("Organisation: " + values['org'] + "\t")
        print("as: " + values['as'])
        break
except BaseException:
    logging.warning("CHECK YOUR IP ADDRESS!")
