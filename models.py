from database import db

class Partido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipo_local = db.Column(db.String(100), nullable=False)
    equipo_visitante = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(50), nullable=False)
    fase = db.Column(db.String(50), nullable=False)
    goles_local = db.Column(db.Integer)
    goles_visitante = db.Column(db.Integer)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)