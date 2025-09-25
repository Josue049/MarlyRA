from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/model')
def model():
    # Sirve el modelo desde la carpeta static
    return send_from_directory('static', 'bracelet.glb')

if __name__ == "__main__":
    # host="0.0.0.0" => visible en la red local
    app.run(host="0.0.0.0", port=5000, debug=True)

