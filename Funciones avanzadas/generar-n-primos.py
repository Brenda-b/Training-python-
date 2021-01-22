def primos(maximo):
    for x in range (0,maximo):
        contador=0
        for y in range (1, x):
            if (x%y==0 ):
                contador=contador +1
        if contador<2 :
            yield x 

maximo=100
lista_primos=[]
for numeros in primos(maximo):
    lista_primos.append(numeros)

print(lista_primos)
 

