#!/usr/bin/env python
__author__ = 'eaboytes'

import telnetlib
import time

ip_addr="184.105.247.70"
name="pynet-rtr1"
t_port=23
t_timeout=5
uname="pyclass"
pw="88newclass"

def main():
    remote_conn = telnetlib.Telnet(ip_addr, t_port, t_timeout)
    output = remote_conn.read_until("sername:", t_timeout)
    print output
    remote_conn.write(uname + "\n")
    output = remote_conn.read_until("assword:", t_timeout)
    print output
    remote_conn.write(pw + "\n")
    time.sleep(5)
    output = remote_conn.read_very_eager()
    print output
    remote_conn.write("show ip interface brief" +"\n")
    time.sleep(5) 
    output = remote_conn.read_very_eager()
    print output
    remote_conn.close
if __name__=="__main__":
    main()
