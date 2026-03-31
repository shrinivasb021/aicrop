from flask import Flask, render_template, request, jsonify
import os
import random

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

diseases = [
    "Tomato Early Blight",
    "Potato Late Blight",
    "Corn Healthy",
    "Leaf Spot Disease"
]

treatments = {
    "Tomato Early Blight":
    "Use fungicide and remove infected leaves",

    "Potato Late Blight":
    "Apply copper-based fungicide",

    "Corn Healthy":
    "No treatment needed",

    "Leaf Spot Disease":
    "Use neem oil spray"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    disease = random.choice(diseases)

    confidence = random.randint(85, 99)

    return jsonify({

        "disease": disease,

        "confidence": confidence,

        "treatment": treatments[disease]

    })


if __name__ == "__main__":
    app.run(debug=True)
