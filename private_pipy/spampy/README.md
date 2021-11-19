# Spam 
### A simple project to become familiar with developing a python cli project.

#### Link To Google Presentation
https://docs.google.com/presentation/d/1RZWrIIF8D4DH5Dl_eWHXbjCoqHklsM-9EovS5XdSr8I/edit#slide=id.g6243d2033c_1_0

## Getting started
After cloning this repo, create the python virtual environment (venv)
```shell
make py-init
```
you should now have a directory called `venv` in the root of your project. This is the installation of python which we are going to use. 
To find out more about python virtual environments, check here

https://docs.python.org/3.6/tutorial/venv.html

We must now activate our ```venv```
```shell
source venv/bin/activate
```

You should now see a ``(venv)`` at the far left of your terminal prompt.


### Makefile
This file is used for automation and general management of your project. It is a simple example, but like anything makefiles can get quite complex and 
can be a very powerful tool. To learn more check out this tutorial

https://opensource.com/article/18/8/what-how-makefile

Run this command to install the ```spam``` application in development mode. The command run is
```pip install -e .``` where the `-e` flag creates a link in the `venv` to your project. Any changes
to the code in the `/spam` directory will be available to run immediately. This option is the best when developing an
application as you do not need to rebuild / install your code all the time to run it.
```shell
make install
```

This will install the `spam` application in your local python venv. After running this command, you should now be able to run
```shell
spam --help
```
This will show you a list of available commands.

## Entry Points
All entry points for the cli can be found in the ``spam/cli`` directory.
The main entry point for the cli can be found in ``__main__.py`` 

### How is spam now available on my terminal?
checkout the make file for the snippet run in the section named `install`. You can check out more about pip and its features here.

https://realpython.com/what-is-pip/


# Further Reading

This is an excellent resource regarding python in general and is 100% free, and is probably the best python resource on the web.
https://realpython.com/

A great guide on packaging your python project
https://packaging.python.org/

Python zip app - How to make a single python executable zip file
https://python.astrotech.io/stdlib/modules/zipapp.html

Make your cli zip app available globally on your system using a symlink (check out the linking commands in the makefile)
https://www.howtogeek.com/297721/how-to-create-and-use-symbolic-links-aka-symlinks-on-a-mac/

Deepen you knowledge about the terminal search path. This is vital to distributing and running your python cli!
https://medium.com/@jalendport/what-exactly-is-your-shell-path-2f076f02deb4
