from flask import Blueprint, request, jsonify
from models import Partido
from database import db

partidos_bp = Blueprint("partidos", __name__)

@partidos_bp.route("/partidos", methods=["GET"])
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
            "fase": p.fase,
            "goles_local": p.goles_local,
            "goles_visitante": p.goles_visitante
        })

    return jsonify(resultado), 200

@partidos_bp.route("/partidos", methods=["POST"])
def crear_partido():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    campos_obligatorios = ["equipo_local", "equipo_visitante", "fecha", "fase"]

    for campo in campos_obligatorios:
        if campo not in data:
            return jsonify({"error": f"Falta el campo {campo}"}), 400

    nuevo_partido = Partido(
        equipo_local=data["equipo_local"],
        equipo_visitante=data["equipo_visitante"],
        fecha=data["fecha"],
        fase=data["fase"]
    )

    db.session.add(nuevo_partido)
    db.session.commit()

    return jsonify({
        "mensaje": "Partido creado correctamente",
        "partido": {
            "id": nuevo_partido.id,
            "equipo_local": nuevo_partido.equipo_local,
            "equipo_visitante": nuevo_partido.equipo_visitante,
            "fecha": str(nuevo_partido.fecha),
            "fase": nuevo_partido.fase
        }
    }), 201

@partidos_bp.route("/partidos/<int:id>", methods=["GET"])
def detalle_partido(id):
    partido = Partido.query.get(id)

    if not partido:
        return jsonify({"error": "Partido no encontrado"}), 404

    return jsonify({
        "id": partido.id,
        "equipo_local": partido.equipo_local,
        "equipo_visitante": partido.equipo_visitante,
        "fecha": str(partido.fecha),
        "fase": partido.fase,
        "goles_local": partido.goles_local,
        "goles_visitante": partido.goles_visitante
    }), 200

@partidos_bp.route("/partidos/<int:id>", methods=["PATCH"])
def actualizar_partido(id):
    partido = Partido.query.get(id)

    if not partido:
        return jsonify({"error": "Partido no encontrado"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    campos_permitidos = [
        "equipo_local",
        "equipo_visitante",
        "goles_local",
        "goles_visitante",
        "fecha",
        "fase"
    ]

    for campo in campos_permitidos:
        if campo in data:
            setattr(partido, campo, data[campo])

    db.session.commit()

    return jsonify({
        "mensaje": "Partido actualizado correctamente",
        "partido": {
            "id": partido.id,
            "equipo_local": partido.equipo_local,
            "equipo_visitante": partido.equipo_visitante,
            "goles_local": partido.goles_local,
            "goles_visitante": partido.goles_visitante
        }
    }), 200

@partidos_bp.route('/partidos/<int:id>/resultado', methods=['PUT'])
def actualizar_resultado_partido(id):
    partido = Partido.query.get(id)

    if not partido:
        return jsonify({"error": f"No se encontró el partido con ID {id}"}), 404

    data = request.get_json()
    
    if not data or 'goles_local' not in data or 'goles_visitante' not in data:
        return jsonify({"error": "Faltan los campos requeridos: goles_local y/o goles_visitante"}), 400
        
    goles_local = data.get('goles_local')
    goles_visitante = data.get('goles_visitante')
    
    if not isinstance(goles_local, int) or not isinstance(goles_visitante, int):
        return jsonify({"error": "Los goles deben ser valores numéricos enteros"}), 400
        
    if goles_local < 0 or goles_visitante < 0:
        return jsonify({"error": "Los goles no pueden ser negativos"}), 400

    partido.goles_local = goles_local
    partido.goles_visitante = goles_visitante

    db.session.commit()
        
    return jsonify({
        "mensaje": "Resultado actualizado con éxito",
        "resultado_cargado": {
            "goles_local": goles_local,
            "goles_visitante": goles_visitante
        }
    }), 200

@partidos_bp.route("/partidos/<int:id>", methods=["DELETE"])
def eliminar_partido(id):
    partido = Partido.query.get(id)

    if not partido:
        return jsonify({"error": "Partido no encontrado"}), 404
        
    db.session.delete(partido)
    db.session.commit()

    return jsonify({
        "mensaje": "Partido eliminado correctamente"
    }), 200
