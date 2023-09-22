#Class definition for the Dog
class Dog:

    #Class constructor for Dog
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    #Dunder string method that overrides print
    def __str__(self):
        return f"{self.name} is a {self.age} year old dog that is {self.colour}"
    
    #Speak method that takes a sound argument
    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussel(Dog):

    #Override speak method with a default argument
    def speak(self, sound="Yap"):
        return f"{self.name} says {sound}"

class Bulldog(Dog):

    #Override speak method with a default argument
    def speak(self, sound="Growl"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):

    #Override speak method with a default argument
    def speak(self, sound="Sausage"):
        return f"{self.name} says {sound}"

class GermanShephard(Dog):

    #Override speak method with a default argument
    def speak(self, sound="Spek"):
        return f"{self.name} says {sound}"

#Instantiate dogs    
dog1 = Dog('Harold', 6, 'UoP: Red')
dog2 = JackRussel('Purple', 7, 'Burgundy')

#Test dogs
print(dog1, dog1.speak('Nuh-uh'))
print(dog2, dog2.speak())