class vehicle():
    def __init__(self,type,make,model):
        self.type=type
        self.make=make
        self.model=model

    def fuel_type(self,type):
        if type.casefold()=='cycle':
            return "Not Applicable"
        else:
            return "Diesel"

    def availability(self,type):
        if type.casefold()=="cycle":
            return "Can be delivered post 30 days of ordered date"
        else:
            return "3 months of time from order date"

    def get_price(self,model):
        if model=='car':
            return "price range from 10L - 50L"
        elif model=="jeep":
            return "price range from 17L to 60L"
        else:
            return "please check at showroom"

class Bus(vehicle):
    def availability(self, type):
        if type=="basemodel":
            return "Can be delivered post 6 months of ordered date"
        else:
            return "12 months of time from order date"

    def get_price(self, model):
        if model == 'ordinary':
            return "1Cr"
        elif model == "Special":
            return "1.5Cr"
        else:
            return "please check at showroom"

    def fuel_type(self,type):
        return super().fuel_type(type)

b=Bus('bus','Tata',2022)
print(b.availability('Ultradelux'))

print(b.fuel_type('Jeep'))