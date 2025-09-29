#* Polymorphism
def show() :
    print("This is show() method")

def show() :
    print(f"This is another show() method")

# show() #? This is another show() method

class Animal :
    def speak(self) :
        print("Animal speaks")

class Human(Animal) :
    def speak(self) :
        print("Human speaks")

obj = Human()

obj = Animal()

# obj.speak2() #? Animal speaks
# obj.speak() #? Human speaks
# obj.speak() #? Human speaks
# obj.speak() #? Animal speaks

#? Method Overloading doesn't exist in Python.

#* Duck Typing

class Test :
    def show(self) :
        print("This is show() method from Test class")

class Demo :
    def display(self) :
        print("This is display() method from Demo class")

obj = Test()
obj2 = Demo()

obj.show() #? This is show() method from Test class
obj2.display() #? This is display() method from Demo class