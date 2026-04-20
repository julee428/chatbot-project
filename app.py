print("Starting Flask App...")

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    return jsonify({"response": "You said: " + user_message})

if __name__ == "__main__":
    app.run(debug=True, port=5000)