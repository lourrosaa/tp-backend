from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando 🚀"

if __name__ == "__main__":
    app.run(debug=True)


from routes.partidos import partidos_bp

app.register_blueprint(partidos_bp)