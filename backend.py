from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("randomforest_model.pkl")
FEATURES = list(model.feature_names_in_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_data = {f: data.get(f, 0) for f in FEATURES}

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)

    return jsonify({
        "predicted_price": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
