import tkinter as tk
from tkinter import ttk, messagebox
from modelos.usuario import Usuario
from servicios.usuarios_service import UsuariosService

class UsuariosView:
    def __init__(self, root, usuario_actual):
        self.root = root
        self.root.title("Gestion de Usuarios")
        self.servicio = UsuariosService()
        self.usuario_actual = usuario_actual

        # Solo el administrador puede acceder
        if usuario_actual.rol != "Administrador":
            messagebox.showerror("Acceso denegado", "Solo el Administrador puede gestionar usuarios")
            self.root.destroy()
            return

        # Formulario
        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Identificacion").grid(row=0, column=0)
        self.entry_id = tk.Entry(frame_form)
        self.entry_id.grid(row=0, column=1)

        tk.Label(frame_form, text="Nombre").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(frame_form, text="Correo").grid(row=2, column=0)
        self.entry_correo = tk.Entry(frame_form)
        self.entry_correo.grid(row=2, column=1)

        tk.Label(frame_form, text="Clave").grid(row=3, column=0)
        self.entry_clave = tk.Entry(frame_form, show="*")
        self.entry_clave.grid(row=3, column=1)

        tk.Label(frame_form, text="Rol").grid(row=4, column=0)
        self.combo_rol = ttk.Combobox(frame_form, values=["Administrador", "Empleado", "Cliente"])
        self.combo_rol.grid(row=4, column=1)
        self.combo_rol.bind("<<ComboboxSelected>>", self.on_rol_selected)

        # Botones
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="Registrar", command=self.registrar).grid(row=0, column=0, padx=5)
        tk.Button(frame_buttons, text="Actualizar", command=self.actualizar).grid(row=0, column=1, padx=5)
        tk.Button(frame_buttons, text="Eliminar", command=self.eliminar).grid(row=0, column=2, padx=5)
        tk.Button(frame_buttons, text="Limpiar", command=self.limpiar).grid(row=0, column=3, padx=5)

        # Treeview
        self.tree = ttk.Treeview(root, columns=("id","nombre","correo","rol"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("correo", text="Correo")
        self.tree.heading("rol", text="Rol")
        self.tree.pack(pady=10)

        # Eventos
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.root.bind("<Return>", lambda e: self.registrar())
        self.root.bind("<Escape>", lambda e: self.limpiar())

        self.cargar_treeview()

    def cargar_treeview(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for u in self.servicio.usuarios:
            self.tree.insert("", "end", values=(u.identificacion, u.nombre, u.correo, u.rol))

    def registrar(self):
        usuario = Usuario(
            self.entry_id.get(),
            self.entry_nombre.get(),
            self.entry_correo.get(),
            self.entry_clave.get(),
            self.combo_rol.get()
        )
        self.servicio.registrar_usuario(usuario)
        self.cargar_treeview()
        self.limpiar()

    def actualizar(self):
        ok = self.servicio.actualizar_usuario(
            self.entry_id.get(),
            self.entry_nombre.get(),
            self.entry_correo.get(),
            self.entry_clave.get(),
            self.combo_rol.get()
        )
        if ok:
            self.cargar_treeview()
            self.limpiar()
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def eliminar(self):
        self.servicio.eliminar_usuario(self.entry_id.get())
        self.cargar_treeview()
        self.limpiar()

    def limpiar(self, event=None):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_clave.delete(0, tk.END)
        self.combo_rol.set("")

    def on_select(self, event):
        item = self.tree.selection()
        if item:
            valores = self.tree.item(item)["values"]
            usuario = self.servicio.obtener_usuario(valores[0])
            if usuario:
                self.entry_id.delete(0, tk.END)
                self.entry_id.insert(0, usuario.identificacion)
                self.entry_nombre.delete(0, tk.END)
                self.entry_nombre.insert(0, usuario.nombre)
                self.entry_correo.delete(0, tk.END)
                self.entry_correo.insert(0, usuario.correo)
                self.entry_clave.delete(0, tk.END)
                self.entry_clave.insert(0, usuario.clave)
                self.combo_rol.set(usuario.rol)

    def on_rol_selected(self, event):
        messagebox.showinfo("Rol seleccionado", f"Rol: {self.combo_rol.get()}")