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



def crealinks( ):
        
    for dest in [ datapath + "hoy.jpg", datapath + "manana.jpg"]:
        try:
            os.unlink(dest)
        except:
            pass
    os.symlink( datapath + year + month +  "/" + today + ".jpg" ,  datapath  + "hoy.jpg" )
    os.symlink( datapath + year + tmonth + "/" + tomorrow + ".jpg", datapath + "manana.jpg" )


