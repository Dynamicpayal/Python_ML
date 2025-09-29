#* Inheritance

#? Benefit of Inheritance

#? Code Reusability 
#? Organized Structure
#? Easy to maintain and extend

class Parent : #? Parent class
    class_attribute = "I am a class attribute"
    def hello(self) :
        print("I am a method from Parent class")

class Child(Parent) : #? Child class inherits from Parent class
    pass


obj = Parent()

obj2 = Child()

# print(obj.class_attribute) #? I am a class attribute
# obj.hello() #? I am a method from Parent class

#? If we try to print a function then the output will be None.

# print(obj2.class_attribute) #? I am a class attribute
# obj2.hello() #? I am a method from Parent class


#* Single Inheritance

class Animal :
    def __init__(self, name) :
        self.name = name
    
    def show(self) :
        print(f"Animal name is {self.name}")

class Human(Animal) :
    def __init__(self, name, age) :
        super().__init__(name)
        self.age = age

person1 = Human("Lion", 12)
# person1.show() #? Animal name is Lion

person2 = Animal("Tiger")
# person2.show() #? Animal name is Tiger


#* Multiple Inheritance
class A :
    def feature1(self) :
        print("Feature 1 is working")
    
    def feature2(self) :
        print("Feature 2 is working")

class B :
    def feature3(self) :
        print("Feature 3 is working")
    
    def feature4(self) :
        print("Feature 4 is working")

class C(A, B) :
    def feature5(self) :
        print("Feature 5 is working")

obj = C()
# obj.feature1() #? Feature 1 is working
# obj.feature3() #? Feature 3 is working
# obj.feature5() #? Feature 5 is working


#* Multilevel Inheritance
class Factory :
    def __init__(self, material, zips) :
        self.material = material
        self.zips = zips

class BhopalFactory(Factory) :
    def __init__(self, material, zips, color) :
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFactory) :
    def __init__(self, material, zips, color, pockets) :
        super().__init__(material, zips, color)
        self.pockets = pockets

obj = PuneFactory("leather", 3, "black", 4)

