import pickle
frutas={"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}
fichero= open("fichero.pckl","wb")
pickle.dump(frutas, fichero)
fichero.close()
print(fichero)