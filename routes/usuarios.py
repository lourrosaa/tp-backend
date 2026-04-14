from flask import Blueprint, request, jsonify
from models import Usuarios
from database import db
from database import obtener_usuarios, guardar_usuarios

usuarios_id_bp = Blueprint("usuarios_id",__name__)

@usuarios_id_bp.route("/usuarios/<int:id>", methods=["GET"])
def detalle_usuarios(id):
    #busco el partido en db
    Usuarios = obtener_usuarios()
    usuario_encontrado = None

    for usuario in Usuarios:
        if usuario["id"] == id:
            usuario_encontrado = usuario

    if usuario_encontrado is None:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify(usuario_encontrado), 200
    
    
@usuarios_id_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuarios(id):
    Usuarios = obtener_usuarios()

    nuevos_usuarios = []
    encontrado = False

    for usuario in Usuarios:
        if usuario["id"] == id:
            encontrado = True
        else:
            nuevos_usuarios.append(usuario)

    if not encontrado:
        return jsonify({"error": "Usuario no encontrado"}), 404

    guardar_usuarios(nuevos_usuarios)

    return jsonify({
        "mensaje": "Usuario eliminado correctamente"
    }), 200