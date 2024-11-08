
#our cat entity
class cat:
    #constructor: making a cat for the code
    #to construct a cat, it is required to give it a given_name and a given_colour
    #given_name and given_colour are attributes
    def __init__(self, given_name,given_colour):
        self.name = given_name
        self.colour = given_colour

# instance: a specific occurance of a class
# an instance of 
mimi = cat("mimi","brown")
print (mimi.name)
print (mimi.colour)