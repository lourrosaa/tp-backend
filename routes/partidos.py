from flask import Blueprint, request, jsonify
from models import Partido
from database import db

partidos_bp = Blueprint("partidos", __name__)

@partidos_bp.route("/partidos/<int:id>", methods=["PATCH"])
def actualizar_partido(id):
    # Buscar partido
    partido = Partido.query.get(id)

    if not partido:
        return jsonify({"error": "Partido no encontrado"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    # Campos permitidos para actualizar
    campos_permitidos = [
        "equipo_local",
        "equipo_visitante",
        "goles_local",
        "goles_visitante"
    ]

    # Actualizar solo lo permitido
    for campo in campos_permitidos:
        if campo in data:
            setattr(partido, campo, data[campo])

    # Guardar cambios
    db.session.commit()

    return jsonify({
        "mensaje": "Partido actualizado correctamente",
        "partido": {
            "id": partido.id,
            "equipo_local": partido.equipo_local,
            "equipo_visitante": partido.equipo_visitante,
            "goles_local": partido.goles_local,
            "goles_visitante": partido.goles_visitante
        }
    }), 200