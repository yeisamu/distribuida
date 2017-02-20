n=int(input("cantidad de elementos:\n"))
lista=[]
for i in range(0,n):
    lista.append(raw_input("ingrese elemento "+str(i+1)+" de la lista \n"))

def cuenta(lista):
    totelem = 0
    for i in lista:
        totelem += 1
    return totelem

print str(cuenta(lista))+" elemento en la lista "+str(lista)