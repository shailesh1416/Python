# Implementing array ADT using array capabilities of the ctype module
import ctypes


class Array:
    # create an array with size element
    def __init__(self, size):
        assert size > 0, "Array size must be greater than zero"
        self._size = size
        # Create the array structure using the ctype module
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # initialise each element
        self.clear(None)

    # Gets the content of the index
    def __getitem__(self, index):
        assert index >= 0 and index < self._size, "Array subscript out of range"
        return self._elements[index]
    # Sets the content at a given index

    def __setitem__(self, index, value):
        assert index >= 0 and index < self._size, "Array subscript out of range"
        self._elements[index] = value
    # Clears the array by setting each element to the given value

    def clear(self, value):
        for i in range(self._size):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)


# Aniterator for Array ADT
class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


class Array2D:
    # Create 2D of size numRows x numCols.
    def __init__(self, numRows, numCols):
        # Create a 1-D array to store an array referene for 1D arrays
        self._theRows = Array(numRows)

        # create the 1-D array for each row of the 2-D array
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    # Returns the number of columns in the 2-D array
    def numRows(self):
        return self._theRows._size

    # Returns the number of the columns in the 2-D array
    def numCols(self):
        return self._theRows[0]._size

    # Clear the array by setting every element to a given value
    def clear(self, value):
        for row in self._theRows:
            row.clear(value)

    # Access the content of the element at position [i,j]
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of arry subscript"
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows()\
            and col >= 0 and col < self.numCols(),\
            "Array subscript out of range"
        the1dArray = self._theRows[row]
        return the1dArray[col]

    # Set the content to the element at position [i,j]
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of arry subscript"
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows()\
            and col >= 0 and col < self.numCols(),\
            "Array subscript out of range"
        the1dArray = self._theRows[row]
        the1dArray[col] = value
