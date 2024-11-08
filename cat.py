class cat:
    #constructor: making a cat for the code
    #to construct a cat, it is required to give it a given_name and a given_colour
    #given_name and given_colour are attributes
    def __init__(self,given_name,given_colour):
        self.name = given_name
        self.colour = given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5

    def train(self):
        print(f"{self.name} is training...")
        self.intelligence +=1
        self.energy -= 5
    
    def eat(self):
        print(f"{self.name} is eating...")
        self.weight += 3
        self.energy += 1
    
    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy += 3
    
    def play(self):
        print(f"{self.name} is playing...")
        self.weight -= 2
        self.energy -= 2



    