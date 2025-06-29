

from pydantic import BaseModel, EmailStr, Field ,field_validator
from typing import List ,Dict, Optional, Annotated
## Feild is used to validate ur custome data
## we can also attach metadata in Feild function

##step-1
class Patients(BaseModel):
    name:str
    age:int
    weight: float
    email:EmailStr
    married: Optional[bool]=None 
    allergies:List[str] 
    contact_detail: Dict[str,str]

    ## we are creating a custome validator in email
    @field_validator("email",mode="after") ## mode="after" ka matlab hai ki jo value meko mil rhi hai agter type conversion milegi ,default value after hi rhta hai
    @classmethod
    def validate_email(cls,value):
        valid_domain=["hdfc.com","icici.com"]
        domain_name=value.split("@")[-1]
        if domain_name not in valid_domain:
            raise ValueError("Email is not in domain")
        else:
            return value


## step-2
patients_info={"name":"Anshuman",
            "age":"30",
            "weight":67.3,
            "email":"abc@gmail.com" , ## This will raise value error becaudse of the constraints that er have given 
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