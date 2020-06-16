# Packet Sniffer Information

**Purpose**

A computer program that can intercept and log traffic that passes over a digital network or part of a network.
Allows for a hacker to store data and is commonly used in a "Man-in-the-Middle" attack

**Our Purpose**

I wanted to keep track of urls that a user is accessing on a machine as well as Username and Password logins

**Stipulations**

This Sniffer is utilized for http websites only as of now ....

---
To run this "Man-in-the-Middle"  attack first

    1. Run the arp_spoofer (FILES IN OTHER PROJECT) program to establish the "Man-in-the-Middle" connection
    2. Run the packet_sniffer in tandem as the arp_spoofer will allow you the connection
---
To allow packet forwarding from your Dabien Linux Terminal use the command:

    echo 1 > /proc/sys/net/ipv4/ip_forward
---
# Code and Tools
**Code Breakdown**
 I created these methods:
 
    1. sniff(interface) ----> sniffs the victim for packets
    2. printEff(split,usrKey) ----> allows for easier printing
    3. getUrl(packet) ----> gets url packet from http layer after connection is established
    4. get_login(packet) ----> gets specific login credentials from a packet using layer detection
    5. process_sniffed_packet(packet) ----> get sniffed packet and translates it using layer detection and retrieves data
---
**Tools**
sniff(interface):

    -Used scapy sniff module to assit in the sniffing and establishment of connection through eth0
    -Has a call back operator that sends the packets to the process_sniffed_packet function

printEff(split,usrKey):

    -Used split to organize output

getUrl(packet):

    -uses function that are part of layer dection such as .Host and .Path to retrieve data from the packet request (packet[http.HTTPRequest])

get_login(packet):

    - -uses function that are part of layer dection such as .load to retrieve data from the load of the  packet request (packet[http.HTTPRequest])

process_sniffed_packet(packet):

    -accepets the packets from the callback of sniff(interface)
    -searches packet for http layer using packet.haslayer(http.HTTPRequest)
    -calls the getUrl(packet) and stores its information tracking every url accessed by external machine
    -calls get_login(packet)
    
        -> searches packet for the Raw data layer that stores the login and password information
        ->then collects the load of the Raw data and stores it to be accessed when called.
---
# Disclaimer
**Notice**

    This program is run on my own virtual box machines and set up. The code in this project can be and should be editied to fit your ip and mac address specifications. Ideal set up is necessary for proper efficeny.
---
***WARNING***

THIS CODE IS NOT USED FOR MALLICIOUS INTENT AND IS AN EDUCATIONAL PROJECT USED TO SHOWCASE MY ABILITIES AS A ETHICAL HACKER.
IF THIS CODE IS UTILIZED IN ANY FORM OF MALLICIOUS INTENT, BE INFORMED THAT PROPER LEAGAL COURSE OF ACTION CAN BE TAKEN ON THOSE WHO
USE IT BY LAW ENFORCEMENT AGENCIES.
