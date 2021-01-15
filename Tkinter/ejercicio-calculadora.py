import tkinter
from tkinter.constants import CENTER, END
ventana= tkinter.Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")
ventana.resizable(False,False)
ventana.configure(background="gray")
#funciones
operacion=""
resultado= tkinter.StringVar()
def click(valor):
    global operacion
    global resultado
    operacion= operacion+ str(valor)
    pantalla.delete(0, END)
    pantalla.insert(0, operacion)

def borrar():
    global operacion
    global resultado
    operacion=""
    pantalla.delete(0, END)

def calcular():
    global operacion
    global resultado
    try:
        resultado= str(eval(operacion))
    except:
        resultado="ERROR"
    finally:
        pantalla.delete(0, END)
        pantalla.insert(0, resultado)

#display de los resultados
pantalla=tkinter.Entry(ventana, font=("arial", 20, "bold"), borderwidth=2)
pantalla.grid(row=0, column=0, columnspan=3, pady=10, padx=5)

#boton AC
boton_reset= tkinter.Button(ventana, text="AC",width=8, height=2, command= lambda:borrar())
boton_reset.grid(row=0, column=3, pady=10)

#botones de numero
ancho=8
alto=3
boton1=tkinter.Button(ventana, text="1", width=ancho, height=alto, command=lambda:click("1"))
boton1.grid (row=1, column=0, padx=3, pady=5)

boton2=tkinter.Button(ventana, text="2", width=ancho, height=alto, command=lambda:click("2"))
boton2.grid(row=1, column=1, padx=3, pady=5)

boton3=tkinter.Button(ventana, text="3", width=ancho, height=alto,command=lambda:click("3"))
boton3.grid(row=1, column=2, padx=3, pady=5)

boton4=tkinter.Button(ventana, text="4", width=ancho, height=alto,command=lambda:click("4"))
boton4.grid(row=1, column=3, padx=3, pady=5)

boton5=tkinter.Button(ventana, text="5", width=ancho, height=alto,command=lambda:click("5"))
boton5.grid(row=2, column=0, padx=3, pady=5)

boton6=tkinter.Button(ventana, text="6", width=ancho, height=alto,command=lambda:click("6"))
boton6.grid(row=2, column=1, padx=3, pady=5)

boton7=tkinter.Button(ventana, text="7", width=ancho, height=alto,command=lambda:click("7"))
boton7.grid(row=2, column=2, padx=3, pady=5)

boton8=tkinter.Button(ventana, text="8", width=ancho, height=alto,command=lambda:click("8"))
boton8.grid(row=2, column=3, padx=3, pady=5)

boton9=tkinter.Button(ventana, text="9", width=ancho, height=alto,command=lambda:click("9"))
boton9.grid(row=3, column=0, padx=3, pady=5)

boton0=tkinter.Button(ventana, text="0", width=ancho, height=alto,command=lambda:click("0"))
boton0.grid(row=3, column=1, padx=3, pady=5)

boton_punto=tkinter.Button(ventana, text=".", width=ancho, height=alto,command=lambda:click("."))
boton_punto.grid(row=3, column=2, padx=3, pady=5)

boton_suma=tkinter.Button(ventana, text="+", width=ancho, height=alto,command=lambda:click("+"))
boton_suma.grid(row=3, column=3, padx=3, pady=5)

boton_resta=tkinter.Button(ventana, text="-", width=ancho, height=alto,command=lambda:click("-"))
boton_resta.grid(row=4, column=0, padx=3, pady=5)

boton_multiplicacion=tkinter.Button(ventana, text="*", width=ancho, height=alto,command=lambda:click("*"))
boton_multiplicacion.grid(row=4, column=1, padx=3, pady=5)

boton_division=tkinter.Button(ventana, text="/", width=ancho, height=alto,command=lambda:click("/"))
boton_division.grid(row=4, column=2, padx=3, pady=5)

boton_igual=tkinter.Button(ventana, text="=", width=ancho, height=alto,command=lambda:calcular())
boton_igual.grid(row=4, column=3, padx=3, pady=5)


ventana.mainloop()