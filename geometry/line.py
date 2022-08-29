import math


# Creates a point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"


# Creates a new Line Segment instance defined by the two Point objects
class LineSegment:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"({self.a.x},{self.a.y}),({self.b.x},{self.b.y})"

    #  Returns the first endpoint of the line
    def endPointA(self):
        return self.a

    #  Returns the mid-point of the line
    def midPoint(self):
        mx = (self.a.x + self.b.x)/2
        my = (self.a.y + self.b.y)/2
        return Point(mx, my)

    #  Returns the second endpoint of the line
    def endPointB(self):
        return self.b

    # Returns the length of the line segment given as the Euclidean distance between the two endpoints
    def length(self):
        return math.sqrt(((self.b.x-self.a.x)**2)+((self.b.y-self.a.y)**2))

    # Returns a string representation of the line segment in the format (Ax, Ay)#(Bx, By).
    def toString(self):
        return f"({self.a.x},{self.b.x}) ({self.a.y},{self.b.y})"

    # Checkes if line a parallen to y axis?
    def isVertical(self):
        if (self.b.x - self.a.x) == 0:
            return True
        else:
            return False

    # Checkes if line a parallen to x axis?
    def isHorizontal(self):
        if (self.b.y - self.a.y) == 0:
            return True
        else:
            return False

    # is this line parallel to other line
    def isParallel(self, otherLine):
        # comparing points a - a and point b - b
        if (otherLine.a.x-self.a.x) == (otherLine.b.x-self.b.x) and (otherLine.a.y-self.a.y) == (otherLine.b.y-self.b.y):
            return True
        # comparing points a - b and point b - a
        elif (otherLine.a.x-self.b.x) == (otherLine.b.x-self.a.x) and (otherLine.a.y-self.b.y) == (otherLine.b.y-self.a.y):
            return True
        else:
            return False

    # Returns the slope of the line segment given as the rise over the
    # run. If the line segment is vertical, None is returned.
    def slope(self):
        if (self.b.x-self.a.x) == 0:
            return None
        return (self.b.y-self.a.y)/(self.b.x-self.a.x)

    # Checking if two lines are perpendicular to each other
    def isPerpendicular(self, otherLine):

        # If one line is horizontal and other is vertical the its always perpendicular
        if (self.isVertical() and otherLine.isHorizontal()) or (otherLine.isVertical() and self.isHorizontal()):
            return True

        # Checking perpendicularity for regular lines
        if (self.slope() * otherLine.slope()) == -1:
            return True
        else:
            return False

    # Checking if two lines are intersecting each other
    def isIntersect(self, otherLine):
        if self.isParallel(otherLine):
            return False
        else:
            return True

    # Shifts the line segment by xInc amount along the x-axis and yInc amount along the y-axis.
    def shift(self, xInc, yInc):
        self.a.x = self.a.x+xInc
        self.b.x = self.b.x+xInc
        self.a.y = self.a.y+yInc
        self.b.y = self.b.y+yInc
        return LineSegment(self.a, self.b)


if __name__ == "__main__":

    # creating an instance of linesegment
    line = LineSegment(Point(1, 1), Point(3, 1))
    line2 = LineSegment(Point(2, 1), Point(2, 3))

    # formated string
    # print('Eucleadian Disatnce : {}'.format(line.length()))
    # f string
    print(f'Eucleadian Disatnce : {line.length()}')
    print("MidPoint : ", line.midPoint())
    print("Sifted line : ", line.shift(xInc=2, yInc=3))
    print("EndPoint A : ", line.endPointA())
    print("EndPoint B : ", line.endPointA())
    print("Line String : ", line.toString())
    print("Vertical : ", line.isVertical())
    print("Horizontal : ", line.isHorizontal())
    print("Slope of Line : ", line.slope())
    print("Slope of Line2 : ", line2.slope())
    print("Parallel : ", line.isParallel(line2))
    print("Perpendicular : ", line.isPerpendicular(line2))
    print("Intersect : ", line.isPerpendicular(line2))
