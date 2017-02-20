uno=int(input("Ingrese Numero 1:\n"))
dos=int(input("Ingrese Numero 2:\n"))
tres=int(input("Ingrese Numero 3:\n"))

def max_de_tres(primero,segundo,tercero):

    if (primero > segundo and primero > tercero):
        resp="El numero mayor es: " + str(primero)
    else:
        if (segundo > primero and segundo > tercero):
            resp ="El numero mayor es: " + str(segundo)
        else:
            resp="El numero mayor es: " + str(tercero)
    return resp

print max_de_tres(uno,dos,tres)