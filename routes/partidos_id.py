from flask import Blueprint, request, jsonify
from models import Partido
from database import db

partidos_id_bp = Blueprint("partidos_id", __name__)

@partidos_id_bp.route("/partidos/<int:id>", methods=["GET"])
def detalle_partido(id):
    #busco el partido en db
    partido = Partido.query.get(id)

    if not partido:
        return jsonify({"error": "Partido no encontrado"}), 404
    
    return jsonify({
        "id":partido.id,
        "equipo_local":partido.equipo_local,
        "equipo_visitante":partido.equipo_visitante,
        "goles_local":partido.goles_local,
        "goles_visitante":partido.goles_visitante,
    }), 200
    
@partidos_id_bp.route("/partidos/<int:id>", methods=["DELETE"])
def eliminar_partido(id):
    partido = Partido.query.get(id)

    if not partido:
        return jsonify({"error": "Partido no encontrado"}), 404

    # Eliminar de la DB
    db.session.delete(partido)
    db.session.commit()

    return jsonify({
        "mensaje": "Partido eliminado correctamente"
    }), 200