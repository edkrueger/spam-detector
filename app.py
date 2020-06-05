from flask import Flask, request, jsonify
from joblib import load

clf = load("clf.joblib")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data_dict = request.get_json()

    text = [data_dict["text"]]

    return jsonify({
        "result": clf.predict(text)[0]
    })

if __name__ == "__main__":
    app.run()