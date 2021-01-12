import re
texto= "Hola, mi nombre es Antonio"
busqueda= re.search("nombre$", texto)
print(busqueda)