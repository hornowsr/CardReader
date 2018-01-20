#!/usr/bin/env python
# -*- coding: utf8 -*-

import getpass
import MySQLdb
import sys



#Download and print data
def check(database, h_ash ):

	cursor = database.cursor()

	cursor.execute("SELECT * FROM users WHERE hash = %s", (h_ash))

	if not cursor.rowcount:
		print ("Access DENIED!")
	else:
		#Parse data to table
		for row in cursor:
			print ("")
		else:
			#Print result
			if h_ash == row[3]:
				print ("Access GRANTED!")
				print (("Hello " + row[1] + " " + row[2]))
	print ((30 * "-", "FINISHED", 30 * "-"))

#	cursor.execute("""SELECT * FROM users;""")
#	print cursor.fetchall()



#Printing database
def printDatabase(database):

	cursor = database.cursor()
	#Collecting all data from database
	cursor.execute("SELECT * FROM users")
	data = cursor.fetchall()
	#Printing data
	print ((30 * "-", "DATABASE", 30 * "-"))
	for x in data:
		print (x)

	print ((30 * "-", "END-DATABASE", 30 * "-"))




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
		print ("Success")
	except MySQLdb.Error as e:
		print("Error")
		print(e)
		sys.exit()

	cursor.close()




#Write to database
def writeToDatabase(database,name,surrname,h_ash):

	cursor = database.cursor()
	#Database.execute("DROP TABLE IF EXISTS users")
	try:
		cursor.execute("""INSERT INTO users
						(name, surrname, hash)
						VALUES (%s,%s,%s)""", (name, surrname, h_ash))
		#cursor.execute(add_user, user_data)
		database.commit()
		print ('Success!!!')
	except MySQLdb.Error as e:
		print("Error!!!!")
		database.rollback()
		print(e)
		sys.exit()

	#cursor.execute("""SELECT * FROM users;""")
	#print cursor.fetchall()




#Delete from database database
def deleteFromDatabase(database,id):

	cursor = database.cursor()
	#Try to delete record
	try:
		delStatment = "DELETE FROM users WHERE id LIKE '%s'"
		cursor.execute(delStatment, (int(id)))
		#cursor.execute(add_user, user_data)
		database.commit()
		print ('Success!!!')
	except MySQLdb.Error as e:
		print("Error!!!!")
		database.rollback()
		print(e)
		sys.exit()




#Update database
def updateDatabase(database,data):

	cursor = database.cursor()

	for x in data:
		print (x)

	#Try to update record
	try:
		updateStatment = """UPDATE users SET
							name = %s,
							surrname = %s,
							hash = %s
							WHERE id LIKE %s"""
		cursor.execute(updateStatment, (data))
		#cursor.execute(add_user, user_data)
		database.commit()
		print ('Success!!!')
	except MySQLdb.Error as e:
		print("Error!!!!")
		database.rollback()
		print(e)
		sys.exit()



#Check if database exists
def checkIfDatabaseExists(database, name):

	cursor = database.cursor()

	showStatment = "SHOW DATABASES LIKE %s"
	cursor.execute(showStatment, name)
	if cursor.fetchone():
		return True
	else:
		return False



#Try to connect to database
def connectToDB(hostname, username, password, database, port):

	try:
		myC = MySQLdb.connect(host=hostname,
							user=username,
							passwd=password,
							db=database,
							port=port,
							connect_timeout=10)
		if checkIfDatabaseExists(myC, database):
			return myC
		else:
			print ("Cannot connec to databse!")
			sys.exit()
		#check(myC)
		#myC.close()
	except MySQLdb.Error as e:
		try:
			print (("MySQL Error [%d]: %s \n" % (e.args[0], e.args[1])))
			return 1
		except IndexError:
			print (("MySQL Error: %s \n" % str(e)))




#Collect data and connect to database
def collectData():

	#Initialize port
	port = 3306
	validate = True

	#Get essential values
	while validate:
		hostname = raw_input(("Enter hostname:"))
		validate = checkHostname(hostname)

	username = raw_input(("Enter username:"))
	password = getpass.getpass("Enter password:")
	database = raw_input(("Enter database name:"))

	#Get and check port value
	try:
		port = int(raw_input(("Enter port(default : 3306):")))
	except ValueError:
		print ("That was NOT a port number!\n Setting default port...")

	if port:
		print ('')
	else:
		port = 3306
	#Connect to to database
	eCode = connectToDB(hostname, username, password, database, port)
	return eCode



#Check hostname
def checkHostname(host):

	value = True

	#Split data
	data = host.split('.')
	#Check if lenght is correct
	if len(data) == 4:
		for x in range(0, 4):
			try:
				#Check if data is an integer
				valueData = int(data[x])
				#Chek if data is in range
				if valueData > 0 and valueData < 256:
					continue
				else:
					value = False
			except ValueError:
				value = False
				break
	else:
		value = False
	if value:
		return False
	else:
		print ("You have entered wrog hostname!!")
		print ("It should look like: x.x.x.x where x is between 1 and 255 ")
		return True

