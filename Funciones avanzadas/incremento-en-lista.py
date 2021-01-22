def multiplicar(numero):
    return numero+10

lista=[1,2,3,4,5,6,7,8,9,10]
numeros_incrementados=list(map(multiplicar, lista))
print(numeros_incrementados)