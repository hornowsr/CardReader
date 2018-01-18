#!/usr/bin/env python
# -*- coding: utf8 -*-

import getpass

#Collect data and connect to database
def connectDB():

    #Initialize port
    port = 3306

    #Get essential values
    hostname = raw_input("Enter hostname:")
    username = raw_input("Enter username:")
    password = getpass.getpass("Enter password:")
    database = raw_input("Enter database name:")

    #Get and check port value
    try:
        port = int(raw_input("Enter port(default : 3306):"))
    except ValueError:
        print "That was NOT a number!"

    if port:
        print ''
    else:
        port = 3306




    #Print inserted values
    print hostname, ";", username, ";", password, ";", database, ";", port, "\n"

