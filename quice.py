c=int(input("Introduce un numero "))
num=str(c)
cuentac=0;
suma=0;

for i in num:
   cuentac=cuentac+1
if(cuentac == 1):
    if(c%2==0):
        print str(c)+" es Par "
    else:
        print str(c) + " es impar "
else:
    cuentac=0
    for i in num:
        suma = int(num[cuentac])+suma
        cuentac = cuentac + 1
if(int(suma)%2==0):
   print "la suma de los digitos es "+str(suma)+" y es Par "
else:
   print"la suma de los digitos es "+ str(suma) + " y es impar "
