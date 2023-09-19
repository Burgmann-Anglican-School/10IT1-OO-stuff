Car example
class Car:

    def __init__(self, colour, ks):
        self.colour = colour
        self.ks = ks
    
    def __str__(self):
        return f"The {self.colour} car has {self.ks:,} kilometres."
    
car1 = Car("blue", 20000)
car2 = Car("red", 30000)

print(car1)
print(car2)