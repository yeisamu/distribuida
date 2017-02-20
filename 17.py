c=int(input("Introduce cantida de elementos "))
palabra=[]
for i in range(0,c):
    palabra.append(raw_input("Palabra "+str(i+1)+" "))

def mas_larga(lista):
    mayor=len(lista[0])
    maslarga=lista[0]
    for palabra in lista:
        if mayor <= len(palabra):
            mayor=len(palabra)
            maslarga = palabra
        else:
            maslarga=maslarga
    return maslarga


print "la palabra mas larga es : "+mas_larga(palabra)