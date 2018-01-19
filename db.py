#!/usr/bin/env python
# -*- coding: utf8 -*-

import getpass
import MySQLdb
import sys

#Download and print data
def check(database, h_ash ):

	cursor = database.cursor()

	cursor.execute("SELECT * FROM users WHERE hash = %s", (h_ash))
	rows = cursor.fetchall()

	#Parse data to table
	for row in rows:
		print ''

	#Print result
	if h_ash == row[3]:
		print "Access GRANTED!"
		print "Hello "+row[1]+" "+row[2]
	else:
		print "Access DENIED!"
	print 30 * "-" , "FINISHED" , 30* "-"

#	cursor.execute("""SELECT * FROM users;""")
#	print cursor.fetchall()

#Printing database
def printDatabase(database):

	cursor = database.cursor()
	#Collecting all data from database
	cursor.execute("SELECT * FROM users")
	data = cursor.fetchall()
	#Printing data
	print 30 * "-" , "DATABASE" , 30* "-"
	for x in data:
		print x

	print 30 * "-" , "END-DATABASE" , 30* "-"


#Try to create table
def createTable(database):


	cursor = database.cursor()
	try:
		print ("Creating table")
		cursor.execute("DROP TABLE IF EXISTS users")
		cursor.execute("""CREATE TABLE IF NOT EXISTS users (
		id int(11) NOT NULL AUTO_INCREMENT,
		name varchar(30) NOT NULL,
		surrname varchar(30) NOT NULL,
		hash varchar(100) NOT NULL,
		PRIMARY KEY (id))""")
		#cursor.commit()
		print "Success"
	except MySQLdb.Error, e:
		print("Error")
		print(e)
		sys.exit()

	cursor.close()


#Write to database
def writeToDatabase(database,name,surrname,h_ash):


	cursor = database.cursor()
	#Database.execute("DROP TABLE IF EXISTS users")
	try:
		cursor.execute("""INSERT INTO users (name, surrname, hash) VALUES (%s,%s,%s)""",(name, surrname, h_ash))
		#cursor.execute(add_user, user_data)
		database.commit()
		print 'Success!!!'
	except MySQLdb.Error, e:
		print("Error!!!!")
		database.rollback()
		print(e)
		sys.exit()

	#cursor.execute("""SELECT * FROM users;""")
	#print cursor.fetchall()

#Write to database
def deleteFromDatabase(database,id):


	cursor = database.cursor()
	#Try to delete record
	try:
		delStatment = "DELETE FROM users WHERE id LIKE '%s'"
		cursor.execute(delStatment,(int(id)))
		#cursor.execute(add_user, user_data)
		database.commit()
		print 'Success!!!'
	except MySQLdb.Error, e:
		print("Error!!!!")
		database.rollback()
		print(e)
		sys.exit()


#Update database
def updateDatabase(database,data):


	cursor = database.cursor()
	
	for x in data:
		print x
	
	#Try to update record
	try:
		updateStatment = "UPDATE users SET name = %s, surrname = %s, hash = %s WHERE id LIKE %s"
		cursor.execute(updateStatment,(data))
		#cursor.execute(add_user, user_data)
		database.commit()
		print 'Success!!!'
	except MySQLdb.Error, e:
		print("Error!!!!")
		database.rollback()
		print(e)
		sys.exit()

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
		print "That was NOT a port number!\n Setting default port..."

	if port:
		print ''
	else:
		port = 3306
	#Connecto to database
	eCode = connectToDB(hostname, username, password, database, port)
	return eCode


