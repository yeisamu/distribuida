#!/usr/bin/env python
# -*- coding: utf-8 -*-
palabra=raw_input("Ingrese Palabra ")
mayus="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cuentamayus=0
for letra in palabra:
    if letra in mayus:
        cuentamayus=cuentamayus+1
print cuentamayus