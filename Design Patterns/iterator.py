# Iterator - Behavioral Pattern

def count_to(count):
	
	#Our list
	numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight"]

	#Our built-in iterator
	#Creates a tuple such as (1, "one")
	iterator = zip(range(count), numbers)
	
	#Iterate through our iterable list
	#Extract the numbers
	#Put them in a generator called number
	for position, number in iterator:		
		#Returns a 'generator' containing numbers
		yield number 

# generator returned by our iterator
for num in count_to(4):
	print(f"{num}")

print()

for num in count_to(7):
	print(f"{num}")