#!/usr/bin/env python
# -*- coding: utf8 -*-

import getpass
import MySQLdb

#Download and print data
def check(database, h_ash ):

    cursor = database.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    for row in rows:
        print row

    print "DATABASE HASH:"
    print row[3]
    print "CARD HASH:"
    print h_ash
    print "AAAAAAAAAAAAAAAAA"

    if h_ash == row[3]:
        print "Access granted!"
    else:
        print "Access denied!"

    cursor.execute("""SELECT * FROM users;""")
    print cursor.fetchall()

#Write to database
def writeToDatabase(database,name, surrname,h_ash):

    add_user = ("INSERT INTO users "
                "name"
                "VALUES (%s)"
                )

    user_data = 2

    cursor = database.cursor()
    #Database.execute("DROP TABLE IF EXISTS users")
    try:
        #Database.execute("""INSERT INTO test VALUES (%s,%s,%s)""",(name, surrname, h_ash))
        cursor.execute(add_user, user_data)
        database.commit()
        print 'Success'
    except:
        database.rollback()
        print 'Error'

    cursor.execute("""SELECT * FROM users;""")
    print cursor.fetchall()


#Try to connect to database
def connectToDB(hostname, username, password, database, port):

    try:
        myC = MySQLdb.connect(host = hostname, user = username, passwd = password, db = database, port = port )
        return myC
        #check(myC)
        #myC.close()
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


