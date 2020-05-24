#classes of animals:
from math import sqrt
import turtle
import math

#first
class dog:
    def __init__(self):
        self.legs = 4
        self.tail = 1
    def speak(self):
        print("Woof!!")
    def fur(self):
        print("Brown")
        self.__breed()
    def __breed(self):
        print("poodle")

Dog = dog()
Dog.speak()
Dog.fur()

#second
class cat:
    def __init__(self, legs, tail):
        self.legs = legs
        self.tail = tail
    def speak(self):
        print("Meow")
    def fur(self):
        print("Golden")
        self.__eyes()
    def __eyes(self):
        print("shiny")

Cat = cat(4, 1)
print(Cat.legs)
Cat.speak()
Cat.fur()

#third
class ant:
    def __init__(self):
        self.legs = 4
        self.size = "Very Small"
    def Quality(self):
        print("Hardwork")

Ant = ant()
print("size of ant " + Ant.size)
Ant.Quality()

#fourth
class camel:
    def __init__(self):
        self.legs = 4
        self.size = "Very Big"
    def home(self):
        print("desert")
    def speciality(self):
        print("hump")
Camel = camel()
print("size of camel " + Camel.size)
Camel.home()
Camel.speciality()

#fifth
class cow:
    def __init__(self):
        self.legs = 4;
        self.type = "Domestic"
        self.__sound()
    def __sound(self):
        print("Mooh!!")
Cow = cow()

#sixth
class lion:
    def __init__(self):
        self.legs = 4
        self.type = "Wild"
    def speciality(self):
        print("King of the jungle")
        self.__sound()
    def __sound(self):
        print("Roar!!")
Lion = lion()
Lion.speciality()

#seventh
class cheetah:
    def __init__(self):
        self.legs = 4
        self.type = "Wild"
    def Quality(self):
        print("Cheetah is the fastest animal and its " + self.type)
Cheetah = cheetah()
Cheetah.Quality()

#eighth
class kangaroo:
    def __init__(self):
        self.legs = 4
        self.type = "Wild"
    def Special(self):
        print("Kangaroos are the highest jumping animals and have pockets")
Kangaroo = kangaroo()
Kangaroo.Special()

#ninth
class Giraffe:
    def __init__(self):
        self.legs = 4
        self.type = "Wild"
    def Quality(self):
        print("Giraffes are the wild animals with tallest necks")
giraffe = Giraffe()
giraffe.Quality()

#tenth
class elephants:
    def __init__(self):
        self.legs = 4
        self.type = "wild"
    def Speciality(self):
        print("Elephants have long trump")
Elephants = elephants()
Elephants.Speciality()




#classes of shapes:
#first

class Rectangle:
    
    def __init__(self, length = 15, breadth = 10):
        #public access specifiers i.e can be accessed from anywhere
        self.length = length
        self.breadth = breadth
    
    #public member method
    def getlength(self):
        print("The length of rectangle is: {}".format(self.length))
    
    def getbreadth(self):
        print("The breadth of rectangle is: {}".format(self.breadth))
    
    def getPerimeter(self):
        print("The perimeter of rectangle is: {}".format(2*(self.length + self.breadth)))
    
    def getArea(self):
        print("The area of rectangle is: {}".format(self.length*self.breadth))
    
    def drawRectangle(self):
        print("I will draw a rectangle.")
        rect = turtle.Turtle()
        rect.forward(self.length)
        rect.right(90)     # Rotate clockwise by 90 degrees
        rect.forward(self.breadth)
        rect.right(90)

        rect.forward(self.length)
        rect.right(90)
        rect.forward(self.breadth)
        rect.right(90)
        
        turtle.resetscreen()
        
    def __str__(self):
        return "I am a rectangle"
    


#object my_rectangle of class rectangle is formed
my_rectangle = Rectangle(100,50)


#Accessing the public access methods
my_rectangle.getlength()
my_rectangle.getArea()
my_rectangle.getPerimeter()
my_rectangle.drawRectangle()

#second
class Circle:
    
    #Class object attribute
    pi = 3.14
    
    def __init__(self, radius = 10):
        #private access specifier
        self.__radius = radius

    def getradius(self):
        return self.__radius
      
    #private access methods
    def __getCircumference(self):
        print("The circumference of circle is: {}".format(2*self.pi*self.__radius))
        
    def __getArea(self):
        print("The area of circle is: {}".format(self.pi*self.__radius*self.__radius))
        
    def drawCircle(self):
        print("I will draw a circle")
        cir = turtle.Turtle()
        cir.circle(self.getradius())
        
        turtle.resetscreen()
        
    #accessing private method using a public method
    def accessCircumference(self):
        self.__getCircumference()
        
    def accessArea(self):
        self.__getArea()
    

my_circle = Circle(100)


# We cannot access i.e. call my_circle.__getArea since it is a private access method 
# and we use the public method for displaying area

my_circle.accessArea()
my_circle.accessCircumference()
my_circle.drawCircle()

#third
class Square:
    
    def __init__(self, side = 100):
        self.side = side
        
    def getArea(self):
        print("The area of square is: {}".format(self.side * self.side))
    
    def getPerimeter(self):
        print("The area of square is: {}".format(self.side *4))
    
    def drawSquare(self):
        print("I will draw a square.") 
        square = turtle.Turtle()
        
        for i in range(4):
            square.forward(self.side)
            square.right(90)

        turtle.resetscreen()


my_square = Square(150)
my_square.getArea()
my_square.getPerimeter()
my_square.drawSquare()

#fourth
class Equilateral_Triangle:

    def __init__(self, sidee = 60):
        self.sidee = sidee

    def getPerimeter(self):
        print("Perimeter of the equilateral triangle is: {}".format(3*self.sidee))
        
    def getArea(self):
        print("Area of equilateral triangle is: {}".format(sqrt(3)*self.sidee*self.sidee/4))
        
    def drawtriangle(self):
        print("I will draw an equilateral triangle.")
        board = turtle.Turtle()
 
        board.forward(self.sidee) # draw base
         
        board.left(120)
        board.forward(self.sidee)
         
        board.left(120)
        board.forward(self.sidee)

        turtle.resetscreen()

my_triangle = Equilateral_Triangle(100)
my_triangle.getPerimeter()
my_triangle.getArea()
my_triangle.drawtriangle()


#fifth
class Hexagon:

    def __init__(self, hside = 50):
        self.hside = hside

    def getPerimeter(self):
        print("Perimeter of the hexagon is: {}".format(6*self.hside))

    def getArea(self):
        print("Area of hexagon is: {}".format(1.5*sqrt(3)*self.hside*self.hside))

    def drawhexagon(self):
        print("I will draw a heaxagon.")

        hex = turtle.Turtle()

        for i in range(6):
            hex.forward(self.hside) 
            hex.left(60) 

        turtle.resetscreen()


my_hexagon = Hexagon(100)
my_hexagon.getPerimeter()
my_hexagon.getArea()
my_hexagon.drawhexagon()

