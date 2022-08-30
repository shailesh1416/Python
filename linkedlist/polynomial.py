
class Polynomial:
    # Create new polynomial object
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead

    # Return the degree of the polynomial.
    def degree(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree

    # Return the coefficient for the term of the given degree
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial"
        curNode = self._polyHead
        while curNode is not None and curNode.degree >= degree:
            curNode = curNode.next
        if curNode is None or curNode.degree != degree:
            return 0.0
        else:
            return curNode.degree

    # Evaluate the polynomial at the given scalaer alue
    def evaluate(self, scalar):
        assert self.degree() >= 0, "Only non-empty polynomial can be evaluated."
        result = 0.0
        curNode = self._polyHead
        while curNode is not None:
            # print(curNode.coefficient * (scalar**curNode.degree))
            result += curNode.coefficient * (scalar**curNode.degree)
            curNode = curNode.next
        return result

    # Helper method for appending terms to the polynomial
    def _appendTerm(self, degree, coefficient):
        if coefficient != 0.0:
            newTerm = _PolyTermNode(degree, coefficient)
            if (self._polyHead is None):
                self._polyHead = newTerm
            else:
                self._polyTail.next = newTerm
            self._polyTail = newTerm

    # Polynomial addition : newPoly = self+rhsPoly
    def __add__(self, rhsPoly):
        if self._polyHead is None and rhsPoly._polyHead is None:
            return Polynomial()
        elif self._polyHead is None:
            return rhsPoly
        elif rhsPoly._polyHead is None:
            return self
        else:
            if self.degree() > rhsPoly.degree():
                maxdegree = self.degree()
            else:
                maxdegree = rhsPoly.degree()

            curNode1 = self._polyHead
            curNode2 = rhsPoly._polyHead
            newPoly = Polynomial()
            for i in range(maxdegree+1):
                if curNode2 is None and curNode2 is None:
                    return newPoly
                elif curNode2 is None:
                    newPoly._appendTerm(
                        curNode1.degree, curNode1.coefficient)
                    curNode1 = curNode1.next
                elif curNode1 is None:
                    newPoly._appendTerm(
                        curNode2.degree, curNode2.coefficient)
                    curNode2 = curNode2.next
                elif curNode1.degree == curNode2.degree:
                    newcoeff = curNode1.coefficient+curNode2.coefficient
                    newPoly._appendTerm(curNode1.degree, newcoeff)
                    curNode1 = curNode1.next
                    curNode2 = curNode2.next
                else:
                    if curNode1.degree > curNode2.degree:
                        newPoly._appendTerm(
                            curNode1.degree, curNode1.coefficient)
                        curNode1 = curNode1.next
                    else:
                        newPoly._appendTerm(
                            curNode2.degree,  curNode2.coefficient)
                        curNode2 = curNode2.next
        return newPoly

    # def polynomial multiplication
    def __mul__(self, rhsPoly):
        if self._polyHead is None or rhsPoly._polyHead is None:
            return Polynomial()
        else:
            newPoly = Polynomial()
            test = []
            curNode1 = self._polyHead

            while curNode1 is not None:
                tempPoly = Polynomial()
                curNode2 = rhsPoly._polyHead
                while curNode2 is not None:
                    tempPoly._appendTerm(
                        curNode1.degree+curNode2.degree, curNode1.coefficient*curNode2.coefficient)
                    curNode2 = curNode2.next
                curNode1 = curNode1.next
                newPoly = newPoly + tempPoly
        return newPoly

    def draw(self):
        if self._polyHead is None:
            print("Polynomila has no terms")
            return -1
        else:
            curPolyNode = self._polyHead
            while curPolyNode is not None:
                print(f'{curPolyNode.coefficient}x({curPolyNode.degree})', end=" ")
                curPolyNode = curPolyNode.next
        print()

# class for creating polynomial term nodes used with the linkd list


class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None


if __name__ == "__main__":
    p1 = Polynomial()
    p1._appendTerm(2, 5)
    p1._appendTerm(0, 4)

    p2 = Polynomial()
    p2._appendTerm(3, 5)
    p2._appendTerm(1, 10)
    p2._appendTerm(0, 0)

    mpoly = p1*p2
    p1.draw()
    p2.draw()
    mpoly.draw()
