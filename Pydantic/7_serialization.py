from pydantic import BaseModel, EmailStr, Field ,field_validator,model_validator,computed_field
from typing import List ,Dict, Optional, Annotated

class Address(BaseModel):
    city:str
    state:str
    pin:str



##step-1
class Patients(BaseModel):
    name:str
    address: Address

address={"city":"Gurgaon","state":"Haryana","pin":"678686"}

Address1=Address(**address)

patient_dict={"name":"Anshuman","address":Address1}

patient1=Patients(**patient_dict)

print(patient1)

temp=patient1.model_dump() ## this will dump the model into dictionary

print(type(temp))