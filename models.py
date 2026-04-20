# models.py
# Aquí irán las definiciones de los modelos de datos (por ejemplo, con SQLAlchemy o clases estándar)

from database import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    puntos = db.Column(db.Integer, default=0)

class Partido(db.Model):
    __tablename__ = 'partidos'
    id = db.Column(db.Integer, primary_key=True)
    equipo_local = db.Column(db.String(100), nullable=False)
    equipo_visitante = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(50), nullable=False)
    fase = db.Column(db.String(50), nullable=False)
    goles_local = db.Column(db.Integer, nullable=True)
    goles_visitante = db.Column(db.Integer, nullable=True)

class Prediccion(db.Model):
    __tablename__ = 'predicciones'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    partido_id = db.Column(db.Integer, db.ForeignKey('partidos.id'), nullable=False)
    goles_local = db.Column(db.Integer, nullable=False)
    goles_visitante = db.Column(db.Integer, nullable=False)