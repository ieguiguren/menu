#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
hostname = os.uname()[1]
if hostname == "server1":
    prepath = "/opt"
elif hostname == "octopussy":
    prepath = "/home/xir/dev"

import sys, urllib, os,cStringIO
try:
    import pycurl
except:
    print "Intentando instalar pycurl"
    try:
       os.system('sudo apt-get install -y python-pycurl')
       import pycurl
    except:
       print "No ha sido posible instalar la libreria necesaria *pycurl*"
       print "Intentalo a mano"
       sys.exit(254)

try:
    from BeautifulSoup import BeautifulSoup
except:
    print "Intentando instalar BeautifulSoap"
    try:
       os.system('sudo apt-get install -y python-beautifulsoup')
       from BeautifulSoup import BeautifulSoup
    except:
       print "No ha sido posible instalar la libreria necesaria *BeautifulSoap*"
       print "Intentalo a mano"
       sys.exit(254)

sys.path.append(os.path.abspath(prepath + "/menu/conf/"))
from menuconf import *
sys.path.append(os.path.abspath(prepath + "/menu/lib/"))
from images import *

mes = [ 'zero','enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre','diciembre' ]
if int(today) > 27:
  mesADescargar = mes[int(month) + 1]
else:
  mesADescargar = mes[int(month)]

def get_image_url( url ):
    buf = cStringIO.StringIO()
    d = pycurl.Curl()
    d.setopt(d.URL, url)
    d.setopt(d.WRITEFUNCTION, buf.write)
    d.perform()
    menu = False
    encontrado = False
    for p in buf.getvalue().split('>'):
        if "Men" in p:
            if mesADescargar in p.lower():
              menu = True
        if menu and not encontrado:
            if "imageanchor" in p:
              encontrado = True
              img = p.split(' ')[1][6:-1]
    buf.close()
    try:
      return img
    except:
      return ""

# if dir exists, don't download again
if os.path.isfile(datapath + str(descargado)):
        sys.exit()
else:
    url = get_image_url(rss)
    if url != "":
      urllib.urlretrieve(url, tpath + filename)
      create_images()
      f = open (datapath + str(descargado), 'w')
      f.close()
