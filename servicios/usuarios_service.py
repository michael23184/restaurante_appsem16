import json
import os
from modelos.usuario import Usuario

class UsuariosService:
    def __init__(self):
        ruta_base = os.path.dirname(__file__)
        self.ruta_usuarios = os.path.join(ruta_base, "..", "datos", "usuarios.json")
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        if os.path.exists(self.ruta_usuarios):
            with open(self.ruta_usuarios, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Usuario(**u) for u in data]
        return []

    def guardar_usuarios(self):
        data = [u.__dict__ for u in self.usuarios]
        with open(self.ruta_usuarios, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        self.guardar_usuarios()

    def actualizar_usuario(self, identificacion, nombre, correo, clave, rol):
        for u in self.usuarios:
            if u.identificacion == identificacion:
                u.nombre = nombre
                u.correo = correo
                u.clave = clave
                u.rol = rol
                self.guardar_usuarios()
                return True
        return False

    def eliminar_usuario(self, identificacion):
        self.usuarios = [u for u in self.usuarios if u.identificacion != identificacion]
        self.guardar_usuarios()

    def obtener_usuario(self, identificacion):
        for u in self.usuarios:
            if u.identificacion == identificacion:
                return u
        return None