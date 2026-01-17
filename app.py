from flask import Flask, request, jsonify
from agents.coordinator import coordinator

app = Flask(__name__)

@app.route("/cds", methods=["POST"])
def cds():
    data = request.json
    result = coordinator(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
