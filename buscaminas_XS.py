from tkinter import *  #importamos la libreria tkinter
from tkinter import messagebox
import random

#-------------------------------configuracion de ventana-------------------------------
root = Tk()                                      #creamos ventana
root.geometry('500x660')                         #aplicamos a la ventana una medida ('WIDTHxHEIGHT')
root.configure(bg="black")                       #aplicamos color de fondo de la ventana
root.title("Buscaminas by Xavi and Gerard")      #cambiamos el nombre de la ventana
root.resizable(False, False)                     #bloqueamos el reescalado de la ventana

#-------------------------------preparamos zonas de la ventana

marco_superior = Frame(root, bg='red', width=500, height=80)  #medidas banner superior
marco_superior.place(x=0, y=0)  #posición

marco_central = Frame(root, bg='green', width=500, height=500)  #medidas donde se jugará
marco_central.place(x=0, y=80)  #posición

marco_inferior = Frame(root, bg='blue', width=500, height=80) #medidas banner inferior
marco_inferior.place(x=0, y=580)  #posicion


class Principal:
    
    


#-------------------------------iniciar ventana-------------------------------
root.mainloop()    