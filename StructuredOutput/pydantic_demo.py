from pydantic import BaseModel,EmailStr,Field

class Student(BaseModel):
    name : str = "nitish"
    email : EmailStr
    cgpa : float = Field(gt = 0, lt = 10,default=5.0,description = "A result showing scale")

new_student = {"name": "32", "email":"abc@gmail.com"}
student = Student(**new_student)

print(student)
print(type(student))