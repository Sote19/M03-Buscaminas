import tkinter as tk
from tkinter import messagebox
import random

class Principal:
    
    menuDIFICULTAD = {"VS 1 Terrorista": (8, 8, 10, 9), "VS Grupo Terrorista": (10, 10, 20, 7)}
    
    def __init__(self, master):
        self.master = master
        self.botones = []
        self.marco_superior = tk.Frame(self.master, bg='red', width=500, height=80)
        self.marco_superior.pack()
        self.marco_central = tk.Frame(self.master, bg='green')
        self.marco_central.pack(expand=True, fill=tk.BOTH) 
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

    def empieza_juego(self, filas, colum, minas, tamaño_casilla):
        self.filas = filas
        self.colum = colum
        self.minas = minas
        self.tamaño_casilla = tamaño_casilla
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

        self.casillas_restantes = self.filas * self.colum - self.minas

        for y in range(self.filas):
            fila = []
            for j in range(self.colum):
                boton = tk.Button(self.marco_central, width=self.tamaño_casilla, height=self.tamaño_casilla // 2, command=lambda fila=y, col=j: self.on_click(fila, col))
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
        if (fila, col) in self.marca:
            return
        
        if (fila, col) in self.revel:
            return
        
        if self.tabla[fila][col] == -1:
            messagebox.showinfo("Game Over", "¡Has perdido!")
            self.mostrar_minas()
        else:
            self.revelar_casilla(fila, col)

    def revelar_casilla(self, fila, col):
        if (fila, col) in self.revel:
            return

        self.botones[fila][col].config(text=str(self.tabla[fila][col]), state='disabled')
        self.revel.add((fila, col))

        self.casillas_restantes -= 1
        if self.casillas_restantes == 0:
            messagebox.showinfo("¡Felicidades!", "¡Has ganado!")

        if self.tabla[fila][col] == 0:
            for f in range(fila - 1, fila + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= f < self.filas and 0 <= c < self.colum and (f, c) not in self.revel:
                        self.revelar_casilla(f, c)

    def banderin(self, fila, col):
        if (fila, col) in self.marca:
            self.botones[fila][col].config(text="")
            self.marca.remove((fila, col))
        else:
            self.botones[fila][col].config(text="🚩")
            self.marca.add((fila, col))

    def mostrar_minas(self):
        for fila, col in self.minas_coor:
            self.botones[fila][col].config(text="💣", state='disabled')

root = tk.Tk()
root.geometry('583x720')
root.configure(bg="black")
root.title("Buscaminas by Xavi and Gerard")
root.resizable(False, False)

principal = Principal(root)

root.mainloop()
