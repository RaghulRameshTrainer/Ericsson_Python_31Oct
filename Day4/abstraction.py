from abc import ABC, abstractmethod
class Car(ABC):
    #cannot have the constructor

    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def mirror(self):
        pass
    @abstractmethod
    def seat_belt(self):
        pass
    @abstractmethod
    def engine(self):
        pass

    def get_price(self,model):
        if model=='EcoSport':
            return '1600000'
        elif model=='Aspire':
            return '1000000'
        elif model=='Fiesta':
            return '1100000'
        else:
            return "Please check at showroom."

class NewCar(Car):
    def __init__(self,model, my):
        self.model=model
        self.my=my

    def breaks(self):
        self.breaks='Applied'

    def mirror(self):
        self.mirror_count=3

    def seat_belt(self):
        self.seat_belt='Fitted'

    def engine(self):
        self.engine_type='powerstrain'
        return self.engine_type

    def inventory_details(self):
        print("EcoSport=1000 \nAspire=1000\nFiesta=500\nEndeavour=300")

c1=NewCar('EcoSport',2022)
print(c1.get_price('Figo'))
c1.inventory_details()
print(c1.engine())
