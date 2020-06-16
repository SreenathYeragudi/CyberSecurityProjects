# DNS SPOOFER

**Purpose**

A computer program that can spoof a web server DNS and send fake websites and information to its victim.

**Our Purpose**

I wanted to utilize a man in the middle attack so that I could pass my own custom information to a victim

**Stipulations**

This Spoofer is written on python 2.7 and the netfilterqueue is native to python 2.7
---
To run this DNS SPOOFER  first
    1.)
        
        FOR LOCAL BROWSER DO THIS:
        
        1.iptables -I OUTPUT -j NFQUEUE --queue-num 0
        2.iptables -I INPUT -j NFQUEUE --queue-num 0
        
        FOR EXTERNAL MACHINES BROWSER:

        1.iptables -I FORWARD -j -NFQUEUE --queue-num0

    2.) Install netfilterqueue using pip commands (only on python 2.7 as of now)
    3.) Run the arp_spoofer program to establish the "Man-in-the-Middle" connection
    4.) Run the dns_spoofer in tandem as the arp_spoofer will allow you the connection
---
To allow packet forwarding from your Dabien Linux Terminal use the command:

    echo 1 > /proc/sys/net/ipv4/ip_forward
---
# Code and Tools
**Code Breakdown**

 I created these methods:
 
    1. process_packet(packet) ----> processes captured packet and uses it to spoof
    
---
**Tools**

process_packet(packet):

    ->use scapy tools us as get_payload() method to create a custom scapy packet
    
    ->used custom scapy packet to amnipulate data
    
    ->check if packet has DNS request layer using .haslayer(scapy.DNSRR)
    
    ->create a variable to store the query name using scapy_packet[scapy.DNSQR].qname
    
    ->use conditional to check if given data is in the query name
    
    ->create a custom answer field using scapy.DNSRR(rrname, rdata)
    
    ->manipulated the rrname and the rdata to the query name (qname) and a custom ip respectively
    
        -: this changes the values in the DNS request that will be sent to the victm and the DNS server
        
    ->Deleted the len and chksum from the IP and UDP sections
    
        -:Allows for us to bypass the DNS servers fail safe to ensure that we are not tampering
        
            del scapy_packet[scapy.IP].len
            
            del scapy_packet[scapy.IP].chksum
            
            del scapy_packet[scapy.UDP].len
            
            del scapy_packet[scapy.UDP].chksum
            
    ->Set the custom scapy packet payload to the packet that we are returning
    
        -:packet.set_payload(str(scapy_packet))
        

---
# Disclaimer
**Notice**

    This program is run on my own virtual box machines and set up. The code in this project can be and should be editied to fit you ip and mac address specifications. Ideal set up is necessary for proper efficeny.
---
***WARNING***

THIS CODE IS NOT USED FOR MALLICIOUS INTENT AND IS AN EDUCATIONAL PROJECT USED TO SHOWCASE MY ABILITIES AS A ETHICAL HACKER.
IF THIS CODE IS UTILIZED IN ANY FORM OF MALLICIOUS INTENT, BE INFORMED THAT PROPER LEAGAL COURSE OF ACTION CAN BE TAKEN ON THOSE WHO
USE IT BY LAW ENFORCEMENT AGENCIES.




