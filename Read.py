#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time

def Read(continue_reading, MIFAREReader):
    
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
				
				continue_reading = False
        			# Print UID
       				print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    
        			# This is the default key for authentication
        			key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        			# Select the scanned tag
        			MIFAREReader.MFRC522_SelectTag(uid)

        			# Authenticate
        			status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

	        		# Check if authenticated
	        		if status == MIFAREReader.MI_OK:
	            			MIFAREReader.MFRC522_Read(8)
	            			MIFAREReader.MFRC522_StopCrypto1()
				else:
					print "Authentication error"

		#print "\n"
		#time.sleep(2)
