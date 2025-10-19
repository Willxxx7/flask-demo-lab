from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "CHANGE_THIS_TO_A_SECRET"  # Update this for production
app.config['DEBUG'] = False  # Ensure production mode

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    # This endpoint is used by Render to check container health
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # Bind to all interfaces so the container can be reached from Render
    app.run(host="0.0.0.0", port=5000)

