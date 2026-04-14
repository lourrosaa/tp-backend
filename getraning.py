from flask import Blueprint, request, jsonify
from models import Usuario

ranking_bp = Blueprint("ranking", __name__)

@ranking_bp.route("/ranking", methods=["GET"])
def obtener_ranking():
    limit = request.args.get("limit", type=int)
    offset = request.args.get("offset", type=int, default=0)
    usuarios = Usuario.query.all()

    ranking = []
    for u in usuarios:
        ranking.append({
            "id_usuario": u.id,
            "puntos": 0
        })

    ranking.sort(key=lambda x: x["puntos"], reverse=True)

    if limit is not None:
        ranking = ranking[offset:offset + limit]

    return jsonify(ranking), 200