import tkinter as tk

from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio

from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion:

    def __init__(self, root):
        self.root = root

        self.root.title("Restaurante App")
        self.root.geometry("900x700")
        self.root.resizable(False, False)

        # Servicios
        self.restaurante = Restaurante()

        self.archivo = ArchivoServicio(
            "datos/productos.json"
        )

        # Cargar productos
        productos_cargados = self.archivo.cargar_productos()
        self.restaurante.cargar_productos(productos_cargados)

        # Cargar usuarios
        usuarios_cargados = self.archivo.cargar_usuarios()
        self.restaurante.cargar_usuarios(usuarios_cargados)

        # Cargar ventas
        ventas_cargadas = self.archivo.cargar_ventas()
        self.restaurante.cargar_ventas(ventas_cargadas)

        # Mostrar login
        self.mostrar_login()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def guardar_productos(self):
        self.archivo.guardar_productos(
            self.restaurante.listar_productos()
        )

    def guardar_ventas(self):
        self.archivo.guardar_ventas(
            self.restaurante.listar_ventas()
        )

    def mostrar_login(self):
        self.limpiar_ventana()

        LoginView(
            self.root,
            self.restaurante,
            self.mostrar_principal
        )

    def mostrar_principal(self):
        self.limpiar_ventana()

        MainView(
            self.root,
            self.restaurante,
            self.mostrar_login,
            self.guardar_productos,
            self.guardar_ventas
        )


def main():
    root = tk.Tk()

    Aplicacion(root)

    root.mainloop()


if __name__ == "__main__":
    main()