ARP SPOOFER (RUN ON TERMINAL IN DEBIAN LINUX (i.e. KALI))
----------------------------------------------------------------------------------------------------------------------------


MAIN IDEA OF THE PROJECT:
-------------------------
To create a spoofer that can intercept request and responses between a machine and a router using the ARP protocol

**PURPOSE:**

Intercept the request and responses from the "victim" machine using a "man in the middle" attack.
-Allows us to monitor what is being done on the vicitim machine
-Allow us to dictate actions to take on the victim machine
-Allows us to send trojans or other attacks by acting as the router

**ARP Protocol (Address Resolution Protocol):**

communication protocol used for discovering the link layer address, such as a MAC address, 
associated with a given internet layer address, typically an IPv4 address

**WHAT WE DID:**

-Sent a response to the router or gateway, impersonating the victim machine, forcing the router to update its
ARP Logs with the Hackers MAC Address

-Ask the victim machine to store the Hacker's MAC in their ARP Logs,to create the connection between the victim and the Hacker
while impersonating the router with its IP

**WHY DO WE DO THIS:**

ARP has some security issues:

1.Clients can accept responses even if they did not send a request
  - This allows us to access a clients vunerability
  
2.Clients trust response without any verification



CODE AND TOOLS OVERVIEW:
------------------------
  **Methods:**
  
      spoof(target_ip,spoof_ip): Method that creates a spoof packet and sends it to other machine

      getMAC(ip): Get any MAC address passed an IP

      dynamicPrint(count):Allows for Dynamic Printing functionality in the project

      restore(dest_ip,src_ip): Restores orignal values (used in the try catch)

      spoofRepeat(boolT): Repeats spoof multiple times passing it to machine

  **TOOLS:**
  
    -Utilized Virtual Box:
      ->Kali Machine (Hacker)
      ->Windows 10 Machine(Victim)
      
    -Utilized Python Methods:
      ->Scapy:Scapy is a packet manipulation tool for computer networks
      ->Time
      ->Sys
      
    -Utilized buffers for Dynamic Printing
---

# Disclaimer
**Notice**

    This program is run on my own virtual box machines and set up. The code in this project can be and should be editied to fit your ip and mac address specifications. Ideal set up is necessary for proper efficeny.
---
***WARNING***

THIS CODE IS NOT USED FOR MALLICIOUS INTENT AND IS AN EDUCATIONAL PROJECT USED TO SHOWCASE MY ABILITIES AS A ETHICAL HACKER.
IF THIS CODE IS UTILIZED IN ANY FORM OF MALLICIOUS INTENT, BE INFORMED THAT PROPER LEAGAL COURSE OF ACTION CAN BE TAKEN ON THOSE WHO
USE IT BY LAW ENFORCEMENT AGENCIES.
      

