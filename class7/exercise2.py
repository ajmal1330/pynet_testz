#!/usr/bin/env python
#Week 7 Exercise 2
#Earl Aboytes

'''
Instructions:
 Using Arista's pyeapi, create a script that allows you to add a VLAN (both the VLAN ID and the VLAN name).

Your script should first check that the VLAN ID is available and only add the VLAN if it doesn't already exist.
Use VLAN IDs between 100 and 999.  You should be able to call the script from the command line as follows:

   python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.

   python eapi_vlan.py --remove 100          # remove VLAN100

Once again only remove the VLAN if it exists on the switch.  You will probably want to use Python's argparse
to accomplish the argument processing.

In the lab environment, if you want to directly execute your script, then you will need to use
'#!/usr/bin/env python' at the top of the script (instead of '!#/usr/bin/python').

--Switch information
username: eapi
password: 7maxwell7
host: 184.105.247.73
transport: https
'''

#import statements
import pyeapi
import argparse
#End Import

def check_vlan(vlanid):
    '''
    Check switch for vlan given in CLI. If vlan is configured on the switch, the name will be returned
    If the vlan is not configured in the switch, a value of fals will be returned
    '''
    vlanid=str(vlanid)
    cmd='show vlan {}'.format(vlanid)

    '''
    Error handling in this function since executing a "show vlan" command using a vlan that does not exist in the
    switch will return an error.  We need a way of continuing to run the function even though an error is given.
    The pyeapi.eaplib.CommandError is raised when the vlan does not exist. Keyerror is a built-in python error and is
    raised when a mapping (dictionary) key is not found in the set of existing keys.
    '''
    try:
        pynet_sw2 = pyeapi.connect_to('pynet-sw2')
        sw_resp = pynet_sw2.enable(cmd)
        find_vlan = sw_resp[0]['result']['vlans']
        return find_vlan[vlanid]['name']
    except (pyeapi.eapilib.CommandError, KeyError):
        pass
    return False
#END check_vlan function

def main():
    parser = argparse.ArgumentParser(description='Add or remove vlan after checking for existence.')
    parser.add_argument('--name', help='supply a descriptive name for this vlan which should be different from the id')
    parser.add_argument('vlanid', help='VLAN number to create or remove', action='store', type=int)
    parser.add_argument(
        '--remove',
        help='Use this command to remove the vlan from the switch. Only the vlan id is needed',
        action='store_true'
    )
    args=parser.parse_args()


    vlanid = args.vlanid
    remove = args.remove
    name = args.name

    #verify existence of vlan in switch
    vlan_exists=check_vlan(vlanid)

    '''Actions are below. If the action is to remove a vlan, the switch is checked to see if it is configured.
    if not, the vlan is removed.
    '''
    if remove:
       if vlan_exists:
           cmd='no vlan {}'.format(vlanid)
           pynet_sw2 = pyeapi.connect_to('pynet-sw2')
           pynet_sw2.config(cmd)
           print 'VLAN {} removed'.format(vlanid)
       else:
           print 'Nothing to do here! VLAN {} does not exist on switch'.format(vlanid)
    #if action is not to remove but add a vlan, first check to see if it exists
    else:
        if vlan_exists:
            if name is not None and vlan_exists != name:
                cmd=[]
                cmd1 = cmd.append('vlan {}'.format(vlanid))
                cmd2 = cmd.append('name {}'.format(name))
                pynet_sw2 = pyeapi.connect_to('pynet-sw2')
                pynet_sw2.config(cmd)
                print 'Vlan found on switch but without a name. Name added to vlan.'
            else:
                print 'Vlan found on switch with name. Nothing to do here'
        else:
            cmd = []
            cmd1 = cmd.append('vlan {}'.format(vlanid))
            cmd2 = cmd.append('name {}'.format(name))
            pynet_sw2 = pyeapi.connect_to('pynet-sw2')
            pynet_sw2.config(cmd)
            print 'Vlan NOT found on switch Adding Vlan.'
if __name__=='__main__':
    main()

