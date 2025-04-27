import dataset
import os

# Conectar a la base de datos (SQLite en este caso)
db = dataset.connect('sqlite:///db/prueba.db')

# Opción 2: Usando una ruta absoluta (más robusta en algunos casos)
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_db_absoluta = f'sqlite:///{os.path.join(directorio_actual, "db", "prueba.db")}'
db_absoluta = dataset.connect(ruta_db_absoluta)