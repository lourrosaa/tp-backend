from flask import Blueprint, request, jsonify
from models import Usuario
from database import db

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios/<int:id>", methods=["PATCH"])
def actualizar_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    # actualiza solo lo que venga
    if "nombre" in data:
        usuario.nombre = data["nombre"]

    if "email" in data:
        usuario.email = data["email"]

    if "puntos" in data:
        usuario.puntos = data["puntos"]

    db.session.commit()

    return jsonify({"mensaje": "Usuario actualizado"}), 200
