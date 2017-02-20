def maximo(uno,dos):
    if uno > dos:
        return "mayor "+str(uno)
    else:
       return "mayor "+str(dos)

x = int(input("Introduce el primer numero: "))
y = int(input("Introduce el segundo numero: "))
print maximo(x,y)