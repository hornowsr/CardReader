#!/usr/bin/env python
# -*- coding: utf8 -*-

import hashlib
import uuid

#Hash data
def hashData(UID):
    #uuid is used to generate a random number
    salt = uuid.uuid4().hex
    uid = 0
    for x in UID:
        uid += x
    uid = str(uid)

    return hashlib.sha256(salt.encode() + uid.encode()).hexdigest() + ':' + salt

def checkData(hashedUID, UID):

    uid , salt = hashedUID.split(':')
    return uid == hashlib.sha256(salt.encode() + UID.encode()).hexdigest()