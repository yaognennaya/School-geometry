EPS = 10 ** (-6)

def eq(first, second):
    return abs(first - second) < EPS

def grate(first, second):
    return first >= second + EPS

def less(first, second):
    return first <= second + EPS

class Point:
    def __init__(self, first, second):
        self.x = first
        self.y = second
    
    def __str__(self):
        return str(self.x) + " " + str(self.y)
    

class Line:
    def __init__(self, first, second):
        self.a = first
        self.b = second
    

class Vector:
    def __init__(self, first, second):
        self.x = second.x - first.x
        self.y = second.y - first.y
    
    def __mul__(first, second):#*
        return first.x * second.y - second.x * first.y
    
    def __pow__(first, second):#**
        return first.x * second.x + second.y * first.y
    
    def __add__(first, second):
        return Vector(Point(0, 0), Point(first.x + second.x, first.y + second.y))
        
        
    def dist(first):
        return (first.x ** 2 + first.y ** 2) ** 0.5

class EquationLine:
    def __init__(self, first, second, third):
        self.A = first
        self.B = second
        self.C = third
    
    def two_point(self):
        a = self.A
        b = self.B
        c = self.C
        return Point(- a * c / (a ** 2 + b ** 2), - b * c / (a ** 2 + b ** 2)), Point(- a * c / (a ** 2 + b ** 2) - b, - b * c / (a ** 2 + b ** 2) + a) 
    def perpendicular_to_line(first, second):
        return [- first.B, first.A, - first.A * second.y + first.B * second.x]

def dist(first, second):
    if type(first) == type(second) == Point:
        return (abs(first.x - second.x) ** 2 + abs(first.y - second.y) ** 2) ** 0.5
    elif type(first) == Line and type(second) == Point:
        return (Vector(first.a, first.b) * Vector(first.a, second)) / dist(first.a, first.b)


x1, y1, x2, y2, x3, y3 = map(int, input().split())    
point0 = Point(0, 0)
point1 = Point(x1, y1)
point2 = Point(x2, y2)
point3 = Point(x3, y3)    

vector1 = Vector(point0, point1)
vector2 = Vector(point0, point2)
vector3 = Vector(point0, point3)
summ = (vector1 + vector2) + vector3
print(summ.x / 3, summ.y / 3)
