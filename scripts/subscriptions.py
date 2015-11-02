#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import sys, os
hostname = os.uname()[1]
if hostname == "server1":
    prepath = "/opt"
elif hostname == "octopussy":
    prepath = "/home/xir/dev"

try:
    from imbox import Imbox
except:
    print """Imbox libray not already installed:
git clone https://github.com/ieguiguren/imbox.git
cd imbox/
sudo apt-get install python-setuptools
sudo python setup.py install
"""
    sys.exit(1)
sys.path.append(os.path.abspath(prepath + "/menu/conf/"))
from menuconf import *
sys.path.append(os.path.abspath(prepath + "/menu/lib/"))
from database import *
from libmails import *

def ayuda( remitente ):
    ''' str -> none '''
    sendmail( "ayuda", remitente, 6 )

def alta ( remitente ) :
    cursor, conn = fusuario(remitente)
    if cursor.fetchone() == None:
         add ( conn, cursor, ( remitente, 1, "diary", 7), "insert" )
    else:
         add ( conn, cursor, ( remitente, 1, "diary", 7), "update" )
    sendmail ("alta", remitente, 6)

def baja ( remitente ) :
    cursor, conn = fusuario(remitente)
    rem = cursor.fetchone()
    if rem != None:
        delete( conn, cursor, rem[2])
    sendmail ("baja", rem[2], 6)

imbox = Imbox( IMAPserver, mailUser, PASSWORD, True)
unread_messages = imbox.messages(unread=True)

for iud, message in unread_messages:
    sender = message.sent_from[0]['email']
    command = message.subject.lower()
    
    if sender == "service@gmx.com" or sender == "MAILER-DAEMON@mail.gmx.com":
        pass

    elif command.find('alta') > -1:
        alta( sender )
        imbox.delete( iud)
      
    elif command.find('baja') > -1:
        baja( sender )
        imbox.delete( iud)
      
    else:
        ayuda( sender )
        imbox.delete( iud)

