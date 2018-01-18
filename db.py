#!/usr/bin/env python
# -*- coding: utf8 -*-

import getpass
import MySQLdb

#Download and print data
def doQuery( conn ):
    cur = conn.cursor()

    cur.execute("SELECT * FROM test")
    rows = cur.fetchall()

    for row in rows:
        print row


#Try to connect to database
def connectToDB(hostname, username, password, database, port):

    try:
        myC = MySQLdb.connect(host = hostname, user = username, passwd = password, db = database, port = port )
        doQuery(myC)
        myC.close()
    except MySQLdb.Error, e:
        print "MySQL Error: %s \n" % str(e)
        return 1


    #Print inserted values
    print hostname, ";", username, ";", password, ";", database, ";", port, "\n"

#Collect data and connect to database
def collectData():

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
        print "That was NOT a port number!\n Settin default port..."

    if port:
        print ''
    else:
        port = 3306

    eCode = connectToDB(hostname, username, password, database, port)
    return eCode


