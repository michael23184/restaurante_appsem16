import tkinter as tk
from tkinter import messagebox
from ui.usuarios_view import UsuariosView

class MainView:
    def __init__(self, root, usuario_actual):
        self.root = root
        self.root.title("Restaurante App - Principal")
        self.root.geometry("500x400")
        self.usuario_actual = usuario_actual

        # Bienvenida
        tk.Label(root, text=f"Bienvenido {usuario_actual.nombre}",
                 font=("Arial", 14, "bold")).pack(pady=20)

        # Botones principales
        tk.Button(root, text="Gestion de Productos",
                  bg="blue", fg="white", width=25, height=2).pack(pady=2)

        tk.Button(root, text="Gestion de Ventas",
                  bg="green", fg="white", width=25, height=2).pack(pady=2)

        tk.Button(root, text="Reportes",
                  bg="orange", fg="white", width=25, height=2).pack(pady=2)

        # Boton Usuarios solo para Administrador
        if usuario_actual.rol == "Administrador":
            tk.Button(root, text="Usuarios",
                      bg="purple", fg="white", width=25, height=2,
                      command=self.abrir_usuarios).pack(pady=2)

        tk.Button(root, text="Salir",
                  bg="red", fg="white", width=25, height=2,
                  command=root.destroy).pack(pady=20)

    def abrir_usuarios(self):
        usuarios_root = tk.Toplevel(self.root)
        UsuariosView(usuarios_root, self.usuario_actual)