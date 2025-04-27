from tabla_usuarios import usuarios,db

# Eliminar un registro
usuarios.delete(nombre='Ana')# type: ignore

db.close()