c= int(input("Introduce un numero entre (1-100000) "))
if(c < 0 or c > 100000 ):
    print "numero fuera de rango"
else:
    num=str(c)
    cuentac=0;
    for i in num:
        cuentac=cuentac+1
    print cuentac