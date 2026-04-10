from flask import Blueprint, request, jsonify

partidos_put_bp = Blueprint("partidos_put", __name__)
# crea un blueprint para agrupar las rutas de este archivo

# mock de datos
partidos = {
    1: {
        "equipo_local": "Argentina",
        "equipo_visitante": "Brasil",
        "fecha": "2026-06-10",
        "fase": "Grupos"
    }
}

@partidos_put_bp.route("/partidos/<int:id>", methods=["PUT"])

def reemplazar_partido(id):

    if id not in partidos:
        return jsonify({"error": "Partido no encontrado"}), 404

    data = request.get_json()
    # obtiene los datos enviados en el body de la request

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400
    # valida que se hayan enviado datos

    campos_requeridos = [
        "equipo_local",
        "equipo_visitante",
        "fecha",
        "fase"
    ]

    for campo in campos_requeridos:
        if campo not in data:
            return jsonify({"error": f"Falta el campo {campo}"}), 400
    # recorre los campos obligatorios y si falta alguno da error

    partidos[id] = {
        "equipo_local": data["equipo_local"],
        "equipo_visitante": data["equipo_visitante"],
        "fecha": data["fecha"],
        "fase": data["fase"]
    }
    # reemplaza completamente el partido existente 

    return jsonify({
        "mensaje": "Partido reemplazado correctamente",
        "partido": partidos[id]
    }), 200