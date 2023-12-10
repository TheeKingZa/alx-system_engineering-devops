# Load balancer
[<](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x0D-web_stack_debugging_1/README.md) 0x0F [#](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master)
---

[web server project](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x0C-web_server/README.md)
---
# Concepts
For this project, we expect you to look at these concepts:

* [Load balancer](#load-balancer)
* [Web stack debugging](#web-stack-debugging)

# Background Context
You have been given 2 additional servers:
---
gc-[STUDENT_ID]-web-02-XXXXXXXXXX
---
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
---

Let’s improve our web stack so that there is [redundancy](https://en.wikipedia.org/wiki/Redundancy_%28engineering%29) for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

# NEED TO KNOW?
* [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
* [HTTP header](https://www.techopedia.com/definition/27178/http-header)
* [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)



# Load balancer
    Ever wonder how Facebook, Linkedin, Twitter and other web giants are handling such huge amounts of traffic?
    They don’t have just one server, but tens of thousands of them.
    In order to achieve this, web traffic needs to be distributed to these servers,
    and that is the role of a load-balancer.

readme
* [Load Balancer](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
* [Load Balancer Algorithms](https://community.f5.com/t5/technical-articles/intro-to-load-balancing-for-developers-the-algorithms/ta-p/273759)

# Web stack debugging
Intro
Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.

[img_here]

# Non-exhaustive guide to debugging

# School specific
    If you are struggling to get something right that is run on the checker,
    like a Bash script or a piece of code,
    keep in mind that you can simulate the flow by starting
    a Docker container with the distribution that is specified in the
    requirements and by running your code.
  * Check the [Docker concept page](https://www.section.io/engineering-education/docker-concepts/) for more info.

# Test and verify your assumptions
    The idea is to ask a set of questions until you find the issue.
    For example,
    if you installed a web server and
    it isn’t serving a page when browsing the IP,
    here are some questions you can ask yourself to start debugging:

    * Is the web server started?
      - You can check using the service manager,
        also double check by checking process list.
    
    * On what port should it listen?
      - Check your web server configuration
    
    * Is it actually listening on this port?
      - netstat -lpdn - run as root 
      or
      - sudo so that you can see the process for each listening port
    
    * It is listening on the correct server IP?
      - netstat is also your friend here
    
    * Is there a firewall enabled?
    
    * Have you looked at logs?
      - usually in /var/log
      and
      - tail -f is your friend
    
    * Can I connect to the HTTP port from the location I am browsing from?
      - curl is your friend

There is a good chance that at this point you will already have found part of the issue.

# Get a quick overview of the machine state
Youtube video First [5 Commands](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/) [When I Connect on a Linux Server](https://www.youtube.com/watch?v=1_gqlbADaAw) or [basic Newtork commands](https://www.youtube.com/watch?v=rurs7cdT5cc)

    When you connect to a server/machine/computer/container
    you want to understand what’s happened recently
    and what’s happening now,
    and you can do this with 5 commands in a minute or less:

[^](#need-to-know)

# w
  * shows server [uptime](https://www.techtarget.com/whatis/definition/uptime-and-downtime) which is the time during which the server has been continuously running
  * shows which users are connected to the server
  * load average will give you a good sense of the server health
      - (read more about load [here](https://scoutapm.com/blog/understanding-load-averages) and [here](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html))

# [history](https://man.freebsd.org/cgi/man.cgi?query=history&apropos=0&sektion=1&manpath=FreeBSD+14.0-RELEASE+and+Ports&arch=default&format=html)
  * shows which commands were previously run by the user you are currently connected to
  * you can learn a lot about what type of work was previously
    performed on the machine,
    and what could have gone wrong with it
  * where you might want to start your debugging work

# [top](https://man.freebsd.org/cgi/man.cgi?query=top&apropos=0&sektion=1&manpath=FreeBSD+14.0-RELEASE+and+Ports&arch=default&format=html)
  * shows what is currently running on this server
  * order results by CPU,
    memory utilization
    and catch the ones that are resource intensive

# [df](https://man.freebsd.org/cgi/man.cgi?query=df&apropos=0&sektion=1&manpath=FreeBSD+14.0-RELEASE+and+Ports&arch=default&format=html)
  * shows disk utilization

# [netstat](https://man.freebsd.org/cgi/man.cgi?netstat(1))
  * what port and IP your server is listening on
  * what processes are using sockets
  * try netstat -lpn on a Ubuntu machine

[^](#need-to-know)

# Machine
    Debugging is pretty much about verifying assumptions,
    in a perfect world the software
    or
    system we are working on would be working perfectly,
    the server is in perfect shape and everybody is happy.
    But actually,
    it NEVER goes this way,
    things ALWAYS fail (it’s tremendous!).

For the machine level, you want to ask yourself these questions:
  * Does the server have free disk space? - [df](#df)
Is the server able to keep up with CPU load? - [w](#w), [top](#top), [ps](https://man7.org/linux/man-pages/man1/ps.1.html)
Does the server have available memory? [free](https://man7.org/linux/man-pages/man1/free.1.html)
Are the server disk(s) able to keep up with read/write IO? - [htop](https://linux.die.net/man/1/htop)

If the answer is no for any of these questions,
then that might be the reason why things are not going as expected.
There are often 3 ways of solving the issue:

  * free up resources (stop process(es)
   or
    reduce their resource consumption)
  * increase the machine resources
    - (adding memory, CPU, disk space…)
  * distributing the resource usage to other machines

[^](#need-to-know)

# Network issue
  For the machine level, you want to ask yourself these questions:
    * Does the server have the expected
    network interfaces and IPs up and running?
      [ifconfig](https://linux.die.net/man/8/ifconfig)
    * Does the server listen on the sockets that it is supposed to? [netstat](https://man.freebsd.org/cgi/man.cgi?netstat(1))([netstat -lpd or netstat -lpn](https://www.lifewire.com/netstat-command-2618098))
    * Can you connect from the location you want to connect from,
      to the socket you want to connect to?
      [telnet](https://support.intermedia.com/app/articles/detail/a_id/25172/~/what-is-telnet%3F-how-do-i-run-it%3F) to the IP + PORT ([telnet 8.8.8.8 80](https://www.youtube.com/watch?v=jA66Jx4bzYU))
    * Does the server have the correct firewall rules? iptables, ufw:
      * [iptables -L](https://linux.die.net/man/8/iptables-save)
      * [sudo ufw status](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04)

[^](#need-to-know)

# Process issue
    If a piece of Software isn’t behaving as expected,
    it can obviously be because of above reasons…
    but the good news is that there is more to look into
    (there is ALWAYS more to look into actually).

  * Is the software started? init, init.d:
    * [service NAME_OF_THE_SERVICE status](https://stackoverflow.com/questions/57964952/how-to-get-the-name-of-the-service-it-is-in-order-to-log-status-on-sql-server)
    * [/etc/init.d/NAME_OF_THE_SERVICE status](https://www.baeldung.com/linux/initialization-managers-service-status)

  * Is the software process running? pgrep, ps:
    * [pgrep -lf NAME_OF_THE_PROCESS](https://stackoverflow.com/questions/38341366/how-to-specify-commandline-arguments-in-pgrep-in-bash)
    * [ps auxf](https://www.linode.com/docs/guides/use-the-ps-aux-command-in-linux/)
  
  * Is there anything interesting in the logs?
    look for log files in [/var/log/](https://www.netsurion.com/articles/top-5-linux-log-file-groups-in-var-log)
    and
    [tail -f](https://www.webmastercampus.com/linux-tail-command/) is your friend

[^](#need-to-know)

# Debugging is fun
    Debugging can be frustrating,
    but it will definitely be part of your job,
    it requires experience and methodology to become good at it.
    The good news is that bugs are never going away,
    and the more experienced you become,
    trickier bugs will be assigned to you! Good luck :)
---

[^](#need-to-know)

