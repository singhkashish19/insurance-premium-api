import pandas as pd
import pickle

# Import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.O' 

def predict_output(user_input : dict):

    input_df = pd.DataFrame([user_input])
    
    output = model.predict(input_df)[0]
    return output
