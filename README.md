# Restaurante App - Semana 16

Este proyecto corresponde a la evolución del sistema de restaurante desarrollado en semanas anteriores.  
En esta versión se implementan las funcionalidades solicitadas por el docente para la Semana 16.

---

## 🚀 Funcionalidades principales

- **Login con validación de roles**:
  - Acceso mediante correo y clave.
  - Roles definidos: **Administrador**, **Empleado**, **Cliente**.
  - Solo el **Administrador** puede acceder a la gestión de usuarios.

- **Gestión de Usuarios (CRUD)**:
  - Registrar nuevos usuarios.
  - Actualizar datos de usuarios existentes.
  - Eliminar usuarios.
  - Visualizar usuarios en un `Treeview` con columnas: ID, Nombre, Correo, Rol.
  - Persistencia en archivo `usuarios.json`.

- **Eventos implementados**:
  - `<<TreeviewSelect>>`: carga datos al formulario al seleccionar una fila.
  - `<Return>`: registra usuario al presionar Enter.
  - `<Escape>`: limpia el formulario.
  - `<<ComboboxSelected>>`: muestra mensaje al cambiar el rol.

- **Interfaz gráfica (Tkinter)**:
  - Ventana principal con menú:
    - Gestión de Productos.
    - Gestión de Ventas.
    - Reportes.
    - Usuarios (solo Administrador).
    - Salir.
  - Ventana de Gestión de Usuarios con formulario, botones y tabla.

---

## 📂 Estructura del proyecto

restaurante_appsem16/
├── assets/              # Recursos gráficos
├── datos/               # Archivos JSON (usuarios, productos, ventas)
├── modelos/             # Clases: Usuario, Producto, Venta
├── servicios/           # Lógica de negocio (auth_service, usuarios_service)
├── ui/                  # Interfaces gráficas (login_view, main_view, usuarios_view)
├── main.py              # Punto de entrada
└── README.md            # Documentación del proyecto

Código

---

## ▶️ Ejecución

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd restaurante_appsem16
Ejecutar el sistema:

bash
python main.py
Ingresar con un usuario Administrador:

Correo: michael@correo.com

Clave: 1234

Rol: Administrador

Desde el menú principal acceder a las funcionalidades:

Productos

Ventas

Reportes

Usuarios (solo Administrador)

✅ Conclusión
La versión de Semana 16 cumple con:

Separación de responsabilidades (modelos, servicios, interfaces).

Gestión de usuarios con roles y eventos.

Interfaz gráfica clara y funcional.

Persistencia de datos en archivos JSON.

Este README documenta la evolución del proyecto y los pasos necesarios para su ejecución.