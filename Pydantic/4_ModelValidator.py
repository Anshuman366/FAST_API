
 ## what if u want to combine 2 feilds and do the data validation then in this case we use Model Validation

from pydantic import BaseModel, EmailStr, Field ,field_validator,model_validator
from typing import List ,Dict, Optional, Annotated


##step-1
class Patients(BaseModel):
    name:str
    age:int
    weight: float
    email:EmailStr
    married: Optional[bool]=None 
    allergies:List[str] 
    contact_detail: Dict[str,str]

    
    @field_validator("email",mode="after") 
    @classmethod
    def validate_email(cls,value):
        valid_domain=["hdfc.com","icici.com"]
        domain_name=value.split("@")[-1]
        if domain_name not in valid_domain:
            raise ValueError("Email is not in domain")
        else:
            return value

    @model_validator(mode="after")
    def validate_emergency_contact(cls,model):
        if model.age > 60 and "emergency" not in model.contact_detail:
            raise ValueError("Patient with age greater than 60 must have emergency contact")
        else:
            return model

## step-2
patients_info={"name":"Anshuman",
            "age":"90",
            "weight":67.3,
            "email":"abc@hdfc.com" , 
            "married":True,
            "allergies":["pollen","Dust"],
            "contact_detail":{
                "email":"abc#gmail.com",
                "phone":"4783264798"
                
            }} 

patient1=Patients(**patients_info)

## step-3
def insert_patient_data(patient:Patients):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)


    print("inserted in database1")

insert_patient_data(patient1)