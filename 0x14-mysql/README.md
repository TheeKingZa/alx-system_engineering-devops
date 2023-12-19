# MySql
[<]() 0x14 [#](https://github.com/TheeKingZa/Portfolio)
---

# Concepts
For this project, we expect you to look at these concepts:

* [Database administration](#database-administration)
* [Web stack debugging](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x0D-web_stack_debugging_0/README.md)
* [[How to] Install mysql 5.7](#how-to-install-mysql-57)
---

# NEED TO KNOW
* [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
* [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
* [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)
* [What is the main role of a database](#Main-role-of-a-database)
* [What is a database replica](#database-replica)
* [What is the purpose of a database replica](#purpose-of-a-database-replica)
* [Why database backups need to be stored in different physical locations](#storing-backups-in-different-physical-locations
)
* [What operation should you regularly perform to make sure that your database backup strategy actually works](#regular-operations-for-batabase-backup-strategy
)

man or help:
* [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)

---

# Database administration
* [What is a database](https://www.techtarget.com/searchdatamanagement/definition/database)
* [What is a database primary/replicate cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
* [MySQL primary/replicate setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
* [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)

---


[^](#need-to-know)

# [How to] Install mysql 5.7

```
Copy the key here to your clipboard
```


[https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html](https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html)

```
    Save it in a file on your machine i.e. signature.key and then

        sudo apt-key add signature.key
```

add the apt repo

```
    sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
    update apt

    sudo apt-get update

now check your available versions:

```
vagrant@ubuntu-focal:/vagrant$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.27-0ubuntu0.20.04.1
  Version table:
     8.0.27-0ubuntu0.20.04.1 500
        500 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.37-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages
```
Now install mysql 5.7
```
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
Copyright © 2023 ALX, All rights reserved.

```

[^](#need-to-know)

---

# Main Role of a Database
```
A database is a structured collection of data that facilitates efficient data storage, retrieval, and manipulation. It serves as a reliable and centralized system for managing information. The key roles of a database include:

- **Data Storage:** Storing data in an organized and structured manner.
- **Data Retrieval:** Efficiently retrieving specific data based on user queries.
- **Data Manipulation:** Updating, deleting, and inserting data as needed.
- **Data Integrity:** Ensuring data accuracy and consistency.
```


[^](#need-to-know)

# Database Replica
```
A database replica is a copy of the original database created and maintained to enhance system reliability and performance. Key characteristics of database replicas include:

- **Types of Replicas:** Primary (master) and secondary (slave) replicas.
- **Load Balancing:** Distributing read operations across multiple replicas to improve performance.
- **Fault Tolerance:** Providing redundancy to ensure system availability in case of a primary replica failure.

```

# Purpose of a Database Replica

The primary purposes of having database replicas include:
```
- **High Availability:** Ensuring continuous access to data even in the face of hardware failures or maintenance.
- **Scalability:** Distributing read operations among replicas to handle increasing workloads.
- **Disaster Recovery:** Facilitating quick recovery in case of data center failures or disasters.
```

[^](#need-to-know)

# Storing Backups in Different Physical Locations

Storing database backups in diverse physical locations is crucial for several reasons:
```
- **Disaster Recovery:** Protecting against data loss due to natural disasters, fires, or other catastrophic events.
- **Data Integrity:** Avoiding a single point of failure that could compromise all backups.
- **Regulatory Compliance:** Meeting regulatory requirements for data backup and storage.
```

# Regular Operations for Database Backup Strategy

To ensure the effectiveness of the database backup strategy, regularly perform the following operations:
```
- **Backup Testing:** Periodically restore backups to verify their completeness and integrity.
- **Monitoring:** Monitor backup processes to detect any issues or failures promptly.
- **Documentation:** Maintain comprehensive documentation on the backup strategy and recovery procedures.
```
---

[^](#need-to-know)
