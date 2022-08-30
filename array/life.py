from myarray import Array2D


class LifeGrid:
    # Define constant to represent cell states
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Create the game grid and initialize the cells to dead
    def __init__(self, numRows, numCols):
        self._grid = Array2D(numRows, numCols)
        # Clear the grid and set to dead state
        self.configure(list())

    # Returns th number of rows
    def numRows(self):
        return self._grid.numRows()

    # Returns th number of columns
    def numCols(self):
        return self._grid.numCols()

    # Configure the grid to contain the given live cells
    def configure(self, coordList):
        # clear the game grid
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)
        # Set the indicated cell to be allive
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    # Does the indicated cll contain a living organism?
    def isLivingCell(self, row, col):
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    # Clears the indicated cell by setting it to dead
    def clearCell(self, row, col):
        self._grid[row, col] = LifeGrid.DEAD_CELL

    # Sets the indiative cell to be alive
    def setCell(self, row, col):
        self._grid[row, col] = LifeGrid.LIVE_CELL

    # Return the number of living neighbour for the given cell.
    def numLivingNeighbours(self, row, col):
        sum = 0
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                pass
