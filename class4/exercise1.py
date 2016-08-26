author__ = 'eaboytes'

#import necessary modules
import paramiko
import getpass
import datetime
import time

#set variables for use below
cmd="show version"
ip="184.105.247.71"
port=22

username = raw_input("Username:")
password = getpass.getpass()

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def main():
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
    remote_conn=remote_conn_pre.invoke_shell()
    output=remote_conn.recv(5000)
    print output
    remote_conn.send("terminal length 0\n")
    time.sleep(1)
    remote_conn.send("show version\n")
    time.sleep(1)
    output=remote_conn.recv(5000)
    print output
if __name__=="__main__":
    main()
