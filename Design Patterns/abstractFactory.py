# Abstract and Concrete Factory - Creational Pattern
# Abstract and Concrete Products

class Dog:
    def speak(self):
        return "bark!"

    def __str__(self):
        return "Dog"

class DogFactory:       # Concrete Factory
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food"
        
class PetStore:         # Abstract Factory
    def __init__(self, pet_factory=None):
        self.pet_factory = pet_factory

    def show_pet(self):

        pet = self.pet_factory.get_pet() 
        pet_food = self.pet_factory.get_food() 

        print(f"Our pet is '{pet}'!")
        print(f"Our pet says hello by '{pet.speak()}'")
        print(f"Its food is '{pet_food}'!")

# Main Function

# Concrete Factory
factory = DogFactory()

# Abstract Factory with the instance of Concrete Factory
shop = PetStore(factory)

shop.show_pet()
