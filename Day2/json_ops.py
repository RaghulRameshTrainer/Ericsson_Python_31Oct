import json

# with open("test.json","r") as fo:
#     json_data=json.load(fo)
#     for d in json_data['people']:
#         print("first name : " + d['firstName'] + "  lastname : "+ d['lastName'] +"  age : "+str(d['age']))

emp_data={
    'fname':'Raghul',
    'lname':'Ramesh',
    'salary':None,
    'is_manager':False,
    'city':'Chennai'
}
with open("emp.json","w") as ef:
    json.dump(emp_data,ef,indent=5)

