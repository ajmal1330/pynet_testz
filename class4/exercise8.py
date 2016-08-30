#!/usr/bin/env python
__author__ = 'eaboytes'


from netmiko import ConnectHandler
from devices import pynet2
from getpass import getpass


'''
 Use Netmiko to change the logging buffer size (logging buffered <size>) and to disable console logging (no logging console) from a file on both pynet-rtr1 and pynet-rtr2 
'''

username = raw_input('Username:')
password = getpass()
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
