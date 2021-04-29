# Decorator - Structural Pattern

from functools import wraps

def make_blink(function):
    ''' Decorator definition '''       # docstring

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)

    # inner function
    def decorator():
        #Grab the return value of the function being decorated
        ret = function()

        #Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator

# Decorator is used
@make_blink
def hello_world():
    ''' Original function! '''       # docstring
    
    return "Hello, World!"

# Decorated result
print(hello_world())

# the function name is still the same name of the function being decorated
print(hello_world.__name__)

# the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)