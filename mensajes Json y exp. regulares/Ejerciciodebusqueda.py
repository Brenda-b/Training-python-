import re 
def busqueda(palabra_a_buscar, texto):
      buscar =re.search(palabra_a_buscar,texto)
      if(buscar):
            print(buscar)
      else:
            print("cadena no encontrada")