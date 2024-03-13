from tkinter import *  #importamos la libreria tkinter
from tkinter import messagebox
import random

#-------------------------------configuracion de ventana-------------------------------

root = Tk()                                      #asignamos a "root" como si fuera Tkinter
root.geometry('500x660')                         #aplicamos a la ventana una medida ('WIDTHxHEIGHT')
root.configure(bg="black")                       #aplicamos color de fondo de la ventana
root.title("Buscaminas by Xavi and Gerard")      #cambiamos el nombre de la ventana
root.resizable(False, False)                     #bloqueamos el reescalado de la ventana

#-------------------------------zonas de la ventana-------------------------------

marco_superior = Frame(root, bg='red', width=500, height=80)  #medidas banner superior
marco_superior.place(x=0, y=0)  #posición

marco_central = Frame(root, bg='green', width=500, height=500)  #medidas donde se jugará
marco_central.place(x=0, y=80)  #posición

marco_inferior = Frame(root, bg='blue', width=500, height=80) #medidas banner inferior
marco_inferior.place(x=0, y=580)  #posicion

#-------------------------------funciones-------------------------------

class Principal:
    #-------------------------------menú dificultad-------------------------------
    
    menuDIFICULTAD = {"Fácil": (8, 8, 10), "Medio": (10, 10, 20), "Difícil": (12, 12, 30)}    #asignamos una variable con los valores que tendrá cada dificultad
                                                                                              #{"Dificultad": (celdas, columnas, minas) , ...}
    
    def __init__(self, master):                #definimos "__init__", el cual se llamara cada vez que creemos objetos nuevos en la clase Principal
        self.master = master                   #guardamos variable master cuando se inicie la clase Principal
        self.buttons = []                      #lista vacia para almacenar los botones del menú

        self.create_menu()                     #aplicamos a la función que definirá la dificultad que el usuario vaya a escoger

    def create_menu(self):
        menu = tk.Menu(self.master)            #creamos variable con funcionalidad por defecto de tkinter para crear menus
        self.master.config(menu=menu)

        difficulty_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Dificultad", menu=difficulty_menu)
        for difficulty in Principal.menuDIFICULTAD:
            difficulty_menu.add_command(label=difficulty, command=lambda d=difficulty: self.start_game(*Principal.menuDIFICULTAD[d]))

#-------------------------------iniciar juego-------------------------------
root.mainloop()    
