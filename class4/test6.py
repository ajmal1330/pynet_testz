#!/usr/bin/env python
__author__ = 'eaboytes'


from netmiko import ConnectHandler
from getpass import getpass

#password = getpass()
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

#for router_dict in (pynet1,pynet2,pynetsrx1):
#    router_dict['password'] = password

cmd='show arp'

def main():
    '''
    Logs into each router and collects the arp table
    '''
    print '=' *80
    for device in (pynet1,pynet2,pynetsrx1):
        ssh_conn = ConnectHandler(**device)
        output = ssh_conn.send_command(cmd)
        prompt = ssh_conn.find_prompt()
        print '\nShow arp from ' + prompt +'\n' +output
        print
        print '=' *80

if __name__=="__main__":
    main()
