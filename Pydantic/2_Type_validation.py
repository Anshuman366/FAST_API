

from pydantic import BaseModel, EmailStr, Field 
from typing import List ,Dict, Optional, Annotated
## Feild is used to validate ur custome data
## we can also attach metadata in Feild function

##step-1
class Patients(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Name of the patients",description="Give the name of the patients")]
    age:int
    weight: float
    email:EmailStr
    married: Optional[bool]=None ## this feild is now optional with default value as None
    allergies:List[str] ## Hum list use ni kr sakte the because wo sirf ye validate krta ki allergies list type ka ho,
                        ## wo ye ni validate krta ki jo uske andar data ja rha hao wo bhi string ka ho
                        ## so for 2 level validation we use List , same for Dict also
    contact_detail: Dict[str,str]

## step-2
patients_info={"name":"Anshuman",
            "age":"30",
            "weight":67.3,
            "email":"abc@gmail.com" ,## Now of this follow correct pattern then only it will work otherwise error dega
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