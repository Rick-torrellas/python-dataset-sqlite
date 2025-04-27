from tabla_usuarios import usuarios,db

class Usuario:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def validar(self):
        if not isinstance(self.edad, int):
            raise ValueError("La edad debe ser un número")
        
_usuario: Usuario = Usuario(nombre="Ana", edad=20, email="ana@example.com")
_usuario.validar()
usuario: dict = _usuario.__dict__  # Convertir objeto a diccionario# Validar antes de insertar

# Insertar un registro (como un diccionario)
usuarios.insert(usuario) # type: ignore

db.close()