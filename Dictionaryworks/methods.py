employee={"id":1000, "name":"rahul", "department":"hr", "age":22, "salary":25000}

# print employee salary


# get(key) invalid key return none/fetch a value
print(employee.get("department"))

# pop(key) remove
employee.pop("salary")
print(employee)


# keys() return all keys
for k in employee.keys():

    print(k)



# values() return all values
for v in employee.values():
    print(v)


# items() fetch keys & values

for k,v in employee.items():
    print(k,v)
