#!/usr/bin/env python
# -*- coding: utf8 -*-

import hashlib

#Hash data
def hashData(UID):
	#uuid is used to generate a random number
	#salt = uuid.uuid4().hex
	salt = str(1)
	uid = str(UID)

	return hashlib.sha256(salt.encode() + uid.encode()).hexdigest() + ':' + salt

#Check current hased card data with database hash
def checkData(hashedUID, UID):

	uid, salt = hashedUID.split(':')
	return uid == hashlib.sha256(salt.encode() + UID.encode()).hexdigest()