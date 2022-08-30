from myarray import Array2D
from pylinkedstack import Stack


class Maze:
    MAZE_WALL = '*'
    PATH_TOKEN = 'x'
    TRIED_TOKEN = 'O'

    # Initialize the maze with all cells marked as open
    def __init__(self, numRows, numCols):
        self._mazeCells = Array2D(numRows, numCols)
        self._startCell = None
        self._exitCell = None

    # Returns the number of rows in maze
    def numRows(self):
        return self._mazeCells.numRows()

    # Returns the number of columns in maze
    def numCols(self):
        return self._mazeCells.numCols()

    # Fills the indicated cell with a wall marker
    def setWall(self, row, col):
        assert row >= 0 and row < self.numRows(
        ) and col >= 0 and col < self.numCols(), "Cell index out of range"
        self._mazeCells[row, col] = Maze.MAZE_WALL

    # Sets the starting cell position
    def setStart(self, row, col):
        assert row >= 0 and row < self.numRows(
        ) and col >= 0 and col < self.numCols(), "Cell index out of range"
        self._startCell = _CellPosition(row, col)

    # Sets the exit cell position
    def setExit(self, row, col):
        assert row >= 0 and row < self.numRows(
        ) and col >= 0 and col < self.numCols(), "Cell index out of range"
        self._exitCell = _CellPosition(row, col)

    # Return Ttrue if given cell is valid to move
    def _ValidCell(self, row, col):
        return row >= 0 and row < self.numRows() and col >= 0 and col < self.numRows() and self._mazeCells[row, col] == None

    # Check if the exit cell is found:
    def _exitFound(self, row, col):
        return row == self._exitCell.row and col == self._exitCell.col

    # Drop a tried token at the given cell
    def _markTried(self, row, col):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    # Drop a path token at the given cell
    def _markPath(self, row, col):
        self._mazeCells[row, col] = self.PATH_TOKEN

    # Reset the maze
    def reset(self):
        self._mazeCells.clear(None)

    # Find maze path and return maze
    def findpath(self):
        path = Stack()
        curCell = self._startCell
        preCell = None

        if curCell == self._exitCell:
            path.push(curCell)
            self._markPath(curCell.row, curCell.col)
            print("Start and exit cell are same")
            return True
        else:
            path.push(curCell)
            self._markPath(curCell.row, curCell.col)

        while curCell != self._exitCell:
            row = curCell.row
            col = curCell.col

            if self._ValidCell(row-1, col):
                preCell = curCell
                curCell = _CellPosition(row-1, col)
                path.push(curCell)
                self._markPath(row-1, col)

            elif self._ValidCell(row, col+1):
                preCell = curCell
                curCell = _CellPosition(row, col+1)
                path.push(curCell)
                self._markPath(row, col+1)

            elif self._ValidCell(row+1, col):
                preCell = curCell
                curCell = _CellPosition(row+1, col)
                path.push(curCell)
                self._markPath(row+1, col)

            elif self._ValidCell(row, col-1):
                preCell = curCell
                curCell = _CellPosition(row, col-1)
                path.push(curCell)
                self._markPath(row, col-1)

            else:
                if curCell.row == self._exitCell.row and curCell.col == self._exitCell.col:
                    return True
                elif not path.isEmpty():
                    print("Backtracking")
                    path.pop()
                    self._markTried(row, col)
                    curCell = preCell

        if preCell == self._exitCell:

            return True
        elif path.isEmpty():
            return False

    # draws the MAIZE

    def draw(self):
        for i in range(self.numCols()):
            for j in range(self.numCols()):
                print(self._mazeCells[i, j], end=" ")
            print()


class _CellPosition:
    def __init__(self, row, col):
        self.row = row
        self.col = col
