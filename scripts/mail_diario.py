#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os, sys
hostname = os.uname()[1]
if hostname == "server1":
    prepath = "/opt"
elif hostname == "octopussy":
    prepath = "/home/xir/dev"

sys.path.append(os.path.abspath(prepath + "/menu/conf/"))
from menuconf import *
sys.path.append(os.path.abspath(prepath + "/menu/lib/"))
from database import *
from libmails import *
from links import *


# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'


def get_users():
    '''None -> str[]
       Extrae de la ddbb una lista de los emails de la gente que tiene la cuenta activa'''

    dirs = []
    lista=usuarios().fetchall()
    for usuario in lista:
            dirs.append(usuario[2])
    return dirs

#Actualiza los links a "hoy"
crealinks()
for direccion in get_users():
    if direccion[0] == "+":
	print "send tg to %s" % direccion
    else:
        if os.path.exists('/opt/menu/data/hoy.jpg') or  os.path.exists('/opt/menu/data/manana.jpg'):
            sendmail( "diario", direccion, dw )
        else:
            sendmail( "no_available", "donosor00@gmail.com", dw)
