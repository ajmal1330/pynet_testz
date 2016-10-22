#!/usr/bin/env python
#Class 7 Exercise 1
#Earl Aboytes

'''
Instructions:
Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the 'show interfaces'
output to obtain the 'inOctets' and 'outOctets' fields for each of the interfaces on the switch.
Accomplish this using Arista's pyeapi.
'''

import pyeapi

def main():
    #connect to switch and grab a "show interfaces"
    pynet_sw2 = pyeapi.connect_to('pynet-sw2')
    sh_int=pynet_sw2.enable('show interfaces')

    #strip off some of the extraneous data to get at what we want
    some_dict=sh_int[0]
    show_interfaces=some_dict['result']
    interfaces=show_interfaces['interfaces']
    data={}
    for interface, int_values in interfaces.items():
        int_counters = int_values.get('interfaceCounters', {})
        data[interface] = (int_counters.get('inOctets'), int_counters.get('outOctets'))

    #prints header to table of output
    print "\n{:12}{:>12}{:>12}".format("Interface", "In", "Out")

    #prints output to a table
    for Eth, octets in data.items():
        print "{:12} {:>12} {:>12}".format(Eth, octets[0], octets[1])
    print

if __name__=='__main__':
    main()
