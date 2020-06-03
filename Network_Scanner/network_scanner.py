#!/usr/bin/env python
import scapy.all as scapy
import argparse

def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help="Target IP/ IP range")
    options=parser.parse_args()
    return options
#allows for user console import
def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    #creates a arp packet instance
    #pdst labels the the ip we are looking for
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #creates a ethernet object,sets destination MAC to broadcast MAC
    #dst sets the broadcast MAC Address
    arp_req_brd=broadcast/arp_request
    #combines the broadcast and arp request
    answered_list=scapy.srp(arp_req_brd,timeout=1, verbose=False)[0]
    #gives the first element of the two lists which is the answered lsit
    #Allows us to send packets with our own custom ether part
    #verbose keyword removes unneccesary information

    clients_list=[]
    for element in answered_list:
        client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        #dict- stores the values in the answered_list to specific dictionary entries
        clients_list.append(client_dict)
        #psrc prints ip
        #hwsrc prints MAC Address
    return clients_list
def printer(result_lists):
    print("IP\t\t\tMAC Address\n-----------------------------------")
    for client in result_lists :
        print(client["ip"]+"\t\t"+client["mac"])

opts=get_args()
scan_list=scan(opts.target)
printer(scan_list)
#this will search all ip's in the subnet
