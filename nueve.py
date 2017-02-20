n= int(input("Introduce cantidad de caracteres a generar: "))
c= raw_input("Introduce caracter a generar: ")
def genera_n_caracteres(cant,car):
    ncar=""
    for i in range(0,cant):
        ncar=ncar+car
    return ncar

print genera_n_caracteres(n,c)