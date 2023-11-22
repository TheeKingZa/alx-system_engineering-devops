# Shell, Variables and Expansions
[<](https://github.com/TheeKingZa/alx-system_engineering-devops/blob/master/0x02-shell_redirections/README.md) 0x03 [>](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x04-loops_conditions_and_parsing/README.md)
----


In this README, we'll explore some common shell commands and concepts used in Unix-like operating systems, such as Linux. These commands are fundamental to managing your environment and working effectively in the shell.
---------------------------------------------------------------------------------------------
NEED TO KNOW?!
----------------------------------------CONTENT----------------------------------------------
* General
    What happens when you type $ ls -l *.txt

* Shell Initialization Files
    What are the /etc/profile file and the /etc/profile.d directory
    What is the ~/.bashrc file

* Variables
    What is the difference between a local and a global variable
    What is a reserved variable
    How to create, update and delete shell variables
    What are the roles of the following reserved variables: HOME, PATH, PS1
    What are special parameters
    What is the special parameter $??

* Expansions
    What is expansion and how to use them
    What is the difference between single and double quotes and how to use them properly
    How to do command substitution with $() and backticks
* Shell Arithmetic
    How to perform arithmetic operations with the shell
    The alias Command

* How to create an alias
    How to list aliases
    How to temporarily disable an alias
* ..Other help pages
      How to execute commands from a file in the current shell

------------------------------------------START---------------------------------------------------

1. What happens when you type $ ls -l *.txt?
When you type ls -l *.txt in the shell, you are instructing it to list the files in the current directory with the ".txt" file extension in long format. The shell processes the command as follows:

ls is the command to list files.
-l is an option (or flag) that tells ls to display the files in long format, which includes details like permissions, owner, size, and modification date.
*.txt is a shell wildcard pattern that matches all files with the ".txt" extension in the current directory.
The shell expands *.txt to the list of matching filenames before passing them as arguments to the ls command.
2. Shell Initialization Files:
Shell initialization files are scripts that are executed when a shell starts. They are used to set up the environment and configure the shell according to the user's preferences. Common initialization files include .bashrc, .bash_profile, and .profile for the Bash shell.

3. /etc/profile and /etc/profile.d:
/etc/profile: This is a system-wide shell initialization file. It is executed when any user logs in and sets up system-wide environment variables.
/etc/profile.d: This directory contains additional shell initialization scripts that can be executed during login. It allows administrators to add custom configurations for various applications and services.
4. ~/.bashrc:
The ~/.bashrc file is a user-specific shell initialization file for the Bash shell. It is executed when a user starts an interactive Bash session. Users can customize their environment by adding aliases, setting variables, and configuring their shell prompt in this file.

5. Variables:
Variables in shell scripting are used to store data. They can be categorized into local and global variables.

6. Difference Between Local and Global Variables:
Local Variables: Local variables are defined and used within a specific scope, such as within a function or script. They are not visible or accessible outside that scope.
Global Variables: Global variables are accessible from any part of the script or shell session. They are usually defined at the top level of a script or in shell initialization files.
7. Reserved Variables:
Reserved variables are predefined by the shell and have special meanings. Some examples include:

$HOME: Represents the user's home directory.
$PATH: Specifies a colon-separated list of directories where the shell looks for executable files.
$PS1: Defines the primary prompt string displayed in the shell.
8. Creating, Updating, and Deleting Shell Variables:
Creating Variables: You can create a variable by assigning a value to it. For example, myvar="Hello".
Updating Variables: To update the value of an existing variable, simply reassign it.
Deleting Variables: Use the unset command to delete a variable, e.g., unset myvar.
9. Special Parameters:
Special parameters are variables with predefined meanings in shell scripting. They include:

$#: Number of command-line arguments.
$* and $@: All command-line arguments as a single string or an array, respectively.
$?: Exit status of the last executed command.
10. $?? (Double Question Mark):
The $?? is not a standard special parameter in shell scripting. It appears to be a typo or incorrect usage. If you meant to refer to the exit status of the last command, you should use $?.

For example:

Bash
==Code==

$ ls non_existent_file.txt
$ echo $?
2

--
In this example, '$?' contains the exit status of the 'ls' command, which is 2(indicating an error).
---------------------------------------------------------------------------------------------  

1. Expansions:
Expansions are a fundamental concept in shell scripting. They allow you to replace patterns or placeholders with their actual values. Common types of expansions include variable expansion, command substitution, and arithmetic expansion.

2. Single vs. Double Quotes:
Single Quotes (''): Enclosed text is treated as literal, and no expansions occur. Use single quotes when you want to preserve the exact text.
Double Quotes (""): Enclosed text allows variable expansion and command substitution. Use double quotes when you want to allow substitutions and expand variables.
Example:

bash
==Code==
name="John"
echo 'Hello, $name!'  # Output: Hello, $name!
echo "Hello, $name!"  # Output: Hello, John!
---------------------------------------------------------------------------------------------

3. Command Substitution:
Command substitution allows you to execute a command within a shell command and capture its output.

Using $(): Preferred method for command substitution.
Using Backticks (``): An older method that achieves the same result.
Example with $():

bash
==Code==
current_date=$(date +%Y-%m-%d)
echo "Today is $current_date"

---------------------------------------------------------------------------------------------
4. Shell Arithmetic:
You can perform arithmetic operations within the shell using $((...)). Supported operators include +, -, *, /, %, etc.

Example:

bash
==Code==
result=$((5 + 3))
echo "5 + 3 equals $result"
---------------------------------------------------------------------------------------------

5. The alias Command:
Aliases allow you to create shortcuts or alternate names for commands.

*Creating an Alias:
    Use the alias command followed by the alias name and the command to be aliased.
*Listing Aliases:
    Simply type alias without arguments to list all defined aliases.
*Temporarily Disabling an Alias:
    Prefix the command with a backslash () to temporarily disable an alias for a single command execution.

Example:

bash
==Code==
alias ll='ls -l'
alias   # List all aliases

\ll     # Temporarily disable the 'll' alias for this command

---------------------------------------------------------------------------------------------

6. Executing Commands from a File in the Current Shell:
To execute commands from a file in the current shell session, use the source or . (dot) command followed by the filename.

* source filename or . filename
Example:

bash
==Code==
source myscript.sh
. myscript.sh

--

This executes the commands in myscript.sh in the current shell, allowing them to modify the current environment.

----------------------------------------------------------------------------------------------------

These concepts and commands are essential for effective shell scripting and customization. Understanding how to use expansions, quotes, command substitution, arithmetic, aliases, and command execution are key skills for working with the shell.

----------------------------------------------END-----------------------------------------------
