

## PROBLEM-1
    ## in python there is no type validation , hum enforce ni kr
    #  pa rhe ki hamane function me kis type ka data aai
## PROBLEM-2
    ## hum kisi variable pe validation ni laga sakte , such that ki age greater than 0 hi hina chaiye

# Hum isko thik kr sakte hai agr hum manuaaly code me values k type
#  ko check kre but wo bahut jyada line of code likhna padega

##---it works in 3 step
## step-1 define the pydantic schema , jiske andar hamare data ka ideal schema hoga
## step-2 instantiate this above class with raw data to validate it
## step-3 Now we can use that in our codebase

from pydantic import BaseModel

##step-1
class Patients(BaseModel):
    name:str
    age:int

## step-2
patients_info={"name":"Anshuman","age":"30"} ## focus here we are giving 30 in string but 
                    #then also it will work, because wo internally isko type convert mar de rha hai
                    ## koi  aur string hoga then ye kam ni krega 
patient1=Patients(**patients_info)

## step-3
def insert_patient_data(patient:Patients):
    print(patient.name)
    print(patient.age)
    print("inserted in database1")

insert_patient_data(patient1)