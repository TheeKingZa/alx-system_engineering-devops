# Loops, Conditions and Parsing.
[<](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x03-shell_variables_expansions/README.md) 0x04 [>](https://github.com/TheeKingZa/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/README.md)
----

Need To Know
-------------

* How to create SSH keys?
* What is the advantage of using #!/usr/bin/env bash over #!/bin/bash ?
* How to use while, until and for loops?
* How to use if, else, elif and case condition statements?
* How to use the cut command?
* What are files and other comparison operators, and how to use them?

----------------------------------------------------

* How to Create SSH Keys
----------------------------------------------------
To create SSH keys, follow these steps:
----------------------------------------------------

1.
Open your Terminal.

2.
Use the 'ssh-keygen' command to generate a new SSH key pair. For example:

bash
==Code==
ssh-keygen -t rsa -b 4096 -C "your_email@exmple.com"

3.  You'll be prompted to choose a location to save the key. The default location is usually fine. Press Enter to continue.

4. You can optionally set a passphrase for extra security. Enter a passphrase(or leave it empty for no passphrase) and press Enter.

5. Your SSH key pair will be generated, consisting of a private key(usually 'id_rsa') and a public key(usaually 'id_rsa.pub').

6.
You can now use your SSH key for authentication when connecting to remote servers. Copy the contents of your public key('id_rsa.pub') and add it to the '~/.ssh/authorized_keys' file on the server you want to access.

----------------------------------------------------

* Advantage of 
    #!/usr/bin/env
* bash over 
    #!/bin/bash
----------------------------------------------------

Using #!/usr/bin/env bash as the shebang line in a Bash script has the advantage of being more portable. It allows your script to locate the Bash interpreter in the system's PATH. This means that even if Bash is installed in a different directory on various systems, the script will still work without modification.
----------------------------------------------------

On the other hand, #!/bin/bash assumes that Bash is located at a specific path (/bin/bash), which may not be the case on all systems. Using #!/usr/bin/env bash ensures that the script works regardless of the actual location of the Bash executable.

----------------------------------------------

* How to Use Loops
----------------------------------------------------

while Loop
----------------------------------------------------

   while [condition]; do
        # Code to execute while the condition is true
    done

----

Until Loop
----------------------------------------------------

    until []; do
        # Code to execute until the condiction becomes true
    done

----

For Loop(Iterating over a range)
----------------------------------------------------

    for variable in {start.. end}; do 
        # Code to exe for each iteration.
    done
----

* How to use Conditional Statements
----------------------------------------------------

if Statement
    if [condition]; then
        # Code to exe if condition is true.
    done

----

Else-if(elif) Statement
----------------------------------------------------
    if [condition1]; then
        # Code if condition is to be true
    elif [ condition2 ]; then
        # Condition if its true.
    else
        # Code to execute if none are true.
    fi
-----

Case Statement
----------------------------------------------------

    case  in 
        patten1)
            # Code to execute if  macthes pattern1
            ;;
        pattern2)
            # Code to execute if .. matches pattern2
            ;;
        *)
            # Code to execute if no patterns match
            ;;
    esac

------

How to Use the Cut Command.
----------------------------------------------------

The cut command is used to extract sections from lines of files. Here's a basic usage example:

bash
==Code==

cut -d delimiter -f fields filename
-----

* '-d': Specifies the delimiter character that separates fields.
* '-f': Specifies the field(s) to extract.
* 'filename': The name of the file to process.

EXAMPLE:

echo "John,Doe,30" | cut -d ',' -f 1,2

OUTPUT:
'John, Doe'

as it extraxts the first and second fields separated by a comma

-----------------

* File Comparison Operators
----------------------------------------------------
In Bash scripting, you can use various comparison operators to compare files:

-e filename: True if filename exists.
-f filename: True if filename is a regular file.
-d filename: True if filename is a directory.
-s filename: True if filename is not empty.
file1 -nt file2: True if file1 is newer than file2.
file1 -ot file2: True if file1 is older than file2.
---------------------
Example:
--------

bash
==Code==

    if [ -e file.txt ]; then
        echo "file.txt exists."
    fi
------------------------

env (Environment):
------------------------
env:
* env is a command in Unix-like operating systems that allows you to set or display environment variables.
* Environment variables are key-value pairs that store information used by processes and applications.
      They provide configuration and runtime data.
* env is often used to run a command in a modified environment by setting specific variables or displaying
      the current environment.

cut:
* cut is a command-line utility in Unix-like operating systems used to extract specific sections (columns)
      from lines of text.
* It is often used when dealing with text data that is structured in columns or fields, separated by a
      delimiter like tabs or spaces.
* cut allows you to specify which columns to extract and can be combined with other commands to process and
      manipulate text data.

for:
* for is a control flow statement in Bash and other programming languages that allows you to create loops.
* It is used to repeatedly execute a set of commands a specific number of times or for each item in a list
      (e.g., files in a directory).
* A typical for loop consists of an initialization, a condition, and an increment statement.

while:
* while is another control flow statement in Bash and many other programming languages.
* It creates a loop that continues to execute a block of code as long as a specified condition is true.
* while loops are used when you want to repeat a set of commands until a particular condition is no longer met.

until:
* until is similar to while in that it creates a loop in Bash and other languages.
* However, it works in the opposite way. It continues to execute a block of code as long as a specified
      condition is false.
* until loops are used when you want to repeat a set of commands until a specific condition becomes true.

if:
* if is a conditional statement used in Bash and many other programming languages.
* It allows you to test a condition and execute different sets of commands based on whether the condition is
      true or false.
* if statements are fundamental for creating branching logic in scripts and programs, enabling different
      actions to be taken based on specific conditions.

==============================================================================




