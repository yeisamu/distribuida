#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
ruta_s= socket.socket()
#coneccion con el servidor
ruta_s.connect(("localhost",35000))

while True:
    mensaje=raw_input("ingrese operacion y los valores ")
    ruta_s.send(mensaje)
    datos = ruta_s.recv(1000)
    print datos
    #verificar mensaje para salir
    if mensaje == 'salir':
        break
print "Vuelva cuando quiera"
#cerrar conexion con el servidor
ruta_s.close()