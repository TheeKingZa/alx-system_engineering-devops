# Firewall
[<](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter/README.md) 0x13 [>](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/attack_is_the_best_defense/README.md)
---

# Concepts
        For this project, we expect you to look at this concept:

* [Web stack debugging]()


# NEED TO KNOW?
* [What is a firewall]()

More Info
As explained in the web stack debugging guide concept page, telnet is a very good tool to check if sockets are open with telnet IP PORT. For example, if you want to check if port 22 is open on web-02:


We can see for this example that the connection is successful: Connected to web-02.holberton.online.

Now let’s try connecting to port 2222:


    We can see that the connection never succeeds, so after some time I just use ctrl+c to kill the process.

    This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

    Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on web-01, please perform the test from outside of the school network, like from your web-02 server. If you SSH into your web-02 server, the traffic will be originating from web-02 and not from the school’s network, bypassing the firewall.

# Warning!
    Containers on demand cannot be used for this project (Docker container limitation)

    Be very careful with firewall rules! For instance, if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.
