from flask import Blueprint, jsonify
from models import Usuario
from database import db

usuarios_id_bp = Blueprint("usuarios_id", __name__)


@usuarios_id_bp.route("/usuarios/<int:id>", methods=["GET"])
def detalle_usuario(id):
    usuario = db.session.get(Usuario, id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email
    }), 200

@usuarios_id_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    usuario = db.session.get(Usuario, id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    try:
        db.session.delete(usuario)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el usuario"}), 500

    return jsonify({
        "mensaje": "Usuario eliminado correctamente"
    }), 200