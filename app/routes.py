from flask import Blueprint, render_template, request, jsonify
import pickle
import numpy as np
import os

main = Blueprint("main", __name__)
model_path = os.path.join("Brains", "random_forest_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

@main.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        try:
            input_data = [float(request.form.get(f"feature{i}")) for i in range(1, 5)]
            pred = model.predict([input_data])
            prediction = round(pred[0], 2)
        except Exception as e:
            prediction = f"Error: {str(e)}"
    return render_template("index.html", prediction=prediction)
