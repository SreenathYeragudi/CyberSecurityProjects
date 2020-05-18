#!usr/bin/env python
import subprocess
import optparse
import re
#uses the commands that we used previously
def parser():
    #use pyton3 instead of python when running this code
    parser= optparse.OptionParser()
    #anything in capital letters in python is a class
    #parse is the object of the OptionParser class
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
    #first two commas create the options in terminal
    #third and fourth commas add information about this call to the terminal calls dest, and help
    parser.add_option("-m","--mac",dest="mac",help="puts in a new MAC address")
    (options,args)=parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify interface")
    elif not options.mac:
        parser.error("[-] Please specify new mac address")
    return options
#sets the two sets of info that parse_args sends and saves them as opts and args


def mac_changer(interFc,new_MAC):
    print("[+] Changing MAC address for "+interFc+ " to "+new_MAC)
    subprocess.call("ifconfig "+ interFc + " down",shell=True)
    subprocess.call("ifconfig "+ interFc +" hw ether ",shell=True )
    subprocess.call("ifconfig "+ interFc +" up",shell=True)
def get_curr_Mac(interface):
    res=subprocess.check_output(["ifconfig", interface])
    #catches and stores the terminal output
    mac_address_sresult=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", res)
    #regex code to simplfy result
    if(mac_address_sresult):
        return mac_address_sresult.group(0)
    else:
        print("MAC address cannot be read")

options=parser()
print("Old MAC address: "+ options.mac)
mac_changer(options.interface,options.mac)
curr_Mac=get_curr_Mac(options.interface)
if(curr_Mac==options.mac):
    print("MAC has not changed:"+curr_Mac)
else:
    print(" ")
    print("New MAC is: "+curr_Mac)
