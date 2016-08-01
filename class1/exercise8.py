__author__ = 'eaboytes'
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("ipsec.txt")
#print cisco_cfg

c_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")
#print c_map
for i in c_map:
    print i.text
    for child in i.children:
        print child.text


