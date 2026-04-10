from flask import Flask
from routes.partidos_put import partidos_put_bp

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando"

# registrar antes de correr la app
app.register_blueprint(partidos_put_bp)

if __name__ == "_main_":
    app.run(debug=True)