#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import Read
import Write
import db
import Hash
import sys

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
    print "5. Connect to to DATABASE"
    print "0. Exit"
    print 67 * "-"


loop = True

while loop:

    eCode = ''
    print 30 * "-" , "MENU" , 30* "-"
    print 'Firstly we have to connect to database\n'
    eCode = db.collectData()

    #Check if connection with database is established
    if eCode == 1:
            sys.exit()
    else:

        print 'Connection established!\n\n'
        #Print main menu
        printmenu()
        choice = input("Enter your choice[0-5]:\n")
        continue_reading = True
        if choice == 1:
            print "Option 1 was selected"
            print "Please place the card near the reader\n"
            #Read function. Waiting for card to read
            uid = Read.Read(continue_reading, MIFAREReader)
            for x in uid:
                print x
            print "\n"
            h_ash = Hash.hashData(uid)
            print h_ash
            time.sleep(2)

        elif choice == 2:
            print "Option 2 was selected"
            print "Please place the card near the reader"

            Write.Write(continue_reading, MIFAREReader)
            print "\n"
            time.sleep(2)

        elif choice == 3:
            print ""
        elif choice == 4:
            print ""
        elif choice == 5:
            print "Option 5 was selected"
            db.collectData()
        elif choice == 0:
            loop = False
        else:
            raw_input("Wrong option was selected. Enter any key to try again..")