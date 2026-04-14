from flask import Flask
from routes.partidos import partidos_bp
from routes.usuarios import usuarios_bp
from database import db

app = Flask(__name__)

# CONFIG BASE DE DATOS
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def home():
    return "API funcionando"

# registrar blueprints
app.register_blueprint(partidos_bp)
app.register_blueprint(usuarios_bp)

if __name__ == "__main__":
    app.run(debug=True)