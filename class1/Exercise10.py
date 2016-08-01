__author__ = 'eaboytes'
from ciscoconfparse import CiscoConfParse


cisco_cfg = CiscoConfParse("ipsec.txt")
#print cisco_cfg

c_map = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")
#print c_map
for i in c_map:
    print i.text
    for child in i.children:
        print child.text