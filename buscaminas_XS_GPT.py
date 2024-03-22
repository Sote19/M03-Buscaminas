import tkinter as tk
from tkinter import messagebox
import random

class Principal:
    
    menuDIFICULTAD = {"VS 1 Terrorista": (8, 8, 10), "VS Grupo Terrorista": (10, 10, 20), "VS Terroristas Internacionales": (12, 12, 30)}
    
    def __init__(self, master):
        self.master = master
        self.botones = []
        self.marco_superior = tk.Frame(self.master, bg='red', width=500, height=80)
        self.marco_superior.pack()
        self.marco_central = tk.Frame(self.master, bg='green')
        self.marco_central.pack(expand=True, fill=tk.BOTH) # Expande el marco central para llenar el espacio disponible
        self.marco_inferior = tk.Frame(self.master, bg='blue', width=500, height=80)
        self.marco_inferior.pack()
        self.create_menu()

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        difficulty_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="¿A qué misión quieres enfrentarte?", menu=difficulty_menu)
            
        for difficulty in Principal.menuDIFICULTAD:
            difficulty_menu.add_command(label=difficulty, command=lambda d=difficulty: self.empieza_juego(*Principal.menuDIFICULTAD[d]))

    def empieza_juego(self, filas, colum, minas):
        self.filas = filas
        self.colum = colum
        self.minas = minas
        self.minas_coor = []
        self.revel = set()
        self.marca = set()
        self.campo = set()
        self.crear_tabla()

    def crear_tabla(self):
        for i in self.botones:
            for boton in i:
                boton.grid_forget()
        self.botones = []
        self.tabla = [[0] * self.colum for x in range(self.filas)]
        self.añadir_mina()
        self.añadir_nums()
        
        for y in range(self.filas):
            fila = []
            for j in range(self.colum):
                boton = tk.Button(self.marco_central, width=4, height=2, command=lambda fila=y, col=j: self.on_click(fila, col))
                boton.bind("<Button-3>", lambda event, row=y, column=j: self.banderin(row, column))
                boton.grid(row=y, column=j)
                fila.append(boton)
            self.botones.append(fila)

    def añadir_mina(self):
        self.minas_coor=random.sample([(f, c) for f in range(self.filas) for c in range(self.colum)], self.minas)
        for fila, col in self.minas_coor:
            self.tabla[fila][col] = -1
            
    def añadir_nums(self):
        for fila, col in self.minas_coor:
            for f in range(fila - 1, fila + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= f < self.filas and 0 <= c < self.colum and self.tabla[f][c] != -1: 
                        self.tabla[f][c] += 1       

    def on_click(self, fila, col):
        pass

    def banderin(self, fila, col):
        pass

root = tk.Tk()
root.geometry('500x660')
root.configure(bg="black")
root.title("Buscaminas by Xavi and Gerard")
root.resizable(False, False)

principal = Principal(root)

root.mainloop()
