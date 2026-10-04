import tkinter as tk
from tkinter import messagebox
from servicios.auth_service import AuthService
from ui.main_view import MainView
import os
from PIL import Image, ImageTk  # Pillow ya instalado

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Login")
        self.root.geometry("400x350")
        self.root.configure(bg="#f0f0f0")

        # Logo redimensionado
        ruta_logo = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png.png")
        if os.path.exists(ruta_logo):
            img = Image.open(ruta_logo)
            # Usar LANCZOS en lugar de ANTIALIAS
            img = img.resize((100, 100), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(img)
            tk.Label(root, image=self.logo_img, bg="#f0f0f0").pack(pady=10)

        # Servicio de autenticación
        self.auth_service = AuthService()

        # Etiquetas y campos
        tk.Label(root, text="Correo:", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(pady=5)
        self.entry_correo = tk.Entry(root, width=30)
        self.entry_correo.pack()

        tk.Label(root, text="Clave:", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(pady=5)
        self.entry_clave = tk.Entry(root, width=30, show="*")
        self.entry_clave.pack()

        # Botón ingresar
        tk.Button(root, text="Ingresar", command=self.login,
                  bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
                  width=15).pack(pady=15)

    def login(self):
        correo = self.entry_correo.get()
        clave = self.entry_clave.get()
        valido, usuario = self.auth_service.validar_acceso(correo, clave)

        if valido:
            messagebox.showinfo("Acceso permitido", f"Bienvenido {usuario.nombre}")
            self.root.destroy()  # cerrar login
            main_root = tk.Tk()
            MainView(main_root, usuario)  # abrir ventana principal
            main_root.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o clave incorrectos")

# Para pruebas rápidas
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()  