# Building a Three-Server Distributed Web Infrastructure

In this document, we will explore a more robust web infrastructure designed to host the website www.foobar.com. This infrastructure includes two servers, a web server, an application server, a load balancer (HAproxy), a set of application files, and a database (MySQL).

----
[Diagram](0-simple_web_stack.jpg)|-----------+
----


## Infrastructure Components

### 1. Servers

   - Two servers are employed to distribute the load and ensure redundancy. This is in contrast to the single-server infrastructure, which helps address the SPOF issue.
   
### 2. Web Server (Nginx)

   - The web server (Nginx) continues to serve as the gateway for incoming web requests, just like in the previous infrastructure.

### 3. Application Server

   - The application server hosts the codebase and processes user requests, similar to the previous setup.

### 4. Load Balancer (HAproxy)

   - The load balancer, HAproxy, is introduced to distribute incoming requests across multiple servers. It enhances performance and availability.

   - The load balancer is configured with a distribution algorithm, such as round-robin or least connections, to determine how incoming requests are distributed among servers. This algorithm ensures fair load distribution.

   - The load balancer enables an Active-Active setup, where all servers actively handle requests. Active-Passive would mean that one server is actively serving requests, and the others act as backups.

### 5. Set of Application Files

   - These application files are the codebase of your web application and are hosted on the application server.

### 6. Database (MySQL)

   - The database (MySQL) stores and manages data for the web application, just as in the previous infrastructure.

### 7. Database Primary-Replica Cluster

   - The database is configured as a Primary-Replica (Master-Slave) cluster to enhance data redundancy and fault tolerance. In this setup, the Primary node actively handles write operations, and the Replica node replicates data and can serve read requests.

   - The Primary node is responsible for write operations (insert, update, delete), while the Replica node provides read-only access. This setup enhances data integrity and load distribution.

## Issues with the Infrastructure

1. Single Point of Failure (SPOF)

   - Although the SPOF issue is mitigated to some extent by having multiple servers, each component in the infrastructure can still be a potential SPOF if not properly redundant.

2. Security Issues

   - The infrastructure lacks essential security measures, such as a firewall and HTTPS encryption, making it vulnerable to attacks and data breaches.

3. No Monitoring

   - Without a monitoring system in place, it's challenging to detect and respond to performance issues, downtime, or security breaches in real-time.

In summary, this three-server distributed web infrastructure improves redundancy, load distribution, and fault tolerance. However, it still faces issues related to potential SPOFs, security vulnerabilities, and the absence of a monitoring system. Addressing these concerns is crucial to ensure the reliability and security of the infrastructure.




------
[Back](0-simple_web_stack.md)
------
[Next](2-secured_and_monitored_web_infrastructure.md)
