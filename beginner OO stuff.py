# #The worst
# # Time consuming to create, it's not adaptable for other dogs.
# # Not easy to print out.
# dog = 'Clifford'
# dog_breed = 'big'
# dog_colour = 'red'
# print(f"{dog} the {dog_breed} {dog_colour} dog")

# #The dictionary approach
# dog1 = {'name': input("Name: "), 'breed': input("Breed: "), 'colour': input("Colour: ")}
# for key in dog1:
#     print(key, dog1[key])

#Classes
class Dog:
    #Dunder Method
    #Class initialiser or the class constructor
    def __init__(self, name, breed, colour):
        self.name = name
        self.breed = breed
        self.colour = colour

    #Method that is actually a procedure
    def description(self):
        return self.name + " is a " + self.breed+ " that is " + self.colour

#Instantiation - We are creating an instance of the class as an object
dog1 = Dog('Clifford', 'Big', 'Red')
dog2 = Dog('Bob', 'Great Dane', 'Purple')
dog3 = Dog('Hugo', 'Sausage', '0xFFFFFF')

bob = dog3.description()
print(bob)
