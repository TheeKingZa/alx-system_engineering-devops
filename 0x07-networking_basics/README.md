# Network Basics #0
[<](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x06-regular_expressions/README.md) 0x07 [>](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x08-networking_basics_2/README.md)
---

Need To Know?!
--------------

* OSI Model
	What it is?
	How many layers it has?
	How it is organized?

* What is a LAN
	Typical usage?
	Typical geographical size?

* What is a WAN
	Typical usage?
	Typical geographical size?

* What is the Internet
	What is an IP address?
	What are the 2 types of IP address?
	What is localhost?
	What is a subnet?
	Why IPv6 was created?

* TCP/UDP
	What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)?
	What is the main difference between TCP and UDP?
	What is a port?
	Memorize SSH, HTTP and HTTPS port numbers?
	What tool/protocol is often used to check if a device is connected to a network?

----------------------------------------------------------

OSI Model
The OSI (Open Systems Interconnection) Model is a conceptual framework used to understand and standardize network communication. It consists of seven layers, each with a specific role:

1.
Physical Layer: Deals with the physical medium of data transmission, such as cables and electrical voltages.

2.
Data Link Layer: Ensures reliable data transfer across a physical link. It is divided into two sub-layers: LLC (Logical Link Control) and MAC (Media Access Control).

3.
Network Layer: Responsible for routing and forwarding data packets. It includes IP (Internet Protocol).

4.
Transport Layer: Manages end-to-end communication, providing error detection and correction. It includes protocols like TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

5.
Session Layer: Establishes, maintains, and terminates communication sessions.

6.
Presentation Layer: Translates data between the application and lower layers, handling data encryption and compression.

7.
Application Layer: Provides application-specific services, like HTTP (Hypertext Transfer Protocol) for web browsing.

----------------------

LAN (Local Area Network)
LAN is a network that covers a small geographic area, like a home, office, or campus. It typically connects devices within close proximity. LANs are used for local data sharing and resource access.

* Typical Usage: File sharing, printer access, online gaming.
* Typical Size: Within a single building or campus.

--

WAN (Wide Area Network)
WAN spans a larger geographic area, connecting LANs across cities, countries, or continents. The internet is a global WAN.

* Typical Usage: Internet access, connecting remote offices.
* Typical Size: Global or regional coverage.

-----------------------

Internet
The Internet is a vast, global network of interconnected networks, enabling communication and data exchange worldwide.

IP Address
An IP (Internet Protocol) address is a numerical label assigned to devices on a network to identify them. There are two main types:

1.
IPv4 (Internet Protocol version 4): Uses 32-bit addresses (e.g., 192.168.1.1).

2.
IPv6 (Internet Protocol version 6): Uses 128-bit addresses (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

-------------------------

Localhost
Localhost refers to the loopback network interface of a device, often identified by the IP address 127.0.0.1. It allows a device to communicate with itself for testing purposes.

-------------------------

Subnet
A subnet is a portion of a larger network that can be divided for better organization and management. Subnetting helps optimize IP address allocation.

-------------------------

IPv6 Creation
IPv6 was created to address the exhaustion of IPv4 addresses. Its larger address space ensures a sufficient supply of unique IP addresses.

-------------------------
TCP/UDP
TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two primary data transfer protocols.

* TCP: Ensures reliable, ordered data delivery with error checking and correction.
* UDP: Offers faster, connectionless data transfer without reliability guarantees.

---------------------------

Ports
A port is a numeric identifier used to distinguish different services on a device. Memorize common port numbers:

* SSH(Secure Shell):22
* HTTP(Hypertext Transfer Protocol):80
* HTTPS(Secure HTTP):443
-----------------------------

Network Connectivity Tool
Ping, using the ICMP (Internet Control Message Protocol), is often used to check if a device is connected to a network and measure response times.
