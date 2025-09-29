class Test :
    a = 10 # attribute
    def hello(self) : # method
        print("Hello World") 
    # print("I'm inside class Test")

# print(a) # NameError
# print(Test().a) # 10
# Test().hello() # Hello World

obj = Test()

# print(obj.a) # 10
# obj.hello() # Hello World

obj2 = Test()

obj3 = Test()

#* Constructor

class Factory :
    def __init__(self, material, zips, pockets) :
        # print(self) #? address of the object
        self.material = material
        self.zips = zips
        self.pockets = pockets
    def show(self) :
        print(f"Your object details are {self.material}, {self.zips}, {self.pockets}")

reebok = Factory("leather", 3, 4)
campus = Factory("nylon", 2, 3)
# print(reebok.material) #? leather
# print(campus.material) #? nylon

# reebok.show() #? Your object details are leather, 3, 4
# campus.show() #? Your object details are nylon, 2, 3


#* Types of Attributes & Methods
#? self is used to capture the current object

class Animal :
    name = "Lion" #? class attribute

    def __init__(self,age) :
        self.age = age #? instance attribute

    def show(self) : #? instance method Here self targets the current object
        print(f"Animal name is {self.name} and age is {self.age}")

    @classmethod
    def hello(cls) : #? class method Here cls targets the class itself(Animal)
        # print(f"Hello from class method {cls.age}") #? AttributeError: type object 'Animal' has no attribute 'age'
        print(f"Hello from class method {cls.name}") #? Hello from class method Lion

    @staticmethod
    def static() :
        print("Hello from static method")

obj = Animal(12)
#? Object works like an argument to the instance method

# obj.show() #? Animal name is Lion and age is 12
# obj.hello() #? Hello from class method
# obj.static() #? Hello from static method
