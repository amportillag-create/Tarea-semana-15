class Usuario:
    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        contrasena: str = ""
    ) -> None:

        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    def __str__(self) -> str:
        return (
            f"ID: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "contrasena": self.contrasena
        }