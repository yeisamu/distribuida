n= int(input("Introduce cantidad de elementos: "))
l1=[]
l2=[]
for i in range(0,n):
    l1.append(raw_input("lista 1 posicion ["+str(i+1)+str("] ")))

for i in range(0,n):
    l2.append(raw_input("lista 2 posicion ["+str(i+1)+str("] ")))
concide=0;
for i in range(0, n):
    for y in range(0, n):
        if(l1[i]==l2[y]):
            concide=concide+1

if concide>=1:
    print "true"
else:
    print "false"