# Understanding a Simple Web Infrastructure
--
In this document, we will explore the components and specifics of a simple web infrastructure, including its roles and potential issues. This infrastructure typically consists of a single server with a LAMP (Linux, Apache, MySQL, PHP/Python/Perl) stack.

## Infrastructure Components

### 1. [Server](README.md#server)

A server is a physical or virtual machine that hosts the web application. It is the central component responsible for processing and responding to user requests.

### 2. Domain Name

The domain name, such as "foobar.com," serves as the human-readable address for the website. It provides a way for users to access your site. In this infrastructure, the domain name must be configured with a www record pointing to your server's IP address (e.g., 8.8.8.8).

### 3. DNS Record - www

The "www" in "www.foobar.com" is a subdomain and a DNS record. It typically points to the same IP address as the root domain and directs users to the web server.

### 4. Web Server (Nginx)

The web server, in this case, Nginx, is responsible for handling incoming web requests. It listens for incoming requests, processes them, and serves web content to users. It acts as a gateway between the user's browser and the application server.

### 5. Application Server

The application server hosts the codebase of your web application, such as PHP, Python, or Perl scripts. It processes user requests, executes code, and interacts with the database to generate dynamic web content.

### 6. Database (MySQL)

The database stores and manages data used by the web application. It allows for data retrieval, storage, and manipulation. In this infrastructure, MySQL is the chosen database system.

### 7. User Communication

The web server and application server communicate with the user's computer over HTTP or HTTPS protocols. The user's browser sends requests to the web server, which forwards dynamic requests to the application server for processing. The response is then sent back to the user's browser.

## Issues with the Infrastructure

1. Single Point of Failure (SPOF)

   The entire infrastructure relies on a single server. If it experiences hardware failure or other issues, the entire website may become unavailable.

2. Downtime during Maintenance

   When performing maintenance tasks, such as deploying new code or updates, the web server often needs to be restarted. This can result in temporary downtime and affect user accessibility.

3. Scalability Challenges

   This infrastructure may struggle to handle a significant increase in incoming traffic. Adding more servers or load balancing mechanisms becomes essential for scalability.

## Conclusion

This simple web infrastructure consists of essential components like the server, web server, application server, and database. The domain name plays a vital role in providing an accessible web address. However, it faces challenges such as SPOF, downtime during maintenance, and scalability issues.

Understanding these components and their roles is crucial for building reliable web applications and addressing potential problems in the infrastructure.



------
[Next](1-distributed_web_infrastructure.md)
------
