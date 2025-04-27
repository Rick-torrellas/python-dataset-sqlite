from tabla_usuarios import usuarios,db

# Actualizar un registro
# buscara por el campo nombre y actualizara edad, en este caso busca nombre = Ana
usuarios.update({# type: ignore
    'nombre': 'Ana',
    'edad': 122  # Actualizar edad
}, ['nombre'])  # Buscar por el campo 'nombre'

db.close()