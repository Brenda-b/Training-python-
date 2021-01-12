import pickle
fichero= open("fichero.pckl","rb")
diccionario_leido=pickle.load(fichero)
print(diccionario_leido)