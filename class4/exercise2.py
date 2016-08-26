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

#sends command to router and returns router output
def send_command(remote_conn, cmd):
    cmd=cmd.rstrip()
    remote_conn.send(cmd+"\n")
    time.sleep(1)
    return remote_conn.recv(5000)

#logs into router and changes amount of memory allocated to the local log
def main():
    '''
    Connects to router using SSH and changes the logging buffer to 8196 bytes
    '''
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
    remote_conn=remote_conn_pre.invoke_shell()
    output=remote_conn.recv(5000)
    output = send_command(remote_conn, "config t")
    print output
    output = send_command(remote_conn, "logging buffered 8196")
    print output
    output = send_command(remote_conn, "do wr mem")
    print output
    output = send_command(remote_conn, "end")
    print output
    output = send_command(remote_conn, "show run | inc logging buffered")
    print output
if __name__=="__main__":
    main()
