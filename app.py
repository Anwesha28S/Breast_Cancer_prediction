print("=== RUNNING NEW BREAST CANCER APP ===")
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask,jsonify,request,render_template

app=Flask(__name__)

rf_model=pickle.load(open("models/rf_final1.pkl","rb"))
standard_scaler=pickle.load(open("models/sc_final1.pkl","rb"))
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/predictdata",methods=["GET","POST"])
def predict_data():
    if request.method=="POST":
        # Fetch data from form
        Cpm = float(request.form['concave points_mean'])
        Cpw = float(request.form['concave points_worst'])
        rw = float(request.form['radius_worst'])
        aw = float(request.form['area_worst'])
        pw = float(request.form['perimeter_worst'])
        new_data=standard_scaler.transform([[Cpm,Cpw,rw,aw,pw]])
        prediction = rf_model.predict(new_data)[0]
        result = "Malignant" if prediction == 1 else "Benign"
        return render_template(
            "index.html",
            prediction=result)
    else:
        return render_template("index.html",results=None)
    
if(__name__)=="__main__":
    app.run(host="0.0.0.0",debug=True)