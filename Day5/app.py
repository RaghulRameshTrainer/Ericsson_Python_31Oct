from flask import Flask,jsonify,request
app=Flask(__name__)

employee=[
    {
        'name':'Ramshankar',
        'tech':'Python'
    },
    {
        'name':'Balamurugan',
        'tech':'Bigdata'
    }
]

@app.route('/')
def home():
    return "<h1>Web Application is running successfully!</h1>"

@app.route('/employee/<string:name>')
def get_employee(name):
    for emp in employee:
        if(emp['name']==name):
            return jsonify(emp['name'])
    return jsonify({"message":"employee records not found!"})

@app.route('/employee/<string:name>/tech')
def get_employee_tech(name):
    for emp in employee:
        if(emp['name']==name):
            return jsonify(emp['tech'])
    return jsonify({"message":"employee records not found!"})

@app.route('/employee',methods=['POST'])
def add_employee():
    req_data=request.get_json()
    new_employee={
        'name':req_data['name'],
        'tech':req_data['tech']
    }
    employee.append(new_employee)
    return jsonify(new_employee)

@app.route('/delete/<string:name>',methods=['DELETE'])
def delete_employee(name):
    for emp in employee:
        if(emp['name']==name):
            employee.remove(emp)
            return jsonify({"message":"Employee record has been deleted"})
    return jsonify({"message":"employee records not found!"})

app.run(port=8000)