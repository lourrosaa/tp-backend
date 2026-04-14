from flask import Blueprint, request, jsonify
from models import Usuario

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    limit = request.args.get("limit", type=int)
    offset = request.args.get("offset", type=int, default=0)
    query = Usuario.query

    if limit is not None:
        usuarios = query.offset(offset).limit(limit).all()
    else:
        usuarios = query.all()

    resultado = []
    for u in usuarios:
        resultado.append({
            "id": u.id,
            "nombre": u.nombre,
            "email": u.email
        })

    return jsonify(resultado), 200