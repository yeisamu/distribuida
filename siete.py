texto = raw_input("Ingrese palabra: ")
def palindromo(cadena):
    ncadena = []
    comparac=[]
    cuenta=len(cadena)
    for i in range(0,len(cadena)):
         cuentas=cuenta-i
         cuentas=cuentas-1
         ncadena.append (cadena[cuentas])
         comparac.append(cadena[i])
    if(ncadena==comparac):
      return "Palindromo"
    else:
       return "no es palindromo"

print palindromo(texto)