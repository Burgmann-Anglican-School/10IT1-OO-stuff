class Pack:

    def __init__(self, size, contents):
        self.size = size
        self.contents = contents
        # The below would be the best way to solve
        #the adding items to a pack and the
        #capacity checking problem
        '''
        current_size = 0
        for pack_item in self.contents:
            current_size += pack_item.size
        self.current_size = current_size
        '''

    def addItem(self, item):
        current_size = 0
        for pack_item in self.contents:
            current_size += pack_item.size
        if current_size + item.size > self.size:
            print("Pack too full")
            return False
        else:
            self.contents.append(item)
            return True

    def dropItem(self, item):
        if item in self.contents:
            self.contents.remove(item)
            print(f"{item} Added")
            return True
        else:
            print("Item not in pack")
            return False

    def packCapacity(self):
        current_size = 0
        for pack_item in self.contents:
            current_size += pack_item.size
        print(f"I am {self.size} size, and have used {current_size} spaces")

    def __str__(self):
        return f"In my pack: {', '.join(self.contents)}"

class Item:
    
    def __init__(self, size):
        self.size = size
    
    def getSize(self):
        return self.size
    
    def __str__(self):
        attrs = self.__dict__
        output = self.__class__.__name__ + ': '
        for attr in attrs:
            output += attr + ": " + str(attrs[attr]) + ' | ' 
        return output[:-2]
    
class Potion(Item):

    def __init__(self, size, potency):
        self.size = size
        self.potency = potency

    def use(self):
        return "I was used"
    
class Weapon(Item):

    def __init__(self, size, power, _range):
        self.size = size
        self.power = power
        self.range = _range

    def getPower(self):
        return self.power

    def getRange(self):
        return self.range
    
class Axe(Weapon):

    def __init__(self, size, power, _range, name):
        self.size = size
        self.power = power
        self.range = _range
        self.name = name

    def chop(self):
        pass

    def swing(self):
        pass

class Sword(Weapon):

    def __init__(self, size, power, _range, name):
        self.size = size
        self.power = power
        self.range = _range
        self.name = name

    def thrust(self):
        pass

    def swing(self):
        pass

my_pack = Pack(50, [])
print(my_pack)

my_axe = Axe(3, 6, 9, "Twelve")
my_sword = Sword(100, 3, 7000000, "Shush")
my_potion = Potion(7, 32)

print(my_axe)
print(my_potion)
print(my_sword)

print("Adding Axe")
my_pack.addItem(my_axe)
print(my_pack)

print("Adding Sword")
my_pack.addItem(my_sword)
print(my_pack)

print("Adding Potion")
my_pack.addItem(my_potion)
print(my_pack)

print("Dropping Axe")
my_pack.dropItem(my_axe)
print(my_pack)