import json
import os
from modelos.usuario import Usuario

class AuthService:
    def __init__(self):
        # Ruta absoluta al archivo usuarios.json
        ruta_base = os.path.dirname(__file__)  # carpeta servicios
        self.ruta_usuarios = os.path.join(ruta_base, "..", "datos", "usuarios.json")

    def validar_acceso(self, correo, clave):
        try:
            with open(self.ruta_usuarios, "r", encoding="utf-8") as f:
                usuarios = json.load(f)
            for u in usuarios:
                usuario = Usuario(
                    identificacion=u["identificacion"],
                    nombre=u["nombre"],
                    correo=u["correo"],
                    clave=u["clave"],
                    rol=u["rol"]   # ✅ ahora sí pasamos el rol
                )
                if usuario.correo == correo and usuario.clave == clave:
                    return True, usuario
            return False, None
        except Exception as e:
            print("Error al validar acceso:", e)
            return False, None