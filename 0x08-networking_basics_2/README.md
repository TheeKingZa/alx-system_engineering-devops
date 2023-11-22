# Networking Basics 2
[<]() 0x08 [>](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x09-web_infrastructure_design/README.md)
---

Need To Know?!
---------------

What is localhost/127.0.0.1
What is 0.0.0.0
What is /etc/hosts
How to display your machine’s active network interfaces

----------------------------------------------------------

localhost/127.0.0.1:

* localhost refers to the loopback network interface of a device. It is often identified by the IP address 127.0.0.1.

* This address allows a device to communicate with itself. When you access "localhost" or "127.0.0.1" in a web browser or use it in network configurations, the data stays within the device and is not transmitted over a physical network. It is commonly used for testing and development purposes.
----------------------------------------------------------
0.0.0.0:

0.0.0.0 is a special IP address with multiple meanings depending on the context:
* In the context of network configurations, it can represent "all available network interfaces" on a device. When used as a binding address, it indicates that a service should listen on all available network interfaces or addresses.
* In the context of routing tables, it can represent the default route, indicating that all network traffic not matching any specific route should use the default route.
----------------------------------------------------------
/etc/hosts:

* /etc/hosts is a system file on Unix-based operating systems (such as Linux and macOS) that is used to map hostnames to IP addresses.

* It is a simple text file where you can define custom hostname-to-IP address mappings. This file is consulted before making DNS (Domain Name System) queries, so it can be used to override DNS settings locally on the system. You can use it to define custom hostnames and associate them with specific IP addresses.
----------------------------------------------------------

4.
Displaying Active Network Interfaces:

* To display the active network interfaces on your machine, you can use various commands depending on your operating system:

* On Linux or macOS, you can use the ifconfig or ip command to view network interfaces. For example:

bash
==Code==
ifconfig
# or
ip addr

* On Windows, you can use the ipconfig command:

cmd
==Code==
ipconfig

* These commands will provide a list of active network interfaces on your system, including details such as IP addresses, MAC addresses, and network configuration.
man or help
-----------
ifconfig
telnet
nc
cut
-----------

-----------
1.
ifconfig:
-----------

ifconfig, short for "interface configuration," is a command-line utility used in Unix-like operating systems (e.g., Linux and macOS) to configure and display network interfaces on a computer.
It provides information about active network interfaces, including their IP addresses, MAC addresses, network configuration, and more.
You can also use ifconfig to configure network interfaces, assign IP addresses, enable or disable interfaces, and set various network-related parameters.

-----------
2.
telnet:
-----------

telnet is a network protocol and a command-line utility that allows users to establish text-based interactive communication with remote systems over a network, typically the internet.
It was widely used for remote terminal access and administration of remote servers. However, it is considered insecure for most purposes today due to its lack of encryption, making data transmission vulnerable to interception.
Secure alternatives like SSH (Secure Shell) are commonly used in place of telnet for secure remote access.

-----------
3.
nc (netcat):
-----------
nc, short for "netcat," is a versatile networking utility that can be used for various network-related tasks.
It can act as both a client and a server, making it useful for tasks like banner grabbing, port scanning, file transfer, and creating simple network services.
nc is often referred to as the "Swiss Army knife" of networking utilities because of its wide range of capabilities.

-----------
4.
cut:
-----------

cut is a command-line tool used for text processing in Unix-like operating systems.
It is primarily used to extract specific columns or fields from lines of text, with fields separated by a delimiter (commonly a tab or space).
cut provides options to specify the delimiter and the field(s) you want to extract from each line of input text. It is commonly used in combination with other command-line utilities for data manipulation and parsing.
