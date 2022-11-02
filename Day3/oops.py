class Employee():
    hike=1.05
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.pay=salary
        self.email=self.fname+'_'+self.lname+'@ericsson.com'

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def appraisal(self):
        #self.hike=hike
        self.pay=int(self.pay*self.hike)

    @classmethod
    def create_object(cls,emp_str):
        fn,ln,sal=emp_str.split("-")
        return cls(fn,ln,int(sal))

    @staticmethod
    def is_workingday(dt):
        if dt.weekday()==5 or dt.weekday()==6:
            return "HOLIDAY!!!"
        else:
            return "Working Day!"

# emp1=Employee('Levin','Lenus',50000)
# emp2=Employee('Bala','Murugan',60000)

import datetime

td=datetime.date(2022,11,6)
print(Employee.is_workingday(td))
#
# emp1='Raghul-Ramesh-10000'
# emp2='Ram-Prasath-20000'
#
# emp_1=Employee.create_object(emp1)
# emp_2=Employee.create_object(emp2)
#
# print(emp_1.fullname())
# print(emp_2.fullname())
#
# emp_1.hike=1.1
# print(emp_1.pay)
# emp_1.appraisal()
# print(emp_1.pay)
#
# print(emp_2.pay)
# emp_2.appraisal()
# print(emp_2.pay)
#
# # Methods
# # object/instance method
# # classmethod
# # staticmethod

##Features
# Inheritance
# Abstraction
# Polymorphism
# Encapsulation