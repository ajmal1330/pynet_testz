#!/usr/bin/env python
__author__ = 'eaboytes'

'''
Devices used in exercises this week.
'''

#(Cisco 881)
pynet1 = {
    'device_type' : 'cisco_ios',
    'ip' : '184.105.247.70',
    #'snmp_port' : '161',
    'port' : '22',
    #'username' : 'pyclass',
#    'password' : '88newclass',
}

#(Cisco 881)
pynet2 = {
    'device_type': 'cisco_ios',
    'ip' : '184.105.247.71',
    #'snmp_port' : '161',
    'port' : '22',
#    'username' : 'pyclass',
#    'password' : '88newclass',
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
    'port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',
    'secret' : '',
}
