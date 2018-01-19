#!/usr/bin/env python
# -*- coding: utf8 -*-

import random


def Write(continue_reading, MIFAREReader):

	while continue_reading:

		# Scan for cards
		(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

		# If a card is found
		if status == MIFAREReader.MI_OK:
			print "Card detected"

		# Get the UID of the card
		(status,uid) = MIFAREReader.MFRC522_Anticoll()

		# If we have the UID, continue
		if status == MIFAREReader.MI_OK:

			# Print UID
			#print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

			# This is the default key for authentication
			key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

			# Select the scanned tag
			MIFAREReader.MFRC522_SelectTag(uid)

			# Authenticate
			status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
			print "\n"

			# Check if authenticated
			if status == MIFAREReader.MI_OK:

				# Variable for the data to write
				data = []

				# Fill the data with 0xFF
				for x in range(0,16):
					data.append(0xFF)

				print "Sector 8 looked like this:"
				# Read block 8
				MIFAREReader.MFRC522_Read(8)
				print "\n"


				data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
				for x in range(0, 15):
					data[x] = int(random.random()*255)
					#print data[x]


				print "Now we fill it with data"
				MIFAREReader.MFRC522_Write(8, data)
				print "\n"

				# Check to see if it was written
				#MIFAREReader.MFRC522_Read(8)
				#print "\n"

				# Stop
				MIFAREReader.MFRC522_StopCrypto1()

				# Make sure to stop reading for cards
				continue_reading = False
			else:
				print "Authentication error"

			print "--- Finished ---"
