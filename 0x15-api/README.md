# API
[<](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x14-mysql) 0X15 [#](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/README.md)
---
# Resources
Read or watch:

* [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
* [What is an API](https://www.webopedia.com/definitions/api/)
* [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
* [What is a REST API](https://www.sitepoint.com/rest-api/)
* [What are microservices](https://smartbear.com/learn/api-design/microservices/)
* [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://peps.python.org/pep-0008/)

# NEED TO KNOW
* [What Bash scripting should not be used for?](#what-bash-scripting-should-not-be-used-for)
* [What is an API?](#what-is-an-api)
* [What is a REST API?](#what-is-a-rest-api)
* [What are microservices?](#what-are-microservices)
* [What is the CSV format?](#what-is-the-csv-format)
* [What is the JSON format?](#what-is-the-json-format)
* [Pythonic Package and module name style?](#pythonic-package-and-module-name-style)
* [Pythonic Class name style?](#pythonic-class-name-style)
* [Pythonic Variable name style?](#pythonic-variable-name-style)
* [Pythonic Function name style?](#pythonic-function-name-style)
* [Pythonic Constant name style?](#pythonic-constant-name-style)
* [Significance of CapWords or CamelCase in Python?](#significance-of-capwords-or-camelcase-in-python)

---

# What Bash scripting should not be used for
Bash scripting is not suitable for complex and resource-intensive tasks. It lacks the features and performance needed for larger software projects. It's best for simple automation tasks and small utility scripts.
---

[^](#need-to-know)

---
# What is an API
An API, or Application Programming Interface, is a set of rules and protocols that allows one software application to interact with another. It defines how different software components should communicate, enabling the integration of various services and functionalities.
---

[^](#need-to-know)

---
# What is a REST API
REST (Representational State Transfer) API is a type of web API that adheres to the principles of REST. It uses standard HTTP methods (GET, POST, PUT, DELETE) for communication and typically transfers data in JSON format. REST APIs are widely used for web services due to their simplicity and scalability.
---

[^](#need-to-know)

---
# What are microservices
Microservices is an architectural approach where a complex application is built as a set of small, independent services that communicate with each other through APIs. This design allows for better scalability, maintainability, and flexibility compared to monolithic architectures.
---

[^](#need-to-know)

---
# What is the CSV format
CSV (Comma-Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. Each line of the file represents a row, and the values within a row are separated by commas. It's a common format for data exchange between different applications.

```
     Format is used for tabular data. For example, a CSV file might store a list of contacts with columns like "Name," "Email," and "Phone."
```

---

[^](#need-to-know)

---
# What is the JSON format
JSON (JavaScript Object Notation) is a lightweight data interchange format. It uses human-readable text to represent data objects consisting of key-value pairs. JSON is widely used for data exchange between a server and a web application.

```
    An example JSON object could represent a person's information like {"name": "John", "age": 30, "city": "New York"}.
```
---

[^](#need-to-know)

---
# Pythonic Package and module name style
Pythonic package and module names follow the PEP 8 style guide. They are typically lowercase with underscores separating words. For example, a package might be named my_package and a module within that package might be named my_module.

```
    # In a Python package (folder)
    # my_package/__init__.py

    # In a Python module (file)
    # my_package/my_module.py
```
---

[^](#need-to-know)

---
# Pythonic Class name style
Pythonic class names also follow the PEP 8 style guide. They use CapWords (CamelCase) style, where the first letter of each word is capitalized. For example, a class might be named MyClass.
```
    class MyClass:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
```
---

[^](#need-to-know)

---
# Pythonic Variable name style
Pythonic variable names use lowercase with underscores, following the PEP 8 style guide. For example, a variable might be named my_variable.

```
my_variable = 42
```
---

[^](#need-to-know)

---
# Pythonic Function name style
Pythonic function names also use lowercase with underscores, adhering to the PEP 8 style guide. For example, a function might be named my_function.

```
    def my_function(parameter1, parameter2):
        return parameter1 + parameter2
```
---

[^](#need-to-know)

---
# Pythonic Constant name style
Pythonic constant names, like variables, use uppercase with underscores. Constants represent values that should not be changed during the program's execution. For example, a constant might be named MY_CONSTANT.

```
    MY_CONSTANT = 3.14
```
---

[^](#need-to-know)

---
# Significance of CapWords or CamelCase in Python
CapWords or CamelCase is significant in Python, especially for class names, as it helps distinguish them from functions and variables. This naming convention enhances code readability and is widely adopted in the Python community.

```
    class MyExampleClass:
        def __init__(self, value):
            self.value = value

        def display_value(self):
            print(self.value)

    # Create an instance
    example_instance = MyExampleClass("Hello, Python!")

    # Call a method
    example_instance.display_value()

```
---
<div align="center">
<sub>
    These examples demonstrates.
    <hr/>
The use of each concept in both the context
of programming practices
and Python coding styles..</sub>
</div>

---

[^](#need-to-know)

---
