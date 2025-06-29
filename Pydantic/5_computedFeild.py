
 ## what if u want to combine 2 feilds and do the data validation then in this case we use Model Validation

from pydantic import BaseModel, EmailStr, Field ,field_validator,model_validator,computed_field
from typing import List ,Dict, Optional, Annotated


##step-1
class Patients(BaseModel):
    name:str
    age:int
    weight: float
    height:float
    email:EmailStr
    married: Optional[bool]=None 
    allergies:List[str] 
    contact_detail: Dict[str,str]

    
    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=self.weight/self.height**2
        return bmi
## step-2
patients_info={"name":"Anshuman",
            "age":"20",
            "weight":67.3,
            "height":20.0,
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
    print("Bmi",patient.calculate_bmi)


    print("inserted in database1")

insert_patient_data(patient1)