from flask import Blueprint, request, jsonify
from models import Usuario
from database import db

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = Usuario.query.all()
    resultado = []
    for u in usuarios:
        resultado.append({
            "id": u.id,
            "nombre": u.nombre,
            "email": u.email,
            "puntos": u.puntos
        })
    return jsonify(resultado), 200

@usuarios_bp.route("/usuarios", methods=["POST"])
def crear_usuario():
    data = request.get_json()

    if not data or not data.get("nombre") or not data.get("email"):
        return jsonify({"error": "Faltan datos obligatorios (nombre, email)"}), 400

    nuevo_user = Usuario(
        nombre=data["nombre"],
        email=data["email"]
    )

    db.session.add(nuevo_user)
    db.session.commit()

    return jsonify({"mensaje": "Usuario creado"}), 201

@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def detalle_usuarios(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "puntos": usuario.puntos
    }), 200

@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def reemplazar_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    data = request.get_json()

    if not data or "nombre" not in data or "email" not in data:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    usuario.nombre = data["nombre"]
    usuario.email = data["email"]
    if "puntos" in data:
        usuario.puntos = data["puntos"]

    db.session.commit()

    return jsonify({
        "mensaje": "Usuario reemplazado",
        "usuario": {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "puntos": usuario.puntos
        }
    }), 200

@usuarios_bp.route("/usuarios/<int:id>", methods=["PATCH"])
def actualizar_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    if "nombre" in data:
        usuario.nombre = data["nombre"]

    if "email" in data:
        usuario.email = data["email"]

    if "puntos" in data:
        usuario.puntos = data["puntos"]

    db.session.commit()

    return jsonify({"mensaje": "Usuario actualizado"}), 200

@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuarios(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
