from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.user_input import UserInput
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()

# Human Readable
@app.get('/')
def home():
    return {'message':'Insureance Premium Company API'}

# machine readable
@app.get('/health')
def health_check():
    return{
        'status': 'OK',
        'version': MODEL_VERSION
    }
        
@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_grp,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    # Try Catch
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))


    
