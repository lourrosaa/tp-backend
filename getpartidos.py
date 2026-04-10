from flask import Flask, jsonify, request

app = Flask(__name__)

partidos = [
    {"id": 1, "local": "Argentina", "visitante": "Brasil", "fecha": "2026-06-10", "fase": "grupos"},
    {"id": 2, "local": "Francia", "visitante": "Alemania", "fecha": "2026-06-11", "fase": "grupos"},
    {"id": 3, "local": "España", "visitante": "Italia", "fecha": "2026-06-12", "fase": "grupos"},
    {"id": 4, "local": "Argentina", "visitante": "Uruguay", "fecha": "2026-06-13", "fase": "eliminatorias"}
]

@app.route("/partidos", methods=["GET"])
def listar_partidos():
    equipo = request.args.get("equipo")
    fecha = request.args.get("fecha")
    fase = request.args.get("fase")
    limit = request.args.get("limit", type=int)
    offset = request.args.get("offset", type=int, default=0)

    resultado = partidos

    if equipo:
        resultado = [
            p for p in resultado
            if equipo.lower() in p["local"].lower()
            or equipo.lower() in p["visitante"].lower()
        ]

    if fecha:
        resultado = [p for p in resultado if p["fecha"] == fecha]

    if fase:
        resultado = [p for p in resultado if p["fase"] == fase]

    if limit is not None:
        resultado = resultado[offset:offset + limit]

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)