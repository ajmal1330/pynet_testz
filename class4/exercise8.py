#!/usr/bin/env python
__author__ = 'eaboytes'


from netmiko import ConnectHandler

'''
 Use Netmiko to change the logging buffer size (logging buffered <size>) and to disable console logging (no logging console) from a file on both pynet-rtr1 and pynet-rtr2 
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
    'username' : 'pyclass',
    'password' : '88newclass',
    'secret' : '',
}


ver = 'sh run | inc logging buffered'
device = pynet2

def main():
    '''
    Logs into each router and executes commands from file config_file.txt. Verification of config change. 
    '''
    print '=' *80
    ssh_conn = ConnectHandler(**device)
    output = ssh_conn.config_mode()
    print output
    output = ssh_conn.send_config_from_file(config_file='config_file.txt')
    print output
    output = prompt = ssh_conn.find_prompt()
    output = ssh_conn.send_command(ver)
    print '\n %s from %s \n %s' %(ver, prompt, output)
    print
    print '=' *80

if __name__=="__main__":
    main()
