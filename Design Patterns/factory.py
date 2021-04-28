# Factory Pattern

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "bark!"

    def __str__(self):
        return self.name

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "meow!"

    def __str__(self):
        return self.name

def get_pet(pet = "dog"):
    pets = dict(dog = Dog("Simba"), cat = Cat("Caren"))
    return pets[pet]

# Main Function

myPet1 = get_pet("dog")
print(str(myPet1)+" "+str(myPet1.speak()))

myPet2 = get_pet("cat")
print(str(myPet2)+" "+str(myPet2.speak()))
