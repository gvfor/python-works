employee={"eid":1000, "name":"rahul", "salary":35000, "department":"hr", "experience":6 }

print(employee["salary"])

employee["contact"]=98767757

print(employee)

# if experience > 5 update employee salary as current_salary+10000 else current_salary+5000

if employee["experience"]>5:

    employee["salary"]+=10000
else:
    employee["salary"]+=5000

print(employee)

# add role as sde if exp>5 else add role as jde

if employee["experience"]>5:
    
    employee["role"]="sde"
else:
    employee["role"]="jde"

print(employee)