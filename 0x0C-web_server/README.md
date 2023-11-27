# Web Server
[<](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x0B-ssh/README.md) 0x0C [>](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x0D-web_stack_debugging_0/README.md)
---

Concepts
For this project, we expect you to look at this concept:

* [What is a Child Process?](#what-is-a-child-process)

# NEED TO KNOW?
  *


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

# What is a child process?

Although it may sound like something out of a parenting handbook or a psychological journal, the term child process actually has nothing to do with human development. If you run a Unix or Linux dedicated server, you have likely encountered child processes without even knowing it. Therefore, it is good to know what child processes are and how they work.

A child process is a process created by another process. The creator process is properly called the “parent process”. The benefit of a child process is that it can start or stop at will without affecting the parent process. The child process is, however, is typically dependent on the parent process. If the parent process dies, the child process becomes an orphan process.

In normal server operations, the kernel may initiate child processes, and other programs, such as Apache, may have them as well. Apache creates child processes (or children, if you prefer) whenever the number of requests (web page accesses from users) exceeds the maximum allowed number of requests. When the maximum number of child process requests is exceeded, another child process spawns.

To view all running processes along with their child processes in a “tree” format, use the following command:

    $ ps axf

For more information about child processes, see this [documentation](https://www.gnu.org/software/libc/manual/html_node/Processes.html#Processes).


[^](#web-server)
