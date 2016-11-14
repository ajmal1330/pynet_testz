#!/usr/bin/env python

'''
Instructions:
Use threads and Netmiko to execute 'show version' on each device in the database. Calculate the amount
of time required to do this. What is the difference in time between executing 'show version' sequentially
versus using threads?
'''

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django
import threading
import time


def show_ver(a_device):
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type, ip=a_device.ip, password=a_device.password,
                                 username=a_device.username, port=a_device.port, secret='')
    print
    print '#' * 80
    print remote_conn.send_command_expect("show ver")
    print '#' * 80


def main():
    django.setup()
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    for a_device in devices:
        my_thread = threading.Thread(target=show_ver, args=(a_device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print some_thread
            some_thread.join()

    print "\nElapsed time:  " + str(datetime.now() - start_time)
if __name__ == "__main__":
    main()