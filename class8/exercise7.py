
'''
6. Use threads and Netmiko to execute 'show version' on each device in the database.
Calculate the amount of time required to do this. What is the difference in time between executing
'show version' sequentially versus using threads?

7. Repeat exercise #6 except use processes.
'''

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django
from multiprocessing import Process, current_process
import time


def show_ver(a_device):
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type, ip=a_device.ip, password=a_device.password,
                                 username=a_device.username, port=a_device.port, secret='')
    print
    print '#' * 80
    print remote_conn.send_command_expect('show ver')
    print '#' * 80

def main():
    django.setup()
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    procs = []
    for a_device in devices:
        my_proc = Process(target=show_ver, args=(a_device,))
        my_proc.start()
        procs.append(my_proc)

        for a_proc in procs:
            print a_proc
            a_proc.join()

    print "\nElapsed time:  " + str(datetime.now() - start_time)
if __name__ == "__main__":
    main()