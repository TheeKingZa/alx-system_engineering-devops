# Web stack debugging #3
[<](https://github.com/TheeKingZa/alx-system_engineering-devops/blob/master/0x16-api_advanced/README.md) 0x17 [#](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/README.md)
---

# Concepts
```
For this project, we expect you to look at these concepts:
```
* [Web Server](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x0C-web_server/README.md)
* [Web stack debugging](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x0D-web_stack_debugging_0/README.md)

# Background Context
When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… [It actually powers 26% of the web](https://managewp.com/blog/statistics-about-wordpress-usage), so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.
---

# Install puppet-lint
```
  $ apt-get install -y ruby
  $ gem install puppet-lint -v 2.1.1
```
---

[^](#concepts)

---
