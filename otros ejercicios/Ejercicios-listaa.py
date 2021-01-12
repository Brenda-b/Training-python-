minimo=20
maximo=500
print("Introduce un numero")
dato=input()
numero=int(dato)
if(numero<minimo): print("valor bajo")
if(numero>maximo): print("valor alto")
if(numero>minimo)and(numero<maximo): print("valor medio")