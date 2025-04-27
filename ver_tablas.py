from connect import db

tablas_existentes = db.tables

print(tablas_existentes)

db.close()