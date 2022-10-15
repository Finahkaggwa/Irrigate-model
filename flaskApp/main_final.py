from flask import Flask
from flask import request
# Pickle package
import pickle
# from ML.test_model import irrigate_or_not_irrigate

app = Flask(__name__)


# load the model from disk
filename = 'irrigation_final_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def irrigate_or_not_irrigate(Type, Moisture):
    if(loaded_model.predict([[Type, Moisture]]))==0:
        return 'Irrigate'
    else:
        return 'Not irrigate'


@app.route("/")
def home_view():
        return {
            "api_state": "Up and running"
        }

# 
@app.post('/api/predict')
def predict():
        # print(request.form.get('soil_moisture'))
        Type = request.form.get('Type')
        Moisture = request.form.get('Moisture')
        predictions = irrigate_or_not_irrigate(int(Type, Moisture))
        return {
            "predictions": predictions
        }