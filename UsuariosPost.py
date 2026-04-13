from flask import Blueprint, request, jsonify
from models import Usuario
from database import db

usuarios_crear_bp = Blueprint("crear usuarios", __name__)

@usuarios_crear_bp.route("/usuarios", methods=["POST"])
def crear_usuario():
    data = request.get_json()  #Lee lo que manda el cliente

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    campos_obligatorios = ["nombre", "email"]

    for campo in campos_obligatorios:
        if campo not in data:
            return jsonify({"error": f"Falta el campo {campo}"}), 400
    
    if "@" not in data["email"]:  #Valida el email
                return jsonify({"error":"Email invalido"}), 400

    nuevo_usuario = Usuario(
        nombre=data["nombre"],
        email=data["email"]
    )


    db.session.add(nuevo_usuario)  #Lo prepara para guardarlo en la base de datos
    db.session.commit()  #Lo guarda 


    return jsonify({
        "mensaje": "Usuario creado correctamente",
        "usuario": {
            "id": nuevo_usuario.id,
            "nombre": nuevo_usuario.nombre,
            "email": nuevo_usuario.email
        }
    }), 201