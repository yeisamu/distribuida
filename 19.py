#!/usr/bin/env python
# -*- coding: utf-8 -*-
numero = int(raw_input("Ingrese un numero decimal positivo\n"))
binario = ""
if (numero > 0):
    while(numero > 0):
        if (numero%2 == 0):
            binario = "0" + binario
        else:
            binario = "1" + binario
        numero = int(numero/2)
else:
    if (numero == 0):
        binario = "0"
    else:
        binario = "No se pudo convertir el numero. Ingrese solo numeros positivos"
print("El resultado de la conversion es: "+binario)
raw_input()