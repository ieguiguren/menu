#!/usr/bin/env python

import sqlite3, sys, os

hostname = os.uname()[1]
if hostname == "server1":
    prepath = "/opt"
elif hostname == "octopussy":
    prepath = "/home/xir/dev"

sys.path.append(os.path.abspath(prepath + "/menu/conf/"))
from menuconf import *

def connect():
    return sqlite3.connect(datapath + 'usuarios.db')

def fusuario( usuario ):
    conn = connect()
    cursor = conn.cursor()
    return cursor.execute("SELECT * FROM emails WHERE email =?", (usuario,) ), conn

def usuarios():
    conn = connect()
    cursor = conn.cursor()
    return cursor.execute("SELECT * FROM emails WHERE enable =1 ")

def add( conn, cursor, usuario, funcion ):
    if funcion == "insert":
       cursor.execute('INSERT INTO emails (email, enable,subscription_type, when_to_recieve) VALUES (?,?,?,?)', usuario )
    else:
       cursor.execute("UPDATE emails SET enable = 1 WHERE email =?", (usuario[0],))
    conn.commit()
    conn.close()

def delete( conn, cursor, usuario ):
    cursor.execute("UPDATE emails SET enable = 0 WHERE email =?", (usuario,))
    conn.commit()
    conn.close()

