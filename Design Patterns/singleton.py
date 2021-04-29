# Singleton using Borg Design Pattern

class Borg:
    _shared_data = {} # Attribute dictionary is Private
    
    def __init__(self):
        # Make it an attribute dictionary
        self.__dict__ = self._shared_data 

       
class Singleton(Borg): #Inherits from the Borg class
    #This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_data.update(kwargs) 

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_data)

# Main Function

# Singleton object
x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)
# {'HTTP': 'Hyper Text Transfer Protocol'}

# Another Singleton object and if it refers to the same attribute dictionary.
y = Singleton(SNMP="Simple Network Management Protocol")
print(y)
# {'HTTP': 'Hyper Text Transfer Protocol', 'SNMP': 'Simple Network Management Protocol'}