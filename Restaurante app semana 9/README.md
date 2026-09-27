## Nombre del estudiante

Adriana Marcela Portilla Guaman
# Restaurante App

## Descripción

Restaurante App es un sistema desarrollado en Python utilizando Programación Orientada a Objetos (POO). El proyecto permite gestionar productos, usuarios y ventas mediante una interfaz gráfica desarrollada con Tkinter.

El proyecto ha ido evolucionando durante las diferentes semanas de trabajo. En esta etapa se incorporó el manejo de eventos en la interfaz gráfica mediante botones, callbacks y el parámetro `command=`.

## Semana 15 - Manejo de eventos

En esta semana se trabajó con los conceptos fundamentales del manejo de eventos en interfaces gráficas.

El objetivo principal fue conectar las acciones realizadas por el usuario en la interfaz con los métodos correspondientes del sistema.

Por ejemplo, cuando el usuario presiona el botón **Registrar venta**, se ejecuta un callback mediante `command=`. Este callback obtiene los datos seleccionados en la interfaz y los envía al servicio del restaurante para realizar la operación.

El flujo utilizado es:

Usuario → Botón → `command=` → Callback → Servicio → Persistencia → Actualización de la interfaz

## Funcionalidades

El sistema cuenta con las siguientes funcionalidades:

- Inicio de sesión de usuarios.
- Visualización del menú principal.
- Registro de productos.
- Registro de usuarios.
- Registro de ventas.
- Selección de usuarios mediante `Combobox`.
- Selección de productos mediante `Combobox`.
- Ingreso de la cantidad de productos vendidos.
- Visualización de las ventas registradas.
- Actualización de la tabla de ventas después de registrar una venta.
- Guardado de la información en archivos JSON.
- Validaciones realizadas desde las clases y servicios del sistema.

## Manejo de eventos

Para el manejo de eventos se utilizan principalmente botones de Tkinter con el parámetro `command=`.

Algunos ejemplos utilizados en el proyecto son:

```python
tk.Button(
    self.frame,
    text="Registrar venta",
    command=self.registrar_venta
)