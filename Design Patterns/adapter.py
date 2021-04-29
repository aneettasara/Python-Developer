# Adapter - Structural Pattern

class French:
	'''  French Speaker '''
	def __init__(self):
		self.name = "French"

	def speak_french(self):
		return "Bonjour!"

class British:
	'''  English Speaker '''
	def __init__(self):
		self.name = "British"	

	def speak_english(self):
		return "Hello!"	

class Adapter:
	''' changes generic method name to individualized method names '''

	def __init__(self, object, **adapted_method):
		''' Change the name of the method '''
		self._object = object

		#Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
		#For example, speak() will be translated to speak_french() if the mapping says so
		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		''' Simply return the rest of attributes! '''
		return getattr(self._object, attr)
		
#List to store speaker objects
objects = []

#Create a French object
french = French()

#Create a British object
british =British()

#Append the objects to the objects list
objects.append(Adapter(french, speak=french.speak_french))
objects.append(Adapter(british, speak=british.speak_english))


for obj in objects:
	print(f"{obj.name} says '{obj.speak()}'\n")