#!/usr/bin/env python

'''
Instructions:
Use Netmiko to connect to each of the devices in the database. Execute 'show version' on each device.
Calculate the amount of time required to do this. Note, your results will be more reliable if you use
Netmiko's send_command_expect() method. There is an issue with the Arista vEOS switches and Netmiko's
send_command() method.
'''

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django

def show_ver(a_device):
    '''Handles logging into each device and doing the show command'''
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address,
                                 password=creds.password,
                                 username=creds.username,
                                 port=a_device.port,
                                 secret='')
    print a_device
    print '#' * 80
    print remote_conn.send_command_expect('show ver')
    #print remote_conn.send_command("show ver") <== This was tried and worked well but method above was recommended
    print '#' * 80

def main():

    '''Creates a starting point to time entire transaction then goes into each device in
    the django database and executes a "show version" command provides the difference
    between starting time above and end time.  In other words, how long did this take.
    '''

    django.setup()

    start_time = datetime.now()

    devices = NetworkDevice.objects.all()
    for a_device in devices:
        show_ver(a_device)

    elapsed_time = datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)

if __name__ == "__main__":
    main()
