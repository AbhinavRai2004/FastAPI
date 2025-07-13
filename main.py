from fastapi import FastAPI,Path,HTTPException
import json

app = FastAPI()

def load_data():
    with open("patients.json",'r') as f:
        data = json.load(f)

    return data


@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}


@app.get('/get-patients')
def get_patients():
    data = load_data()
    return data


@app.get("/get-patients/{patient_id}")
def get_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code=404, detail="Patient not found")
