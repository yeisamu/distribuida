#!/usr/bin/env python
# -*- coding: utf-8 -*-
def sumar(lista):
    sum = 0
    for i in range(0, len(lista)):
        sum = sum + lista[i]
    return sum

def multiplica(lista):
    res = 1
    for i in range(0, len(lista)):
        res = res * lista[i]
    return res

#A = [1, 2, 3, 5]
n=int(input("cantidad de elementos:\n"))
lista=[]
for i in range(0,n):
    lista.append(int(input("ingrese elemento "+str(i+1)+" de la lista \n")))

print "La Suma de los elementos es: " + str(sumar(lista))

print "La Multiplicación de los elementos es: " + str(multiplica(lista))
