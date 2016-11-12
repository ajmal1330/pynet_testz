#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django

def show_ver(a_device):
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type, ip=a_device.ip_address, password=creds.password,
                                 username=creds.username, port=a_device.port, secret='')
    print a_device
    print '#' * 80
    print remote_conn.send_command_expect("show ver")
    print '#' * 80

def main():
    django.setup()

    #Creates a starting point to time entire transaction
    start_time = datetime.now()

    #goes into each device in the django database and executes a "show version" command
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        show_ver(a_device)

    #provides the difference between starting time above and end time.  In other words, how long did this take.
    elapsed_time = datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)

if __name__ == "__main__":
    main()
