#!/usr/bin/env python
# -*- coding: utf-8 -*-
#inicio
import socket
#se crea una variable de conoxion tipo socket
server= socket.socket()
#direccion ip del servidor y puerto de la conexion
server.bind(("",35000))
#cuantas conexiones se van a escuchar
server.listen(1)
ruta_c, direccion=server.accept()
def suma(n1,n2):
    rsuma= int(n1) + int(n2)
    return rsuma

while True:
    #tamaño de los mensajes enviados por el cliente
    recibido=ruta_c.recv(1024)
    if recibido == 'salir':
        break
    string=recibido.split(" ")
    #Devolvemos el mensaje al cliente
    if string[0]=='suma':
       resuma= suma(string[1],string[2])
       ruta_c.send(str(resuma))
    #devolver peticion al cliente
print "Hasta la Vista"
ruta_c.close()
server.close()