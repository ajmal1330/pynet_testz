uthor__ = 'eaboytes'
import pexpect
from getpass import getpass
import sys

#objective: Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
#pynet-rtr2 (Cisco 881)
hostname= 'pynet-rtr2'
ip_addr = '184.105.247.71'
snmp_port = '161'
ssh_port = '22'
username = 'pyclass'
#password = '88newclass'
password = getpass()

def main():
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, ssh_port))
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword')
    ssh_conn.sendline(password)
    ssh_conn.expect(hostname + '#')
    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect(hostname + '#')
    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect(hostname + '#')
    print ssh_conn.before
    print ssh_conn.after
if __name__=="__main__":
    main()
