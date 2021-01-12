class ClaseSilla: 
    color="blanco"
    precio=100
objetoSilla1=ClaseSilla()
print(objetoSilla1.color)
objetoSilla2=ClaseSilla()
objetoSilla2.color="verde"
objetoSilla2.precio=120
print("el color de la silla2 es "+ objetoSilla2.color)
class Personas:
   def __init__ (self,nombre,edad):
       self.nombre= nombre
       self.edad= edad
   def saludar(self): 
      print("hola, me llamo {} y tengo {} años".format(self.nombre,self.edad))
persona1= Personas("Brenda", 23)
print(persona1.edad)
print(persona1.nombre)
print(persona1.saludar())