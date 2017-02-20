#!/usr/bin/env python
# -*- coding: utf-8 -*-
def es_bisiesto(anio):
	if anio%4 == 0:
		if anio%100 != 0:
			print("Es bisiesto")
	else:
		print("No es bisiesto")

anio = input("Escriba un año para saber si es bisiesto: ")
es_bisiesto(anio)