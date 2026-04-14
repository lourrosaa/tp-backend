<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
=======
# database.py
# Aquí irá la lógica de conexión a la base de datos (por ejemplo, SQLite, PostgreSQL, etc.)
import csv
import os

ARCHIVO_CSV = "partidos.csv"
ARCHIVO_USUARIOS = "usuarios.csv"

CAMPOS_USUARIOS = [
    "id",
    "nombre",
    "email"
]

CAMPOS = [
    "id",
    "equipo_local",
    "equipo_visitante",
    "fecha",
    "fase",
    "goles_local",
    "goles_visitante"
]


def inicializar_archivo():
    existe = os.path.exists(ARCHIVO_CSV)

    if not existe:
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CAMPOS)
            writer.writeheader()


def obtener_todos():
    inicializar_archivo()

    partidos = []

    with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for fila in reader:
            # convertir id
            fila_id = int(fila["id"])
            fila["id"] = fila_id

            # goles_local
            if fila["goles_local"] != "":
                goles_local = int(fila["goles_local"])
            else:
                goles_local = None
            fila["goles_local"] = goles_local

            # goles_visitante
            if fila["goles_visitante"] != "":
                goles_visitante = int(fila["goles_visitante"])
            else:
                goles_visitante = None
            fila["goles_visitante"] = goles_visitante

            partidos.append(fila)

    return partidos


def guardar_todos(partidos):
    with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CAMPOS)

        writer.writeheader()

        for partido in partidos:
            writer.writerow(partido)

#USUARIOS------------------------
def inicializar_usuarios():
    existe = os.path.exists(ARCHIVO_USUARIOS)

    if not existe:
        with open(ARCHIVO_USUARIOS, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CAMPOS_USUARIOS)
            writer.writeheader()

def obtener_usuarios():
    inicializar_usuarios()

    usuarios = []

    with open(ARCHIVO_USUARIOS, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for fila in reader:
            fila["id"] = int(fila["id"])
            usuarios.append(fila)

    return usuarios

def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CAMPOS_USUARIOS)

        writer.writeheader()

        for usuario in usuarios:
            writer.writerow(usuario)
>>>>>>> origin/rama-de-lara
