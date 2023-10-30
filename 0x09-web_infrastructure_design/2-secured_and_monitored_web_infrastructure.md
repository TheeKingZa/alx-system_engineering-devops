# Building a Secured and Monitored Three-Server Web Infrastructure

In this document, we will design a robust and secure web infrastructure that hosts the website www.foobar.com. This infrastructure comprises three servers, firewalls, SSL certificate, and monitoring clients.

## Infrastructure Components

### 1. Servers

   - We use three servers with identical components to enhance redundancy and ensure the availability of the website.

### 2. Firewalls

   - Three firewalls are added for enhanced security. Firewalls act as a barrier between the servers and the internet, controlling incoming and outgoing traffic based on predefined security rules.

### 3. SSL Certificate

   - An SSL certificate is employed to serve the website over HTTPS. This certificate ensures data encryption and secure communication between the user's browser and the web server.

### 4. Monitoring Clients

   - Three monitoring clients are included to collect and send data to a monitoring service like Sumo Logic. Monitoring tools help track the performance, security, and availability of the infrastructure.

## Specifics About the Infrastructure

- Firewalls are added to enhance security by filtering and controlling network traffic. They help protect the servers from unauthorized access and potential threats.

- Serving traffic over HTTPS using an SSL certificate ensures data encryption, privacy, and security. It's essential for securing sensitive data and maintaining user trust.

- Monitoring tools are used to track the health, performance, and security of the infrastructure. They collect data from various components, allowing administrators to proactively identify issues and take necessary actions.

- Monitoring clients are responsible for collecting data about server performance, security, and availability and sending it to a monitoring service like Sumo Logic.

- To monitor web server Queries Per Second (QPS), you need to configure the monitoring tool to track and log web server metrics. The tool will collect data on request rates and response times to calculate QPS.

## Issues with the Infrastructure

1. Terminating SSL at the Load Balancer Level

   - Terminating SSL at the load balancer can be an issue because it means that SSL decryption and encryption take place at the load balancer. This adds processing load and may be a security risk if not properly configured.

2. Only One MySQL Server Accepting Writes

   - Relying on a single MySQL server for write operations is risky. If it experiences downtime or failures, it can lead to data loss and reduced availability. Implementing a Primary-Replica (Master-Slave) setup is advisable.

3. Servers with Identical Components

   - Having servers with identical components can be problematic if a specific component fails. It's important to have redundancy and failover mechanisms to maintain continuous service.

In summary, this secure and monitored infrastructure enhances security, performance, and availability. However, it still faces potential issues related to SSL termination, database redundancy, and the need for failover mechanisms in case of component failure.




------
[Back](2-secured_and_monitored_web_infrastructure.md)
------
[Next](3-scale_up.md)
