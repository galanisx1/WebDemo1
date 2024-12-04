from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Asegúrate de que Flask escuche en el puerto 5000 en la dirección 0.0.0.0
    app.run(host="0.0.0.0", port=5000)
