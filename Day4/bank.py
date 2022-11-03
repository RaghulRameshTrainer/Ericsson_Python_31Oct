class Account():
    def __init__(self,fname,lname,aadhar,deposit):
        self.fname=fname
        self.lname=lname
        self.aadhar=aadhar
        self.__balance=deposit   #(_ => protected , __ => private)
        self.userid=fname+aadhar[:3]
        self.password=lname+aadhar[-3:]

    def getBalance(self):
        return self.__balance

    def setBalance(self,amt):
        self.__balance=self.__balance+amt
