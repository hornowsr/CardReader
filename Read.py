#!/usr/bin/env python
# -*- coding: utf8 -*-

import Hash
import db

#Read data from card
def Read(continue_reading, MIFAREReader, database):

	cont = continue_reading
	print ("Please place the card near the reader\n")
	while cont:

		# Scan for cards
		(status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

		# If a card is found
		if status == MIFAREReader.MI_OK:
			print ("Card detected\n")

		# Get the UID of the card
		(status, uid) = MIFAREReader.MFRC522_Anticoll()

		# If we have the UID, continue
		if status == MIFAREReader.MI_OK:
			cont = False

			# This is the default key for authentication
			key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

			# Select the scanned tag
			MIFAREReader.MFRC522_SelectTag(uid)
			# Authenticate
			status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
			# Check if authenticated
			if status == MIFAREReader.MI_OK:
				cardID = str(MIFAREReader.MFRC522_Read(8))
				MIFAREReader.MFRC522_StopCrypto1()
			else:
				print ("Authentication error")

			h_ash = Hash.hashData(cardID)
			print ((30 * "-", "FINISHED READING", 30 * "-"))
			return h_ash

#Check data with database
def checkCardWithDatabase(database, h_ash):

	print ("Checking card...")
	db.check(database, h_ash)

