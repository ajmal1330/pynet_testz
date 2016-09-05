#!/usr/bin/env python
__author__ = 'eaboytes'


from netmiko import ConnectHandler
from getpass import getpass

'''
Exercise instructions
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
'''

#(Cisco 881)
pynet1 = {
    'device_type' : 'cisco_ios',
    'ip' : '184.105.247.70',
    #'snmp_port' : '161',
    'port' : '22',
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
    'port' : '22',
#    'netconf_port' : '830',
    'username' : 'pyclass',
    'password' : '88newclass',
    'secret' : '',
}


def main():
    '''
    Logs into each router and collects the arp table
    '''
    print '=' *80
    pynet_rtr1 = ConnectHandler(**pynet1)
    pynet_rtr1.enable()
    output = pynet_rtr1.send_command('show arp')
    print '\nShow arp from pynet1\n' +output
    print
    print '=' *80

    pynet_rtr2 = ConnectHandler(**pynet2)
    pynet_rtr2.enable()
    output = pynet_rtr2.send_command('show arp')
    print '\nShow arp from pynet2\n' +output
    print
    print '=' *80

    pynet_srx1 = ConnectHandler(**pynetsrx1)
    output = pynet_srx1.send_command('show arp')
    print '\nShow arp from SRX' +output
if __name__=="__main__":
    main()
