from myarray import Array2D


class Matrix:
    # Creates a matrix of size numRow x numCols initialized to 0
    def __init__(self, numRows, numCols):
        self.theGrid = Array2D(numRows, numCols)
        self.theGrid.clear(0)

    def plotmatrix(self):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                print(self[r, c], end=" ")
            print()

    # Return the umber of rows in matrix
    def numRows(self):
        return self.theGrid.numRows()

    # Retruns the number of columns in matrix
    def numCols(self):
        return self.theGrid.numCols()

    # Returns the value of element (i,j)
    def __getitem__(self, ndxTuple):
        return self.theGrid[ndxTuple[0], ndxTuple[1]]

    # Sets the value of element (i,j)
    def __setitem__(self, ndxTuple, scalar):
        self.theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    # scale the matrix by given value
    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar

    # Create and return a new matrix that resuts from matrix addition
    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and\
            rhsMatrix.numCols() == self.numCols(),\
            "Matrix size is not compatible for the add operation."
        # Create a new matrix
        newMatrix = Matrix(self.numCols(), self.numCols())
        # Add the corresponding matrix
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c]+rhsMatrix[r, c]
        return newMatrix

     # Create and return a new matrix that resuts from matrix addition
    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and\
            rhsMatrix.numCols() == self.numCols(),\
            "Matrix size is not compatible for the subtract operation."
        # Create a new matrix
        newMatrix = Matrix(self.numCols(), self.numCols())
        # Subtract the corresponding matrix
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = rhsMatrix[r, c]+self[r, c]
        return newMatrix

    # Create and return a new matrix resulting from matrix multipliation
    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numCols() and\
            rhsMatrix.numCols() == self.numRows(),\
            "Matrix size is not compatible for the Multiply operation."
        # create a new matrix
        newMatrix = Matrix(self.numRows(), rhsMatrix.numCols)
        # Multiply th two matrix by matrix rule
        for r in range(newMatrix.numRows()):
            for c in range(newMatrix.numCols()):
                sum = 0
                for i in range(self.numCols()):
                    # sum = self[c,i]*rhsMatrix[i,c]
                    sum += self[r, i]*rhsMatrix[i, c]
                newMatrix[r, c] = sum
        return newMatrix

    # create and return a new matrix that is transpose of the matrix

    def transpose(self):
        # creating a new matrix
        newMatrix = Matrix(self.numCols(), self.numRows())

        # transposing the matrix
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[c, r] = self[r, c]
        return newMatrix
