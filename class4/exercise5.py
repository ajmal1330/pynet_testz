#!/usr/bin/env python
__author__ = 'eaboytes'

'''
Exercise 5 Instructions:
Use Netmiko to enter into configuration mode on pynet-rtr2.
Also use Netmiko to verify your state (i.e. that you are currently in configuration mode).
'''

#import necessary modules
from netmiko import ConnectHandler
from getpass import getpass
import datetime
import time

#(Cisco 881)
pynet1 = {
    'device_type' : 'cisco_ios',
    'ip' : '184.105.247.70',
    'snmp_port' : '161',
    'ssh_port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',
}

#(Cisco 881)
pynet2 = {
    'device_type': 'cisco_ios',
    'ip' : '184.105.247.71',
    #'snmp_port' : '161',
    'port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',
}

#(Arista vEOS switch)
pynetsw1  = {
    'device_type' : 'Arista',
    'ip' :'184.105.247.72',
    'ssh_port' : '22',
    'eapi_port' : '443',
    'username' : 'admin1',
    'password' : '99saturday',
}

#(Arista vEOS switch)
pynetsw2 = {
    'device_type' : 'Arista',
    'ip' : '184.105.247.73',
    'ssh_port' : '22',
    'eapi_port' : '443',
    'username' : 'admin1',
    'password' : '99saturday',
}
# (Arista vEOS switch)
pynetsw3 = {
    'device_type' : 'Arista',
    'ip' : '184.105.247.74',
    'ssh_port' : '22',
    'eapi_port' : '443',
    'username' : 'admin1',
    'password' : '99saturday',
}
#(Arista vEOS switch)
pynetsw4 = {
    'device_type' : 'Arista',
    'ip' : '184.105.247.75',
    'ssh_port' : '22',
    'eapi_port' : '443',
    'username' : 'admin1',
    'password' : '99saturday',
}

#(Juniper SRX)
pynetsrx1 = {
    'device_type' : 'juniper',
    'ip' : '184.105.247.76',
    'ssh_port' : '22',
    'netconf_port' : '830',
    'username' : 'pyclass',
    'password' : '88newclass',
    'secret' : '',
}


#username = raw_input("Username:")
#password = getpass.getpass()



def main():
    '''
    Connects to router and switches to config mode
    '''
    pynet_rtr2 = ConnectHandler(**pynet2)
    pynet_rtr2.enable()
    pynet_rtr2.config_mode()
    
    '''
    Checks to see if you are in enable mode and prints results to screen
    '''
    if pynet_rtr2.check_config_mode() is True:
        output = pynet_rtr2.find_prompt()
        print output
    else:
        print 'You are NOT in config mode'
if __name__=="__main__":
    main()

