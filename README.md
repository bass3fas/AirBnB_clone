# 0x00. AirBnB clone - The console

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)



### Introduction

#### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

### Installation

git clone https://github.com/bass3fas/AirBnB_clone.git
change to the AirBnb directory and run the command:
```
 ./console.py
```

### Usage

#### Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Testing

All the test are defined in the tests folder.

Documentation
Modules:
```
python3 -c 'print(__import__("my_module").__doc__)'
```
Classes:
```
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```
Functions (inside and outside a class):
```
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```
and
```
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```
Python Unit Tests
unittest module
File extension .py
Files and folders star with test_
Organization:for models/base.py, unit tests in: tests/test_models/test_base.py
Execution command:
```
python3 -m unittest discover tests
```
or:
```
python3 -m unittest tests/test_models/test_base.py
```
run test in interactive mode
```
echo "python3 -m unittest discover tests" | bash
```
run test in non-interactive mode
To run the tests in non-interactive mode, and discover all the test, you can use the command:
```
python3 -m unittest discover tests
```