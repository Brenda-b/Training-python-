numero_par=[1,2,3,4,5,6,7,8,9,10]
def pares(numero_par):
    if (numero_par %2 ==0):
        return True
    else:
        return False

resultado=filter(pares, numero_par)
par= list(resultado)
print(par)