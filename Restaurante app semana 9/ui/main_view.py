import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(
        self,
        root,
        servicio,
        cerrar_sesion,
        guardar_productos,
        guardar_ventas
    ):
        self.root = root
        self.servicio = servicio
        self.cerrar_sesion = cerrar_sesion
        self.guardar_productos = guardar_productos
        self.guardar_ventas = guardar_ventas

        self.frame = tk.Frame(
            root,
            padx=20,
            pady=20
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        # -----------------------------------------
        # TÍTULO
        # -----------------------------------------

        titulo = tk.Label(
            self.frame,
            text="Sistema de Restaurante",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            pady=(0, 5)
        )

        subtitulo = tk.Label(
            self.frame,
            text="Menú principal",
            font=("Arial", 12)
        )

        subtitulo.pack(
            pady=(0, 15)
        )

        # -----------------------------------------
        # MENÚ
        # -----------------------------------------

        menu_frame = tk.Frame(
            self.frame
        )

        menu_frame.pack(
            fill="x",
            pady=10
        )

        boton_productos = tk.Button(
            menu_frame,
            text="Productos",
            width=15,
            command=self.mostrar_productos
        )

        boton_productos.grid(
            row=0,
            column=0,
            padx=5
        )

        boton_usuarios = tk.Button(
            menu_frame,
            text="Usuarios",
            width=15,
            command=self.mostrar_usuarios
        )

        boton_usuarios.grid(
            row=0,
            column=1,
            padx=5
        )

        boton_ventas = tk.Button(
            menu_frame,
            text="Ventas",
            width=15,
            command=self.mostrar_ventas
        )

        boton_ventas.grid(
            row=0,
            column=2,
            padx=5
        )

        boton_cerrar = tk.Button(
            menu_frame,
            text="Cerrar sesión",
            width=15,
            command=self.cerrar
        )

        boton_cerrar.grid(
            row=0,
            column=3,
            padx=5
        )

        # -----------------------------------------
        # CONTENIDO
        # -----------------------------------------

        self.contenido_frame = tk.Frame(
            self.frame
        )

        self.contenido_frame.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.mostrar_productos()

    # =================================================
    # LIMPIAR CONTENIDO
    # =================================================

    def limpiar_contenido(self):

        for widget in self.contenido_frame.winfo_children():
            widget.destroy()

    # =================================================
    # PRODUCTOS
    # =================================================

    def mostrar_productos(self):

        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido_frame,
            text="Gestión de productos",
            font=("Arial", 16, "bold")
        )

        titulo.pack(
            pady=10
        )

        formulario = tk.LabelFrame(
            self.contenido_frame,
            text="Registrar producto",
            padx=10,
            pady=10
        )

        formulario.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # Código

        tk.Label(
            formulario,
            text="Código:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.codigo_entry = tk.Entry(
            formulario,
            width=30
        )

        self.codigo_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # Nombre

        tk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.nombre_entry = tk.Entry(
            formulario,
            width=30
        )

        self.nombre_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # Categoría

        tk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        self.categoria_entry = tk.Entry(
            formulario,
            width=30
        )

        self.categoria_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        # Precio

        tk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=3,
            column=0,
            padx=5,
            pady=5
        )

        self.precio_entry = tk.Entry(
            formulario,
            width=30
        )

        self.precio_entry.grid(
            row=3,
            column=1,
            padx=5,
            pady=5
        )

        # Stock

        tk.Label(
            formulario,
            text="Stock:"
        ).grid(
            row=4,
            column=0,
            padx=5,
            pady=5
        )

        self.stock_entry = tk.Entry(
            formulario,
            width=30
        )

        self.stock_entry.grid(
            row=4,
            column=1,
            padx=5,
            pady=5
        )

        boton_registrar = tk.Button(
            formulario,
            text="Registrar producto",
            command=self.registrar_producto
        )

        boton_registrar.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=10
        )

        # Tabla

        tabla_frame = tk.LabelFrame(
            self.contenido_frame,
            text="Productos registrados",
            padx=10,
            pady=10
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "stock"
        )

        self.tabla_productos = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_productos.heading(
            "codigo",
            text="Código"
        )

        self.tabla_productos.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_productos.heading(
            "categoria",
            text="Categoría"
        )

        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )

        self.tabla_productos.heading(
            "stock",
            text="Stock"
        )

        self.tabla_productos.pack(
            fill="both",
            expand=True
        )

        productos = self.servicio.listar_productos()

        for producto in productos:

            self.tabla_productos.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    producto.precio,
                    producto.stock
                )
            )

    def registrar_producto(self):

        codigo = self.codigo_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        categoria = self.categoria_entry.get().strip()
        precio_texto = self.precio_entry.get().strip()
        stock_texto = self.stock_entry.get().strip()

        if not codigo or not nombre or not categoria:
            messagebox.showwarning(
                "Producto",
                "Complete todos los campos."
            )
            return

        try:
            precio = float(precio_texto)
            stock = int(stock_texto)

        except ValueError:
            messagebox.showerror(
                "Producto",
                "Precio y stock deben ser valores válidos."
            )
            return

        try:

            from modelos.producto import Producto

            producto = Producto(
                codigo,
                nombre,
                categoria,
                precio,
                stock
            )

            resultado = self.servicio.registrar_producto(producto)

            if not resultado:
                messagebox.showerror(
                    "Producto",
                    "No se pudo registrar el producto."
                )
                return

            self.guardar_productos()

            messagebox.showinfo(
                "Producto",
                "Producto registrado correctamente."
            )

            self.mostrar_productos()

        except ValueError as error:

            messagebox.showerror(
                "Producto",
                str(error)
            )

    # =================================================
    # USUARIOS
    # =================================================

    def mostrar_usuarios(self):

        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido_frame,
            text="Gestión de usuarios",
            font=("Arial", 16, "bold")
        )

        titulo.pack(
            pady=10
        )

        formulario = tk.LabelFrame(
            self.contenido_frame,
            text="Registrar usuario",
            padx=10,
            pady=10
        )

        formulario.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # Identificación

        tk.Label(
            formulario,
            text="Identificación:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.identificacion_entry = tk.Entry(
            formulario,
            width=30
        )

        self.identificacion_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # Nombre

        tk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.nombre_usuario_entry = tk.Entry(
            formulario,
            width=30
        )

        self.nombre_usuario_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # Correo

        tk.Label(
            formulario,
            text="Correo:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        self.correo_entry = tk.Entry(
            formulario,
            width=30
        )

        self.correo_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        boton_registrar = tk.Button(
            formulario,
            text="Registrar usuario",
            command=self.registrar_usuario
        )

        boton_registrar.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10
        )

        # Tabla

        tabla_frame = tk.LabelFrame(
            self.contenido_frame,
            text="Usuarios registrados",
            padx=10,
            pady=10
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columnas = (
            "identificacion",
            "nombre",
            "correo"
        )

        self.tabla_usuarios = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_usuarios.heading(
            "identificacion",
            text="Identificación"
        )

        self.tabla_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_usuarios.heading(
            "correo",
            text="Correo"
        )

        self.tabla_usuarios.pack(
            fill="both",
            expand=True
        )

        usuarios = self.servicio.listar_usuarios()

        for usuario in usuarios:

            self.tabla_usuarios.insert(
                "",
                tk.END,
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.correo
                )
            )

    def registrar_usuario(self):

        identificacion = self.identificacion_entry.get().strip()
        nombre = self.nombre_usuario_entry.get().strip()
        correo = self.correo_entry.get().strip()

        if not identificacion or not nombre or not correo:
            messagebox.showwarning(
                "Usuario",
                "Complete todos los campos."
            )
            return

        try:

            resultado = self.servicio.registrar_usuario(
                identificacion,
                nombre,
                correo
            )

            if not resultado:
                messagebox.showerror(
                    "Usuario",
                    "No se pudo registrar el usuario."
                )
                return

            messagebox.showinfo(
                "Usuario",
                "Usuario registrado correctamente."
            )

            self.mostrar_usuarios()

        except ValueError as error:

            messagebox.showerror(
                "Usuario",
                str(error)
            )

    # =================================================
    # VENTAS
    # =================================================

    def mostrar_ventas(self):

        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido_frame,
            text="Gestión de ventas",
            font=("Arial", 16, "bold")
        )

        titulo.pack(
            pady=10
        )

        # -----------------------------------------
        # FORMULARIO DE VENTA
        # -----------------------------------------

        contenedor = tk.LabelFrame(
            self.contenido_frame,
            text="Registrar venta",
            padx=10,
            pady=10
        )

        contenedor.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # Usuario

        tk.Label(
            contenedor,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.usuario_combo = ttk.Combobox(
            contenedor,
            state="readonly",
            width=35
        )

        usuarios = self.servicio.listar_usuarios()

        usuarios_valores = [
            usuario.identificacion
            for usuario in usuarios
        ]

        self.usuario_combo["values"] = usuarios_valores

        self.usuario_combo.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # Producto

        tk.Label(
            contenedor,
            text="Producto:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.producto_combo = ttk.Combobox(
            contenedor,
            state="readonly",
            width=35
        )

        productos = self.servicio.listar_productos()

        productos_valores = [
            producto.codigo
            for producto in productos
        ]

        self.producto_combo["values"] = productos_valores

        self.producto_combo.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # Cantidad

        tk.Label(
            contenedor,
            text="Cantidad:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.cantidad_entry = tk.Entry(
            contenedor,
            width=38
        )

        self.cantidad_entry.insert(
            0,
            "1"
        )

        self.cantidad_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        # Botón registrar

        boton_registrar = tk.Button(
            contenedor,
            text="Registrar venta",
            command=self.registrar_venta
        )

        boton_registrar.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=5,
            pady=10
        )

        # -----------------------------------------
        # TABLA DE VENTAS
        # -----------------------------------------

        tabla_frame = tk.LabelFrame(
            self.contenido_frame,
            text="Ventas registradas",
            padx=10,
            pady=10
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columnas = (
            "usuario",
            "producto",
            "cantidad",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "cantidad",
            text="Cantidad"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.column(
            "usuario",
            width=150
        )

        self.tabla_ventas.column(
            "producto",
            width=150
        )

        self.tabla_ventas.column(
            "cantidad",
            width=100
        )

        self.tabla_ventas.column(
            "fecha",
            width=180
        )

        self.tabla_ventas.pack(
            fill="both",
            expand=True
        )

        # Mostrar ventas existentes

        ventas = self.servicio.listar_ventas()

        for venta in ventas:

            self.tabla_ventas.insert(
                "",
                tk.END,
                values=(
                    venta.usuario_id,
                    venta.producto_codigo,
                    venta.cantidad,
                    venta.fecha
                )
            )

    def registrar_venta(self):

        usuario_id = self.usuario_combo.get().strip()
        producto_codigo = self.producto_combo.get().strip()
        cantidad_texto = self.cantidad_entry.get().strip()

        # -----------------------------------------
        # VALIDAR USUARIO
        # -----------------------------------------

        if not usuario_id:

            messagebox.showwarning(
                "Venta",
                "Seleccione un usuario."
            )

            return

        # -----------------------------------------
        # VALIDAR PRODUCTO
        # -----------------------------------------

        if not producto_codigo:

            messagebox.showwarning(
                "Venta",
                "Seleccione un producto."
            )

            return

        # -----------------------------------------
        # VALIDAR CANTIDAD
        # -----------------------------------------

        try:

            cantidad = int(cantidad_texto)

        except ValueError:

            messagebox.showerror(
                "Venta",
                "La cantidad debe ser un número entero."
            )

            return

        if cantidad <= 0:

            messagebox.showerror(
                "Venta",
                "La cantidad debe ser mayor que cero."
            )

            return

        # -----------------------------------------
        # REGISTRAR VENTA
        # -----------------------------------------

        resultado = self.servicio.vender_producto(
            producto_codigo,
            usuario_id,
            cantidad
        )

        if not resultado:

            messagebox.showerror(
                "Venta",
                "No se pudo registrar la venta.\n\n"
                "Verifique que el usuario y producto existan "
                "y que haya suficiente stock."
            )

            return

        # -----------------------------------------
        # GUARDAR CAMBIOS
        # -----------------------------------------

        self.guardar_productos()

        self.guardar_ventas()

        # -----------------------------------------
        # MENSAJE
        # -----------------------------------------

        messagebox.showinfo(
            "Venta registrada",
            "La venta se registró correctamente."
        )

        # -----------------------------------------
        # ACTUALIZAR TABLA
        # -----------------------------------------

        self.mostrar_ventas()

    # =================================================
    # CERRAR SESIÓN
    # =================================================

    def cerrar(self):

        self.cerrar_sesion()