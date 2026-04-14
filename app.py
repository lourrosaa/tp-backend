from flask import Flask
from config import Config
from database import db
from routes.partidos import partidos_bp
from routes.usuarios import usuarios_bp
from routes.ranking import ranking_bp

app = Flask(__name__)
app.register_blueprint(partidos_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(ranking_bp)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "API funcionando"

if __name__ == "__main__":
    app.run(debug=True)
