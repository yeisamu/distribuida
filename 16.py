c=int(input("Introduce un numero "))
num=str(c)
cuentac=0
for i in num:
    numero = int(num[cuentac])
    if(numero%2==0):
        print str(numero) + " Par "
    cuentac = cuentac + 1