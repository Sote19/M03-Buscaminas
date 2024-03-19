import tkinter as tk  #importamos la libreria tkinter
from tkinter import messagebox
import random #importamos la libreria
#-------------------------------configuracion de ventana-------------------------------

root = tk.Tk()                                      #asignamos a "root" como si fuera Tkinter
root.geometry('500x660')                         #aplicamos a la ventana una medida ('WIDTHxHEIGHT')
root.configure(bg="black")                       #aplicamos color de fondo de la ventana
root.title("Buscaminas by Xavi and Gerard")      #cambiamos el nombre de la ventana
root.resizable(False, False)                     #bloqueamos el reescalado de la ventana

#-------------------------------zonas de la ventana-------------------------------

marco_superior = tk.Frame(root, bg='red', width=500, height=80)  #medidas banner superior
marco_superior.place(x=0, y=0)  #posición

marco_central = tk.Frame(root, bg='green', width=500, height=500)  #medidas donde se jugará
marco_central.place(x=0, y=80)  #posición

marco_inferior = tk.Frame(root, bg='blue', width=500, height=80) #medidas banner inferior
marco_inferior.place(x=0, y=580)  #posicion

#-------------------------------funciones-------------------------------

class Principal:
    #-------------------------------menú dificultad-------------------------------
    
    menuDIFICULTAD = {"VS 1 Terrorista": (8, 8, 10), "VS Grupo Terrorista": (10, 10, 20), "VS Terroristas Internacionales": (12, 12, 30)}    #asignamos una variable con los valores que tendrá cada dificultad
    #{"Dificultad": (celdas, columnas, minas) , ...}
    
    
    def __init__(self, master):                #definimos "__init__", el cual se llamara cada vez que creemos objetos nuevos en la clase Principal
        self.master = master                   #guardamos variable master cuando se inicie la clase Principal
        self.botones = []                      #lista vacia para almacenar los botones del menú

        self.create_menu()                     #aplicamos a la función que definirá la dificultad que el usuario vaya a escoger

    def create_menu(self):
        menu = tk.Menu(self.master)            #creamos variable con funcionalidad por defecto de tkinter para crear menus
        self.master.config(menu=menu)

        difficulty_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="¿A que misión quieres enfrentarte?", menu=difficulty_menu)
            
        for difficulty in Principal.menuDIFICULTAD:
            difficulty_menu.add_command(label=difficulty, command=lambda d=difficulty: self.empieza_juego(*Principal.menuDIFICULTAD[d]))



    def empieza_juego (self, filas, colum, minas): #Creamos funcion para definir los parametros del tablero
        self.filas = filas
        self.colum = colum
        self.minas = minas                                    
        self.minas_coor = []
        self.revel = set()
        self.marca = set()
        self.campo = set()
        
        self.crear_tabla()
#------------------------------- Crear Tablero -----------------------------

    def crear_tabla(self):
        for i in self.botones:
            for boton in i:
                boton.grid_forget() #Para limpiar el tablero despues de cambiar la dificultad
        self.botones = []
        self.tabla = [[0] * self.colum for x in range(self.filas)]
        self.añadir_mina()
        self.añadir_nums()
        
        for y in range (self.filas):
            fila = []
            for j in range(self.colum):
                boton = tk.Button(self.master, width=2, height=1, command=lambda fila=y, col=j: self.on_click(fila, col))
                boton.bind("<Button-3>", lambda event, fila=y, col=j: self.banderin(fila, col))
                boton.grid(fila=y, col=j)
                fila.append(boton)
            self.botones.append(fila)
    
    def añadir_mina(self):
        self.minas_coor=random.sample([(f, c) for f in range (self.filas) for c in range (self.colum)], self.minas)
        for fila, col in self.minas_coor:
            self.tabla[fila][col] = -1
            
    def añadir_nums(self):
        for fila, col, in self.minas_coor:
            for f in range (fila -1, fila +2):
                for c in range (col -1, col +2):
                    if 0 <= f < self.filas and 0 <= c < self.colum and self.tabla[f][c] != -1: 
                        self.tabla[f][c] += 1       
            
            
            
            
            
principal = Principal(root) #Creamos punto de guardado y llamamos

#-------------------------------iniciar juego-------------------------------
root.mainloop()    