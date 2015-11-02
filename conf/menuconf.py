#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import time, os, calendar , datetime, recordatorio
#Generico
hostname = os.uname()[1]
if hostname == "server1":
    prepath = "/opt"
elif hostname == "octopussy":
    prepath = "/home/xir/dev"

path = prepath + "/menu/"
tpath = path + "tmp/"
datapath = path + "data/"
db = path + "data/usuarios.db"
descargado = "descargado.tmp"
pdfFile = "calendar.pdf"
jpgFile = "calendar"
filename = "calendar-1.jpg"
#rss = "http://cplasveredas.blogspot.com.es/p/servicio-de-comedor.html"
rss = "http://www.cpblasveredas.com/menus-de-comedor"
recordatorios = recordatorio.rec

#Tiempo
year  = time.strftime("%Y")
month = time.strftime("%m")
today = time.strftime("%d")
dw    = time.strftime("%w")
tow = datetime.date.today() + datetime.timedelta(days=1)
tomorrow = tow.strftime("%d")
#mes de mañana para los enlaces
tmonth = tow.strftime("%m")
mes = [ '','enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre','diciembre' ]
#mes a descargar en numero y letra
nmes = int(month)
if int(today) > 25:
  nmes +=  1
mesADescargar = mes[nmes]
firstweekday, month_length = calendar.monthrange(int(year), int(nmes))
nmes = "%02d" % nmes


#cuerpo emails:
predestacados = ''
if recordatorios != '':
  predestacados = "Destacados de este mes:"
encabezado = predestacados + recordatorios + """ 
Hola.

    Este servicio envia por correo, de lunes a jueves a las 7am, el menu del colegio para ese mismo dia y para el siguiente. Los viernes solo se envia el del propio viernes y el domingo se envia el del lunes.
"""

c_ayuda = """    Para solicitar el alta en el servicio envia un correo a menulasveredas@gmx.com poniendo en el asunto:
alta
    Para solicitar la baja en el servicio envia un correo a menulasveredas@gmx.com poniendo en el asunto:
baja
"""

c_alta = """Para solicitar la baja en el servicio envia un correo a menulasveredas@gmx.com poniendo en el asunto:
baja
"""

c_baja = """Si deseas volver a solicitar el alta en el servicio envia un correo a menulasveredas@gmx.com poniendo en el asunto:
alta
"""

pie = """    Para enviar sugerencias de mejora o errores, envia en el asunto la palabra sugerencia o error y en el cuerpo del mensaje la descripcion de la idea. Si es un problema, detalla todo lo posible como se puede reproducir.

    Si te resulta util este servicio y crees que deberia mejorar en algun aspecto (dominio propio, mas opciones como poder elegir la hora a la que se envian los mensajes, que el domingo se envie el menu de toda la semana o agradecer el esfuerzo de crearlo), puedes hacer una donacion a traves de Paypal a donosor00@gmail.com.

    Muchas gracias por utilizar este servicio.
"""

ayuda = encabezado + c_ayuda + pie
alta = encabezado + c_alta + pie
baja =   c_baja + pie
no_available = "Menu no disponible todavia en la web del colegio"
