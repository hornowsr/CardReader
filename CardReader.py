#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import Read

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
def printmenu():
	print 30 * "-" , "MENU" , 30* "-"
	print "1. Read"
	print "2. Reset card"
	print "3. Add user"
	print "4. Delete user"
	print "5. Load DATABASE"
	print "0. Exit"
	print 67 * "-"


loop = True

while loop:
	printmenu()
	choice = input("Enter your choice[1-5]:\n")
	continue_reading = True
	if choice == 1:
		print "Option 1 was selected"
		print "Please place the card near the reader\n"
		# This loop keeps checking for chips. If one is near it will get the UID and authenticate
		Read.Read(continue_reading, MIFAREReader)

	elif choice == 2:
		print "Option 2 was selected"
		print "Please place the card near the reader"
		
		# Hook the SIGINT
		signal.signal(signal.SIGINT, end_read)
		
		# Create an object of the class MFRC522
		MIFAREReader = MFRC522.MFRC522()
		
		# This loop keeps checking for chips. If one is near it will get the UID and authenticate
		while continue_reading:
			
			# Scan for cards    
			(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
			
			# If a card is found
			if status == MIFAREReader.MI_OK:
				print "Card detected\n"
		
			# Get the UID of the card
			(status,uid) = MIFAREReader.MFRC522_Anticoll()
			
			# If we have the UID, continue
			if status == MIFAREReader.MI_OK:
				
				#Stop waiting for the card
				countinue_reading = False

				# Print UID
				print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
				
				# This is the default key for authentication
				key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
				
				# Select the scanned tag
				MIFAREReader.MFRC522_SelectTag(uid)
				
				# Dump the data
				MIFAREReader.MFRC522_DumpClassic1K(key, uid)
				
				# Stop
				MIFAREReader.MFRC522_StopCrypto1()
			print "\n"
			time.sleep(2)


		
	#elif choice == 3:
	#
	#elif choice == 4:
	
	elif choice == 3:
		print ""
	elif choice == 4:
		print ""
	elif choice == 5:
		print ""
	elif choice == 0:
		loop = False
	else:
		raw_input("Wrong option was selected. Enter any key to try again..")
#
