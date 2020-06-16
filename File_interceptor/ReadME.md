# FILE INTERCEPTOR

**Purpose**

A computer program that can intercept specific downloaded files and send its own custom file to be downloaded

**Our Purpose**

I wanted to utilize a man in the middle attack and a interceptor so I can send trojans and or malware

**Stipulations**

This Interceptor is written on python 2.7 and the netfilterqueue is native to python 2.7
---
To run this Interceptor  first
    1.)
    
        FOR LOCAL BROWSER DO THIS:
        
        1.iptables -I OUTPUT -j NFQUEUE --queue-num 0
        2.iptables -I INPUT -j NFQUEUE --queue-num 0
        
        FOR EXTERNAL MACHINES BROWSER:

        1.iptables -I FORWARD -j -NFQUEUE --queue-num0

    2.) Install netfilterqueue using pip commands (only on python 2.7 as of now)
    3.) Run the arp_spoofer program to establish the "Man-in-the-Middle" connection
    4.) Run the file_inceptor in tandem as the arp_spoofer will allow you the connection
---
To allow packet forwarding from your Dabien Linux Terminal use the command:

    echo 1 > /proc/sys/net/ipv4/ip_forward
---
# Code and Tools
**Code Breakdown**
 I created these methods:
 
    1. process_packet(packet) ----> processes captured by the packet and uses it to send custom file
    
    2.set_load(packet,load) ---> set load for custom file
    
---
**Tools**

process_packet(packet):

    ->use scapy tools to get payload from a specific field
    
    ->used TCP field to understnad the packets leaving and entering the server using destination port and source port
   
   ->checked if .exe request was made in load field
    
    -> if so store the ack field of the specific scapy_packet
    
    -> for entering packets check if sequece is the same as the ack
    
        -: if its the same then delete the value from the list and replace the file being downloaded with custom file

---
# Disclaimer
**Notice**

    This program is run on my own virtual box machines and set up. The code in this project can be and should be editied to fit you ip and mac address specifications. Ideal set up is necessary for proper efficeny.
---
***WARNING***

THIS CODE IS NOT USED FOR MALLICIOUS INTENT AND IS AN EDUCATIONAL PROJECT USED TO SHOWCASE MY ABILITIES AS A ETHICAL HACKER.
IF THIS CODE IS UTILIZED IN ANY FORM OF MALLICIOUS INTENT, BE INFORMED THAT PROPER LEAGAL COURSE OF ACTION CAN BE TAKEN ON THOSE WHO
USE IT BY LAW ENFORCEMENT AGENCIES.
