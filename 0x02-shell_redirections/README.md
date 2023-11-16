# Shell, Directions and Filters
[<]() 0x02 [>]()
----

    In this README, we will explore several important shell commands frequently used in Unix-like operating systems. Each command serves a distinct purpose and is crucial for various tasks.

# echo
    Description: The echo command is used to display text or variables on the terminal.

    Usage:

    bashCode
        echo "Hello, world!"

[Manual Page](https://man7.org/linux/man-pages/man1/echo.1.html)

[^](#shell-directions-and-filters)

---
# cat
    Description: The cat command is used to concatenate and display the content of files.

    Usage:

    bashCode==
        cat file.txt

[Manual Page](https://man7.org/linux/man-pages/man1/cat.1.html)

[^](#shell-directions-and-filters)

---
# head
    Description: The head command displays the beginning lines of a file.

    Usage:

    bashCode
        head -n 5 file.txt
[Manual Page](https://man7.org/linux/man-pages/man1/head.1.html)

[^](#shell-directions-and-filters)

---
# tail
    Description: The tail command displays the end lines of a file.

    Usage:

    bashCode
        tail -n 10 file.txt
        
[Manual Page](https://man7.org/linux/man-pages/man1/tail.1.html)

[^](#shell-directions-and-filters)

---

# find
    Description: The find command is used to search for files and directories based on specified criteria.

    Usage:

    bashCode
        find /path/to/search -name "*.txt"
        
[Manual Page](https://man7.org/linux/man-pages/man1/find.1.html)

[^](#shell-directions-and-filters)

---

# wc
    Description: The wc command counts lines, words, and characters in a file.

    Usage:

    bashCode
        wc -l file.txt

[Manual Page](https://man7.org/linux/man-pages/man1/wc.1.html)

[^](#shell-directions-and-filters)

---

# sort
    Description: The sort command is used to sort lines of text files.

    Usage:

    bashCode
        sort file.txt

[Manual Page](https://man7.org/linux/man-pages/man1/sort.1.html)

[^](#shell-directions-and-filters)

---

# uniq
    Description: The uniq command removes duplicate lines from a sorted file.

    Usage:

    bashCode
        sort file.txt | uniq
[Manual Page](https://man7.org/linux/man-pages/man1/uniq.1.html)

[^](#shell-directions-and-filters)

---

# grep
    Description: The grep command searches text using patterns and regular expressions.

    Usage:

    bashCode
        grep "pattern" file.txt
[Manual Page](https://man7.org/linux/man-pages/man1/grep.1.html)

[^](#shell-directions-and-filters)

---

# tr
    Description: The tr command is used for character-level translation or deletion.

    Usage:

    bashCode
        echo "Hello" | tr 'a-z' 'A-Z'
[Manual Page](https://man7.org/linux/man-pages/man1/tr.1.html)

[^](#shell-directions-and-filters)

---

# rev
    Description: The rev command reverses lines character-wise.

    Usage:

    bashCode
        echo "Hello" | rev
[Manual Page](https://man7.org/linux/man-pages/man1/rev.1.html)

[^](#shell-directions-and-filters)

---

# cut
    Description: The cut command is used to remove sections from lines of files.

    Usage:

    bashCode
        cut -d',' -f2 file.csv

[Manual Page](https://man7.org/linux/man-pages/man1/cut.1.html)

[^](#shell-directions-and-filters)

---

# passwd (5)
    Description:
    The passwd (5) manual page contains information about the file format and conventions of the /etc/passwd file.

    Usage:

    bashCode
        man 5 passwd

[Manual Page](https://man7.org/linux/man-pages/man1/passwd.5.html)

[^](#shell-directions-and-filters)

---
# Shell, I/O Redirection, and Special Characters
    Commands and Their Functions:

        * head: Displays the beginning lines of a file.
        * tail: Displays the end lines of a file.
        * find: Searches for files and directories based on specified criteria.
        * wc: Counts lines, words, and characters in a file.
        * sort: Sorts lines of text files.
        * uniq: Removes duplicate lines from a sorted file.
        * grep: Searches text using patterns and regular expressions.
        * tr: Performs character-level translation or deletion.
        * cat: Concatenates and displays the content of files.

[^](#shell-directions-and-filters)

---
# I/O Redirection:
    *  Redirect Standard Output to a File: Use > to redirect standard output to a file.

        bashCode
            command > output.txt

    *  Get Standard Input from a File: Use < to get standard input from a file.

        bashCode
            command < input.txt

    *  Send Output to Another Program: Use | (pipe) to send the output from one program to the input of another program.

        bashCode
        command1 | command2

    *  Combine Commands and Filters with Redirections: You can combine multiple commands and filters using redirections to create complex data processing pipelines.

[^](#shell-directions-and-filters)

---
# Special Characters:
    * White Spaces
        ("    "):
            Spaces and tabs are used for separating commands and arguments. Quotes can be used to preserve spaces in arguments.

    * Single Quotes
        (''):
            Enclosed text is treated as a literal. No variable or command expansion occurs.

    * Double Quotes
        (""):
            Enclosed text allows variable and command substitution. Expansions occur within double quotes.

    * Backslash
        (\):
            Used to escape special characters, making them literal. For example, \n represents a newline character.

    * Comment
        (#):
            Anything after a # is treated as a comment and is not executed.

    * Pipe
        (|):
            Connects the output of one command to the input of another, enabling data flow between commands.

    * Command Separator
        (;):
            Separates multiple commands on a single line. They are executed sequentially.

    * Tilde
        (~):
            Represents the user's home directory, e.g., ~username refers to the home directory of the specified user.


[^](#shell-directions-and-filters)
