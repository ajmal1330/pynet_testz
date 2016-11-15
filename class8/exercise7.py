
'''
6. Use threads and Netmiko to execute 'show version' on each device in the database.
Calculate the amount of time required to do this. What is the difference in time
between executing 'show version' sequentially versus using threads?

7. Repeat exercise #6 except use processes.
-pylint score: 7.78/10
-Results...Elapsed time:  0:00:41.061918
'''

from datetime import datetime
from multiprocessing import Process, Queue
from net_system.models import NetworkDevice
import django
from netmiko import ConnectHandler


def show_ver(a_device, queue):
    '''function connects to device using ORM and retrieves output from a "show version" command'''
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address,
                                 password=creds.password,
                                 username=creds.username,
                                 port=a_device.port,
                                 secret='')
    #print
    #print '#' * 80
    output = remote_conn.send_command_expect('show ver')
    #print '#' * 80
    queue.put(output)


def main():
    '''uses processes to retrieve "show version" output from all devices in ORM'''
    django.setup()
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    procs = []
    for a_device in devices:
        queue = Queue(maxsize=20)
        my_proc = Process(target=show_ver, args=(a_device,queue))
        my_proc.start()
        procs.append(my_proc)

        for a_proc in procs:
            print a_proc
            a_proc.join()

    print "\nElapsed time:  " + str(datetime.now() - start_time)
if __name__ == "__main__":
    main()
