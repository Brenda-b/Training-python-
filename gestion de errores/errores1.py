def operacion(numero1,numero2,numero3):
    resultado= numero1/(numero2 - numero3)
    return resultado
try:
    numero1=5
    numero2=4
    numero3=2
    resultado= operacion(numero1, numero2, numero3)
except:
    print("Estas intentando dividir por cero, cambia alguno de los dos ultimos numeros")
else:
    print(resultado)
finally:
    print("gracias por probar!")

