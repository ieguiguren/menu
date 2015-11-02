#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64
from email.Utils import COMMASPACE, formatdate
import mimetypes, sys, os

hostname = os.uname()[1]
if hostname == "server1":
    prepath = "/opt"
elif hostname == "octopussy":
    prepath = "/home/xir/dev"

sys.path.append(os.path.abspath(prepath + "/menu/conf/"))
from menuconf import *

def sendmail( tipo, destination, dw ):

    mensaje = MIMEMultipart()
    mensaje['Date'] = formatdate(localtime=True)
    mensaje['From'] = sender
    mensaje['To'] = destination
    mensaje['Subject']="Menu del colegio Las Veredas"


    if tipo == "baja":
        mensaje.attach( MIMEText(baja) )
    elif tipo == "alta" or tipo == "diario":
        mensaje.attach( MIMEText(alta) )
    # Adjuntamos la imagen
        if dw != "0" and tipo == "diario":
            try:
                fi1 = open(datapath + "hoy.jpg" , "rb")
                contenido = MIMEImage(fi1.read())
                contenido.add_header('Content-Disposition', 'attachment; filename = "hoy.jpg"')
                mensaje.attach(contenido)
            except:
                mensaje.attach( "Parece que ha habido algun error.\nNO SE HA ENCONTRADO EL MENU PARA HOY\n" )
        if dw != "5" and tipo == "diario":
            try:
                fi2 = open(datapath + "manana.jpg" , "rb")
                contenido2 = MIMEImage(fi2.read())
                contenido2.add_header('Content-Disposition', 'attachment; filename = "manana.jpg"')
                mensaje.attach(contenido2)
            except:
                pass
    elif tipo == "no_available":
        mensaje.attach( MIMEText(no_available) )
    else:
        mensaje.attach ( MIMEText(ayuda))

    try:
        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(mailUser, mailPass)
        try:
            conn.sendmail(sender, destination, mensaje.as_string())
            try:
                if dw != 0:
                    fi1.close()
                if dw != 5:
                    fi2.close()
            except:
                pass
        finally:
            conn.close()

    except Exception, exc:
        sys.exit( "mail failed; %s" % str(exc) ) # give an error message


