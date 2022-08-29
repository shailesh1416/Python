from line import Point, LineSegment


class Polygon:
    def __init__(self, *points):
        self.points = points

    # Returns all the vertices of polygon
    def noOfVertices(self):
        return len(self.points)

    # Returns length of all lines of polygon
    def lineLengths(self):
        lengths = []
        for i in range(len(self.points)-1):
            l = LineSegment(self.points[i], self.points[i+1])
            lengths.append(l.length())
        closinglline = LineSegment(self.points[0], self.points[-1])
        lengths.append(closinglline.length())
        return lengths

    # Returns perimeter of polygon
    def perimeter(self):
        return sum(self.lineLengths())

    # Returns the ares of polygon
    def area(self):
        pass


if __name__ == "__main__":

    p = Polygon(Point(0, 0), Point(0, 5), Point(5, 5), Point(5, 0))

    print("Number of vertices : ", p.noOfVertices())
    print("Perimeter : ", p.perimeter())
    print("Lengths : ", p.lineLengths())
