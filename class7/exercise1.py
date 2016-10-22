#!/usr/bin/env python
'''
Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the 'show interfaces'
output to obtain the 'inOctets' and 'outOctets' fields for each of the interfaces on the switch.
Accomplish this using Arista's pyeapi.
'''
import pyeapi
from pprint import pprint

def main():
    pynet_sw2 = pyeapi.connect_to('pynet-sw2')
    sh_int=pynet_sw2.enable('show interfaces')
    some_dict=sh_int[0]
    show_interfaces=some_dict['result']

    interfaces=show_interfaces['interfaces']
    pprint(interfaces)
if __name__=='__main__':
    main()
