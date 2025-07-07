from fastapi import FastAPI,Path,HTTPException ,Query
import json
app=FastAPI()

def load_data():
    with open("patients.json","r") as file:
        data=json.load(file)
    return data

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
