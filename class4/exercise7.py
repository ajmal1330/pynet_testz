uthor__ = 'eaboytes'


from netmiko import ConnectHandler
from getpass import getpass

#password = getpass()
'''
Exercise instructions
Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
'''

#(Cisco 881)
pynet1 = {
    'device_type' : 'cisco_ios',
    'ip' : '184.105.247.70',
    #'snmp_port' : '161',
    'port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',
}

#(Cisco 881)
pynet2 = {
    'device_type': 'cisco_ios',
    'ip' : '184.105.247.71',
    #'snmp_port' : '161',
    'port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',
}

#(Arista vEOS switch)
pynetsw1  = {
    'device_type' : 'Arista',
    'ip' :'184.105.247.72',
    'ssh_port' : '22',
    'eapi_port' : '443',
    'username' : 'admin1',
    'password' : '99saturday',
}

#(Arista vEOS switch)
pynetsw2 = {
    'device_type' : 'Arista',
    'ip' : '184.105.247.73',
    'ssh_port' : '22',
    'eapi_port' : '443',
    'username' : 'admin1',
    'password' : '99saturday',
}
# (Arista vEOS switch)
pynetsw3 = {
    'device_type' : 'Arista',
    'ip' : '184.105.247.74',
    'ssh_port' : '22',
    'eapi_port' : '443',
    'username' : 'admin1',
    'password' : '99saturday',
}
#(Arista vEOS switch)
pynetsw4 = {
    'device_type' : 'Arista',
    'ip' : '184.105.247.75',
    'ssh_port' : '22',
    'eapi_port' : '443',
    'username' : 'admin1',
    'password' : '99saturday',
}

#(Juniper SRX)
pynetsrx1 = {
    'device_type' : 'juniper',
    'ip' : '184.105.247.76',
    'port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',
    'secret' : '',
}


cmd='logging buffered 8198'
ver = 'do sh run | inc '  + cmd
device = pynet2

def main():
    '''
    Logs into each router and executes commands cmd and ver 
    '''
    print '=' *80
    ssh_conn = ConnectHandler(**device)
    ssh_conn.config_mode()
    ssh_conn.send_command(cmd)
    output = ssh_conn.send_command(ver)
    prompt = ssh_conn.find_prompt()
    print '\n %s from %s \n %s' %(cmd, prompt, output)
    print
    print '=' *80

if __name__=="__main__":
    main()
