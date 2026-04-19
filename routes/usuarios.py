from flask import Blueprint, request, jsonify
from models import Usuario
from database import db

usuarios_bp = Blueprint("usuarios", __name__)

# ---------------- POST ----------------
@usuarios_bp.route("/usuarios", methods=["POST"])
def crear_usuario():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    if "nombre" not in data or "email" not in data:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    if "@" not in data["email"]:
        return jsonify({"error": "Email inválido"}), 400

    nuevo_usuario = Usuario(
        nombre=data["nombre"],
        email=data["email"],
        puntos=data.get("puntos", 0)
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        "mensaje": "Usuario creado",
        "usuario": {
            "id": nuevo_usuario.id,
            "nombre": nuevo_usuario.nombre,
            "email": nuevo_usuario.email,
            "puntos": nuevo_usuario.puntos
        }
    }), 201

# ---------------- GET TODOS ----------------
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

# ---------------- GET BY ID ----------------
@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def detalle_usuario(id):

    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "puntos": usuario.puntos
    }), 200

# ---------------- PUT ----------------
@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def reemplazar_usuario(id):

    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    if "nombre" not in data or "email" not in data:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    usuario.nombre = data["nombre"]
    usuario.email = data["email"]

    if "puntos" in data:
        usuario.puntos = data["puntos"]

    db.session.commit()

    return jsonify({"mensaje": "Usuario actualizado"}), 200

# ---------------- PATCH ----------------
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

# ---------------- DELETE ----------------
@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):

    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario eliminado"}), 200

@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario_put(id):
    try:
        data = request.get_json()

        if not data or 'nombre' not in data or 'email' not in data:
            return jsonify({"error": "Faltan los campos requeridos: nombre y/o email"}), 400

        nombre = data.get('nombre')
        email = data.get('email')

        if not isinstance(nombre, str) or not isinstance(email, str):
            return jsonify({"error": "El nombre y el email deben ser cadenas de texto"}), 400

        if len(nombre.strip()) == 0 or len(email.strip()) == 0:
            return jsonify({"error": "El nombre y el email no pueden estar vacíos"}), 400

        #exito=actualizar_usuario_en_db
        exito = True 

        if not exito:
            return jsonify({"error": f"No se encontró el usuario con ID {id}"}), 404

        return jsonify({
            "mensaje": "Usuario actualizado con éxito",
            "usuario": {
                "id": id,
                "nombre": nombre,
                "email": email
            }
        }), 200

    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500