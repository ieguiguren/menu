#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys, os

hostname = os.uname()[1]
if hostname == "server1":
    prepath = "/opt"
elif hostname == "octopussy":
    prepath = "/home/xir/dev"

try:
    import Image
except:
    print "Intentando instalar Image (python-imaging)"
    try:
       os.system('sudo apt-get install -y python-imaging')
       import Image
    except:
       print "No ha sido posible instalar la libreria necesaria *Image*"
       print "Intentalo a mano"
       sys.exit(254)

sys.path.append(os.path.abspath(prepath + "/menu/conf/"))
from menuconf import *


def resize():
    image1=Image.open( tpath + filename )
    width=1600
    height = 1131
    image2=image1.resize((width,height),Image.ANTIALIAS)
    image2.save( tpath + "_" + filename )

def discard_header_right():
    ''' discards header and right non menu relevant from image and returns just menu '''
    image_path = tpath + "_" + filename
    img = Image.open(image_path)
    upper = 148
    left = 10
    right = 1363
    height = 1124
    bbox = (left, upper, right, height)
    working_slice = img.crop(bbox)
    working_slice.save( tpath + "__" + filename )

def cut_days():
    ''' int -> none
    gets the weekday of first day of month and saves the menu of each day in a dir of name MMYYYY
    '''
    
    d = datapath + year + str(nmes) 
    if not os.path.exists(d):
        os.makedirs(d)
    else:
        return
    discard_header_right()
    for day in range( 1, month_length + 1 ):
        if day == 1:
            day_of_week = firstweekday
            week = 0
        else:
            day_of_week += 1
            if day_of_week == 7:
                day_of_week =0
                if day > 3:
                    week += 1
        if day_of_week < 5:
            cut(year, month, day, day_of_week, week)

def cut( year, month, day, day_of_week, week ):
    image_path = tpath + "__" + filename
    img = Image.open(image_path)
    # calc coordenates depending on day of week and day of month
    x=[0,270,537,804,1081,1350]
    y=[0,184,376,568,758,973]
    upper = y[week ]
    lower = y[week + 1 ]
    left  = x[day_of_week]
    right = x[day_of_week + 1]
    bbox = (left, upper, right, lower)
    working_slice = img.crop(bbox)
    working_slice.save(datapath + year + "{0:0>2}".format(int(month)) + "/" + "{0:0>2}".format(int(day)) + ".jpg")

def create_images():
    resize()
    cut_days()
