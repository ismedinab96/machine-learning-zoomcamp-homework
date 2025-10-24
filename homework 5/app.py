from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()
with open ("pipeline_v1.bin","rb") as f_in:
    pipeline = pickle.load(f_in)

class Customer(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.post("/predict")
def predict (client:Customer):
    record = client.model_dump()
    prob = pipeline.predict_proba([record])[0][1]
    return {"prob" : round(float(prob),3)} 
