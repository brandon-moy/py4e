# Python Objects

# This is more definitions and mechanics - how it works not how to use it

# An object is a bit of sef-contained Code and Data
# A key asped of the Object approach is to break the problem into smaller understandable parts (divide and conquer)
# Objects have boudnaries that allow us to ignore un-needed detail

# Definitions
# Class - a template - Dog
# Method or Message - a definied capability of a class - bark()
# Field or attribute - A bit of data in a class - length
# Object or Instance - A particular instance of a class - Lassie
# Constructor - code that runs when an object is created
# Inheritance - the ability to extend a class to make a new class

# Sample Class
class PartyAnimal:              # Template for making PartyAnimal OBJECTS
    x = 0                       # Each PartyAnimal object has a bit of data
    def party(self):            # Defining a method party
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal()              # Constructing a PartyAnimal object and store in an

an.party()
an.party()
an.party()

# Playing with dir() and type()
# dir() command lists capabilities
# Ignore the ones with underscores - these are used by Python
# The rest are real operations that the object can perform
# it is like type() - it tells us something *about* a variable

# Object Lifecycle
# Objects are created, used, and discarded
# We have special blocks of code(methods) that get called
  # At the moment of creation (constructor)
  # At the moment of destruction (destructor)
# Constructors are used a lot, Destructors not so much

class PartyAnimals:
    x = 0

    def __init__(self): # Constructor
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self): # Destructor
        print('I am destructed', self.x)

an = PartyAnimals()

an.party()
an.party()
an = 42

# Inheritance

# When we make a new class- we can reuse an existing calss and inherit all
# the capabilities of an existing class then add our own bit to make a new class
# another form of store and reuse
# Write once- reuse many times
# The new class (child) has all the capabilities of the old class (parent) and then some

class FootballFan(PartyAnimals): # FootballFan is a class that extends PartyAnimals
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
