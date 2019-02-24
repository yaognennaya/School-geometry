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
    def one_point(self):
        a = self.A
        b = self.B
        c = self.C
        return Point(- a * c / (a ** 2 + b ** 2), - b * c / (a ** 2 + b ** 2))
        
        
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
    
def two_line(first, second):
    if Vector(first.a, first.b) * Vector(second.a, second.b) == 0 and Vector(first.a, first.b) * Vector(first.a, second.b) != 0:
        return 0
    elif Vector(first.a, first.b) * Vector(first.a, second.b) == 0 and Vector(first.a, first.b) * Vector(second.a, second.b) == 0 :
        return 2
    else:
        return 1
    
def Equation_line(first, second):
    x1, y1, x2, y2 = first.x, first.y, second.x, second.y
    A = 1
    B = 0
    C = 0
    if y1 == y2:
        A = 0
        B = 1
        C = - y1
    else:
        B = (x1 - x2) / (y2 - y1)
        C = - B * y1 - x1
    return [A, B, C]

def point_in_two_line(first, second):
    A, B, C, a, b, c = first.A, first.B, first.C, second.A, second.B, second.C
    return [(B * c - C * b) / (A * b - B * a), (A * c - C * a) / (a * B - A * b)]

def point_in_line(first, second):
    Vector1 = Vector(first.a, first.b)
    Vector2 = Vector(first.a, second)
    if eq(Vector1 * Vector2, 0):
        return 1 #yes
    else:
        return 0 #no

def point_in_beam(first1, first2, second):
    if point_in_line(Line(first1, first2), second) == 0:
        return 0 #no
    elif Vector(first1, first2) ** Vector(first1, second) >= 0:
        return 1 #yes
    else:
        return 0 #no

def parallel_line(line, R):
    A, B, C = line.A, line.B, line.C
    normal1 = Vector(Point(-B, A), Point(0, 0))
    normal2 = Vector(Point(A * R / normal1.dist(), B * R / normal1.dist()), Point(0, 0)) 
    point1 = line.one_point()
    new_point = Point(point1.x + normal2.x, point1.y + normal2.y)
    a, b, c = A, B, 0
    c = -(new_point.x * a + new_point.y * b)
    return a, b, c

A, B, C, R = map(int, input().split())
equation_line1 = EquationLine(A, B, C)
a, b, c = parallel_line(equation_line1, R)
print(a, b, c)

