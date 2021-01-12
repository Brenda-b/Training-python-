import moduloficheros
nombre_fichero = "fichero1.txt"
fichero= moduloficheros.Ficheros(nombre_fichero)
texto= "esta es la primera linea de mi fuchero.\nY esta es la segunda linea de mi fichero."
fichero.grabar_fichero(texto)
texto="\n ahora estoy queriendo agregar una tercera fila."
fichero.incluir_fichero(texto)
aaversianda= fichero.leer_fichero()
print(aaversianda)