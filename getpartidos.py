from flask import Blueprint, request, jsonify
from models import Partido

getpartidos_bp = Blueprint("getpartidos", __name__)

@getpartidos_bp.route("/partidos", methods=["GET"])
def listar_partidos():

    equipo = request.args.get("equipo")
    fecha = request.args.get("fecha")
    fase = request.args.get("fase")
    limit = request.args.get("limit", type=int)
    offset = request.args.get("offset", type=int, default=0)

    query = Partido.query

    if equipo:
        query = query.filter(
            (Partido.equipo_local.ilike(f"%{equipo}%")) |
            (Partido.equipo_visitante.ilike(f"%{equipo}%"))
        )

    if fecha:
        query = query.filter(Partido.fecha == fecha)

    if fase:
        query = query.filter(Partido.fase == fase)

    if limit is not None:
        partidos = query.offset(offset).limit(limit).all()
    else:
        partidos = query.all()

    resultado = []
    for p in partidos:
        resultado.append({
            "id": p.id,
            "equipo_local": p.equipo_local,
            "equipo_visitante": p.equipo_visitante,
            "fecha": str(p.fecha),
            "fase": p.fase
        })

    return jsonify(resultado), 200