from tabla_usuarios import db,usuarios

carlos = usuarios.find(nombre="Carlos") # type:ignore

# transformar a una lista
carlos_lista = list(carlos)

for carlistos in carlos_lista:
    print(carlistos["nombre"])

print(carlos_lista)

db.close()