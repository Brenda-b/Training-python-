class Coche:
    def __init__ (self, marca, color, combustible, cilindrada):
        self.marca= marca
        self.color= color
        self.combustible= combustible
        self.cilindrada= cilindrada
    def mostrar_caracteristicas (self):
        print( "La marca es {} de color {}, el tipo de combustible que utiliza es {}, y las cilindradas que tiene es de {}".format(self.marca,self.color,self.combustible,self.cilindrada))
coche1 = Coche( "opel", "rojo", "gasolina", "1.6")
print(coche1.mostrar_caracteristicas())