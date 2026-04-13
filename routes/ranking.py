from flask import Blueprint, jsonify
from models import Usuario

ranking_bp = Blueprint("ranking", __name__)

@ranking_bp.route("/ranking", methods=["GET"])
def obtener_ranking():
    usuarios = Usuario.query.order_by(Usuario.puntos.desc()).all()

    resultado = []

    for u in usuarios:
        resultado.append({
            "id": u.id,
            "nombre": u.nombre,
            "puntos": u.puntos
        })

    return jsonify(resultado), 200
