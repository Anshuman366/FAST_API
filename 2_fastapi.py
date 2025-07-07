from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from fastapi import FastAPI,Path,HTTPException ,Query
from fastapi.responses import JSONResponse
import json
app=FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="Id of the patient")]
    name:Annotated[str,Field(...,description="Name of the patients")]
    city:Annotated[str,Field(...,description="City of the patient")]
    age:Annotated[int,Field(...,gt=0,lt=120,description="Age of the patient")]
    gender:Annotated[Literal["male","female","others"],Field(...,description="gender of the patient")]
    height:Annotated[float,Field(...,gt=0,description="Height of the patient")]
    weight:Annotated[float,Field(...,gt=0,description="weight of the patient")]

    @computed_field
    @property
    def bmi(self)->str:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return "Underweight"
        if self.bmi>18.5 and self.bmi<25:
            return "Normal" 
        else:
            return "obese"
    



def load_data():
    with open("patients.json","r") as file:
        data=json.load(file)
    return data
def write_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {"message":"Patients management Api"}

@app.get("/about")
def about():
    return {"message":"Functionl Api to manage patients records"}

@app.get("/view")
def view_data():
    data=load_data()
    return data

@app.get("/patients/{patient_id}")
def view_patients(patient_id:str=Path(...,description="Please give patient Id")):
    ## here path function will  actully used to give description avout thet patient-Id parameter
    ## ... iska matlab hai ki ye mendatorry hai
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail="Patient not found")
        
@app.get("/sort")
def sort_patients(sort_by:str=Query(...,description="Sort  on the basis of ?"),order:str=Query("asc",description="Ascending or descending")):
    valid_feild=["weight","height","bmi"]
    if sort_by not in valid_feild:
        raise HTTPException(status_code=404,detail=f"Invalid feild select from {valid_feild}")
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=404,detail=f"Invalid order provided please select asc or desc")
    data=load_data()

    sort_order=True if order=="asc" else False
    
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data

@app.post("/create")
def create_patient(patient:Patient):
    ## load existing date
    data=load_data()
    ## check if the patient already exist
    if patient.id  in data:
        raise HTTPException(status_code=400,detail='patient already exist')

    ## Add new patient to the database
    data[patient.id]=patient.model_dump(exclude=["id"]) ## Patient.model_dump() will convert the pydantic object to the json

    write_data(data)

    return JSONResponse(status_code=200,content={"message": "Patient created sucessfully"})