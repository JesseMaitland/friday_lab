## What is a venv?
A python virtual environment is used to isolate your instance of python, from the system python which is required by your OS. 
As python does not have proper dependency management, installing packages on your system python could break things in a bad way. 
We use a venv to help mitigate this problem.

## The PATH Environment Variable

This is how your terminal knows where to look for code to execute. When you enter a command, 
this path is searched for a file which matches that command, and if found, will be executed. 

## The makefile
A makefile is used to automate the management of your project. It was originally used by c compilers to specify the order
in which things needed to be compiled amongst other things. Today we use it to store snippets which are handy for our project

## Python Terminology
What is the difference between a module and a package? What are objects in python, and how are they treated. 

## The __init__.py file and the __main__.py files
Why do we need these files and what are they used for? 
Anti-patterns to avoid with __init__.py

## The setup.py File
How does python / pip know how to install and run my code?
Here we will take a look at the makefile and explore some commands. 
listing console scripts / entry points

## Everything Is an Object
In python absolutely everything that your code can interact with is an object.... like literally everything. 

## Python's type system
Duck typing. If it walks like a duck, and quacks like a duck, then it must be a duck and therefore should behave like a duck.
However, it is nice to have some type hints.

## Operator Overloading
Let's talk about dunder / magic methods and remove the python wizardry. No more mystery surrounding what __init__, or __name__ mean.
No more strange "airflow syntax". Let's talk about how this actually works under the hood.

## Decorators
lets cover this
