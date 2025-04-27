from tabla_usuarios import usuarios,db

# Consultar todos los registros
_usuarios = usuarios.all()# type: ignore
for usuario in _usuarios:
    print(usuario['nombre'], usuario['edad'])
    
_usuarios_list = usuarios.all() #type:ignore
usuarios_list = list(_usuarios_list)
print(usuarios_list)

db.close()