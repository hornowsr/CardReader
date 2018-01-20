#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import Read
import Write
import db
import sys
import User

assert sys.version_info >= (2, 7)
assert sys.version_info < (3, 0)

GPIO.setwarnings(False)

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):

	global continue_reading
	print ("Ctrl+C captured, ending program.")
	continue_reading = False
	GPIO.cleanup()
	sys.exit()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
def printmenu():

	print ((30 * "-", "MENU", 30 * "-"))
	print ("1. Read")
	print ("2. Reset card")
	print ("3. Add user")
	print ("4. Delete user")
	print ("5. Update user")
	print ("6. Print database")
	print ("0. Exit")
	print ((67 * "-"))


loop = True

while loop:

	eCode = ''
	print ((30 * "-", "MENU", 30 * "-"))
	print ("Firstly we have to connect to database\n")
	eCode = db.collectData()

	#Check if connection with database is established
	if eCode == 1:
		sys.exit()
	else:
		print ("Connection established!\n\n")
		#Print main menu
		while loop:
			printmenu()
			choice = input(("Enter your choice[0-6]:"))
			continue_reading = True
			if choice == 1:
				print ((30 * "-", "OPTION1 SELECTED", 30 * "-\n"))

				#Read function. Waiting for card to read
				h_ash = Read.Read(continue_reading, MIFAREReader, eCode)
				Read.checkCardWithDatabase(eCode, h_ash)

				time.sleep(2)

			elif choice == 2:
				print ((30 * "-", "OPTION2 SELECTED", 30 * "\n"))
				print ("Please place the card near the reader")
				Write.Write(continue_reading, MIFAREReader)
				print ("\n")
				time.sleep(2)

			elif choice == 3:
				print ((30 * "-", "OPTION3 SELECTED", 30 * "-\n"))
				User.addUser(continue_reading, MIFAREReader, eCode)
			elif choice == 4:
				print ((30 * "-", "OPTION4 SELECTED", 30 * "-\n"))
				User.deleteUser(eCode)
			elif choice == 6:
				print ((30 * "-", "OPTION5 SELECTED", 30 * "-\n"))
				db.printDatabase(eCode)
			elif choice == 5:
				print ((30 * "-", "OPTION6 SELECTED", 30 * "-\n"))
				User.updateUserData(continue_reading, MIFAREReader, eCode)
			elif choice == 0:
				loop = False
				eCode.close()
			else:
				raw_input("Wrong option was selected. Enter enter to try again..")
