#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

hostname = os.uname()[1]
if hostname == "server1":
    prepath = "/opt"
elif hostname == "octopussy":
    prepath = "/home/xir/dev"

from subprocess import call

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



def get_pdf_url( url ):
    buf = cStringIO.StringIO()
    d = pycurl.Curl()
    d.setopt(d.URL, url)
    d.setopt(d.WRITEFUNCTION, buf.write)
    d.setopt(pycurl.FOLLOWLOCATION, 1)
    d.perform()
    soup=BeautifulSoup(buf.getvalue())
    for i in soup.findAll('td', {'class':'td-file'}):
        j = str(i)
        if mesADescargar in j.lower():
            enlaces = i.findAll('a')[1]['href']
            return "http://www.cpblasveredas.com" + enlaces
    return ""

def convertToImage(pdf, jpg):
	"""Converts pdf file to jpg
	   Needs pdftocairo"""
	call(["pdftocairo","-jpeg",pdf,jpg])

	

def main():
# if the directory exists, don't download again
    if not os.path.isfile(datapath + str(descargado)):
        url = get_pdf_url(rss)
        if url != "":
          urllib.urlretrieve(url, tpath + pdfFile)
          jpgFile = 'calendar'
          convertToImage(tpath + pdfFile, tpath + jpgFile )
          resize()
          cut_days()
          f = open (datapath + str(descargado), 'w')
          f.close()

if __name__ == "__main__":
	main()
