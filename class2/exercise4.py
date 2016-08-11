#!/usr/bin/env python
__author__ = 'eaboytes'
from snmp_helper import snmp_get_oid, snmp_extract

COMMUNITY_STRING = "galileo"
SNMP_PORT = 161
IP = ("184.105.247.70","184.105.247.71")
oid = ("1.3.6.1.2.1.1.5.0", "1.3.6.1.2.1.1.1.0")

def main():
    for p in IP:
        for i in oid:
            a_device = (p, COMMUNITY_STRING, SNMP_PORT)
            snmp_data = snmp_get_oid(a_device, oid=i)
            output = snmp_extract(snmp_data)
            print output +"\n"
    
if __name__=="__main__":
    main()
