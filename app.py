from flask import Flask, request, jsonify
from flask_cors import CORS
from services.predict import run_analysis

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        print(" AI REQUEST RECEIVED")

        #  DEBUG
        print("FILES:", request.files)
        print("FORM:", request.form)

        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        data = request.form.to_dict()

        result = run_analysis(file, data)

        return jsonify(result)

    except Exception as e:
        print("❌ AI ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5001)