def pares(maximo):
    for numero in range(0,maximo):
        if (numero%2 ==0 ):
            yield numero

maximo=11
lista_pares=[]
for numero in pares(maximo):
    lista_pares.append(numero)

print(lista_pares)

#lista de pares con funcion Filter

numero_par=[1,2,3,4,5,6,7,8,9,10]
def pares(numero_par):
    if (numero_par %2 ==0):
        return True
    else:
        return False

resultado=filter(pares, numero_par)
par= list(resultado)
print(par)