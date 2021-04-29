# Builder

# Director
class Director():     
    def __init__(self, builder):
        self._builder = builder
       
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()
        
    def get_car(self):
        return self._builder.car       

# Abstract Builder
class Builder():    
    def __init__(self):
        self.car = None
        
    def create_new_car(self):
        self.car = Car()

# Concrete Builder --> provides parts and tools to work on the parts
class BobBuilder(Builder):  
    def add_model(self):
        self.car.model = "Bob"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):    
        self.car.engine = "Turbo engine"

# Product
class Car():
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None
        
    def __str__(self):
        return f'{self.model} | {self.tires} | {self.engine}'

builder = BobBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)