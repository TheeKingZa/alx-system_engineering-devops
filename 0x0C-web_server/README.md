# Web Server
[<](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x0B-ssh/README.md) 0x0C [>](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x0D-web_stack_debugging_0/README.md)
---

Concepts
For this project, we expect you to look at this concept:

* [What is a Child Process?](#what-is-a-child-process)

# NEED TO KNOW?
  * [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
  * [Nginx](https://en.wikipedia.org/wiki/Nginx)
  * [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
  * [Child process concept page](#what-is-a-child-process)
  * [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
  * [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
  * [HTTP redirection](https://moz.com/learn/seo/redirection)
  * [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
  * [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

1. [Web Server](#web-server)
2. [Child Process](#child-process)
3. [Parent and Child Processes in Web Servers](#parent-and-child-processes-in-web-servers)
4. [HTTP Requests](#http-requests)
5. [DNS](#dns)
6. [DNS Stands For](#dns-stands-for)
7. [DNS Main Role](#dns-main-role)
8. [DNS Record Types](#dns-record-types)
    - [A Record](#a-record)
    - [CNAME Record](#cname-record)
    - [TXT Record](#txt-record)
    - [MX Record](#mx-record)

For reference:
  * [RFC 7231 (HTTP/1.1)](https://datatracker.ietf.org/doc/html/rfc7231)
  * [RFC 7540 (HTTP/2)](https://datatracker.ietf.org/doc/html/rfc7540)

man or help:
  * [scp](https://linux.die.net/man/1/scp)
  * [curl](https://linux.die.net/man/1/curl)

[^](#web-server)

# **Background Context**
  In this project, some of the tasks will be graded on 2 aspects:

    1. Is your web-01 server configured according to requirements
    2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example,

    if I need to create a file /tmp/test containing the string hello world and modify the  configuration of Nginx to listen on port 8080 instead of 80,
    I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

    sylvain@ubuntu cat 88-script_example
    #!/usr/bin/env bash
    # Configuring a server with specification XYZ
    echo hello world > /tmp/test
    sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
    sylvain@ubuntu

As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an [SRE](https://www.atlassian.com/incident-management/devops/sre), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.

A good Software Engineer is a [lazy Software Engineer](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb).

[imagehere]

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

    * start a Ubuntu 16.04 sandbox
    * run your script on it
    * see how it behaves

[^](#web-server)

# What is a child process?

Although it may sound like something out of a parenting handbook or a psychological journal, the term child process actually has nothing to do with human development. If you run a Unix or Linux dedicated server, you have likely encountered child processes without even knowing it. Therefore, it is good to know what child processes are and how they work.

A child process is a process created by another process. The creator process is properly called the “parent process”. The benefit of a child process is that it can start or stop at will without affecting the parent process. The child process is, however, is typically dependent on the parent process. If the parent process dies, the child process becomes an orphan process.

In normal server operations, the kernel may initiate child processes, and other programs, such as Apache, may have them as well. Apache creates child processes (or children, if you prefer) whenever the number of requests (web page accesses from users) exceeds the maximum allowed number of requests. When the maximum number of child process requests is exceeded, another child process spawns.

To view all running processes along with their child processes in a “tree” format, use the following command:

    $ ps axf

For more information about child processes, see this [documentation](https://www.gnu.org/software/libc/manual/html_node/Processes.html#Processes).


[^](#web-server)
---
## Web Server

    A web server is a software application or hardware device
    responsible for serving content (web pages, images, files)
    to clients over the internet.
    It handles requests from clients and responds with the requested resources.

## Child Process

    In computing, a child process is a subprocess created by another process,
    known as the parent process.
    Child processes typically inherit attributes from their parent
    and can perform tasks independently.

## Parent and Child Processes in Web Servers

    Web servers often use a parent-child process model for
    handling client requests efficiently.
    The parent process manages multiple child processes,
    each handling a specific client request.
    This architecture enhances concurrency and performance.

## HTTP Requests

    HTTP (Hypertext Transfer Protocol) defines a set of 
    request methods that clients can use to request resources from a web server.
    Common HTTP requests include GET (retrieve resource),
    POST (submit data),
    PUT (update resource),
    and DELETE (delete resource).

## DNS

    DNS (Domain Name System) is a hierarchical and 
    decentralized naming system that translates 
    human-readable domain names into IP addresses.
    It resolves queries,
    allowing users to access websites using domain names rather than IP addresses.

## DNS Stands For

    DNS stands for Domain Name System.

## DNS Main Role

    The main role of DNS is to translate user-friendly domain names
    (e.g., www.example.com)
    into IP addresses,
    enabling the routing of network traffic on the internet.

## DNS Record Types

### A Record

       An A record (Address Record) maps a domain 
       name to the corresponding IPv4 address.

### CNAME Record

       A CNAME record (Canonical Name) alias allows a domain 
       to be an alias for another domain.
       It is often used for subdomains or domain redirection.

### TXT Record

       A TXT record (Text Record) contains text information,
       commonly used for domain verification or to provide
       additional information about a domain.

### MX Record

       An MX record (Mail Exchange) specifies the mail servers
       responsible for receiving email on behalf of the domain.



[^](#web-server)


