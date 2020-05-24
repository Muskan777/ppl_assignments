#10 animals class

#first

class Cat:
    def __init__(self):
        self.legs = 4
        self.eyes = "shiny"
    def family(self):
        self.family = "cats"

#second

class tiger(Cat):
    def __init__(self):
        self.type = "wild"
    def speak(self):
        self.speak = roar

#third

class cheetah(Cat):
    def __init__(self):
        self.type = "wild"
    def speciality(self):
        self.spec = "Fastest animal"

#fourth

class fox(Cat):
    def __init__(self):
        self.type = "Wild"
    def speciality(self):
        self.special = "Smartest Animal in the jungle"

#fifth

class wolf(Cat):
    def __init__(self):
        self.type = "wild"
    def speciality(self):
        self.spec = "scariest animal"

#sixth

class birds:
    def __init__(self):
        self.wings = 2
    def ability(self):
        self.ability = "can fly"

#seventh

class crow(birds):
    def __init__(self):
        self.color = "black"
    def found(self):
        self.found = "found in residential areas"

#eighth

class peacock(birds):
    def __init__(self):
        self.look = "most beautiful bird"
    def dance(self):
        self.dance = "dances in rain"

#ninth

class swan(birds):
    def __init__(self):
        self.swim = "swans can swim"
    def color(self):
        self.color = "White"

#tenth

class pigeon(birds):
    def __init__(self):
        self.livesin = "Resodential areas"
    def type(self):
        self.type = "migratory"

#10 shapes class

#first

class polygons:
    def __init__(self):
        self.figure = "closed"
    def type(self):
        self.type = "multiple sides"

#second

class triangle(polygons):
    def __init__(self):
        self.edges = 3
        self.vertices = 3
    def interiorAngle(self):
        self.sumofintAngle = "180 degree"


#third

class square(polygons):
    def __init__(self):
        self.edges = 4
        self.vertices = 4
    def interiorAngle(self):
        self.sumofintAngle = "360 degree"

#fourth

class pentagon(polygons):
    def __init__(self):
        self.edges = 5
        self.vertices = 5
    def interiorAngle(self):
        self.sumofintAngle = "540 degree"

#fifth

class hexagon(polygons):
    def __init__(self):
        self.edges = 6
        self.vertices = 6
    def interiorAngle(self):
        self.sumofintAngle = "720 degree"

#sixth

class line:
    def __init__(self):
        self.defin = "combination of infinite points joined together"
    def ends(self):
        self.ends = "two end points endless in both directions"

#seventh

class angle(line):
    def __init__(self):
        self.defin = "combination of two lines form an angle"
    def value(self):
        self.value = "smaller angle between two lines is less than or equal to 180 degree"

#eighth

class conics:
    def __init__(self):
        self.form = "formed by cutting a cone in various patterns"

#ninth

class circle(conics):
    def __init__(self):
        self.radius = "fixed"
        self.type = "closed figure"
    def center(self):
        self.center = "has a center"

#tenth

class ellipse(conics):
    def __init__(self):
        self.focii = 2
    def type(self):
        self.type = "closed figure"

        
        


