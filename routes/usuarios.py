from flask import Blueprint, request, jsonify
from models import Usuario
from database import db

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def reemplazar_usuario(id):

    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    data = request.get_json()

    if not data or "nombre" not in data:
        return jsonify({"error": "Falta nombre"}), 400

    usuario.nombre = data["nombre"]

    db.session.commit()

    return jsonify({
        "mensaje": "Usuario actualizado",
        "usuario": {
            "id": usuario.id,
            "nombre": usuario.nombre
        }
    }), 200