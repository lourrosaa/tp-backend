from flask import Blueprint, request, jsonify
from models import Partido
from database import db

partidos_bp = Blueprint("partidos", __name__)

@partidos_bp.route("/partidos", methods=["POST"])
def crear_partido():
    data = request.get_json()  #Lee lo que manda el cliente

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    campos_obligatorios = ["equipo_local", "equipo_visitante", "fecha", "fase"]

    for campo in campos_obligatorios:
        if campo not in data:
            return jsonify({"error": f"Falta el campo {campo}"}), 400

    nuevo_partido = Partido(
        equipo_local=data["equipo_local"],
        equipo_visitante=data["equipo_visitante"],
        fecha=data["fecha"],
        fase=data["fase"]
    )


    db.session.add(nuevo_partido)  #Lo prepara para guardarlo en la base de datos
    db.session.commit()  #Lo guarda 


    return jsonify({
        "mensaje": "Partido creado correctamente",
        "partido": {
            "id": nuevo_partido.id,
            "equipo_local": nuevo_partido.equipo_local,
            "equipo_visitante": nuevo_partido.equipo_visitante,
            "fecha": nuevo_partido.fecha,
            "fase": nuevo_partido.fase
        }
    }), 201