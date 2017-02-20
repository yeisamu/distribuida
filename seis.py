texto = raw_input("Ingrese cadena: ")
def inverso(cadena):
    ncadena = []
    cuenta=len(cadena)
    for i in range(0,len(cadena)):
         cuentas=cuenta-i
         cuentas=cuentas-1
         ncadena.append (cadena[cuentas])
    return ncadena

print inverso(texto)