#!/usr/bin/env python
# -*- coding: utf-8 -*-
def evalvocal(caracter):
    vocales = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

    if caracter in vocales:
       return True
    else:
        return False

vocal = raw_input("Ingrese un caracter:\n")
print evalvocal(vocal)
