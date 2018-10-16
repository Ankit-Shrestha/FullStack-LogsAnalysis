# Project Title

A python based reporting tool that outputs reports based on the date in the database. This program uses psycopg2 module to connect to the database.

## Getting Started

One should be familiar with running python code, basic LINUX command line, and SQL statements.


### Installing

1. Download and install [Vagrant](https://www.vagrantup.com/)

2. Download and install [Virtual Box](https://www.virtualbox.org/)

3. Get the database : This program uses a database, ```newsdata.sql``` provided by Udacity NanoDegree Program. After that, get the ```newsdata.sql``` and ```newsdata.py``` , obtained from the repository and move then to the vagrant directory that you will get with the virtual machine.

## Running the tests

Run the following command line instructions in the terminal

1. ```vagrant up``` followed by ```vagrant ssh``` to set up the virtual machine.
2. ```cd vagrant``` to get into vagrant folder. ```ls``` to check if you have the database, ```newsdata.sql``` and python code, ```newsdata.py``` on the same folder.
3. ```psql -d news -f newsdata.sql``` to load the data from the database.
4. ```python3 newsdata.py``` to run the program.