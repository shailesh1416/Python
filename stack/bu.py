def findpath(self):
    path = Stack()
    curCell = self._startCell
    self._markTried(curCell.row, curCell.col)
    counter = 1
    while curCell is not self.MAZE_WALL:
        print(counter)
        self.draw()
        r = curCell.row
        c = curCell.col
        if self._exitFound(r, c):
            return True
        path.push(curCell)

        if self._ValidCell(r-1, c) and self._mazeCells[r-1, c] is not self.TRIED_TOKEN:
            # if self._mazeCells[r-1, c] is self.PATH_TOKEN:
            #     self._markTried(r, c)
            #     path.pop()
            # else:
            self._markPath(r-1, c)
            curCell = self._mazeCells[r-1, c]
            path.push(curCell)

        # elif self._ValidCell(r, c+1) and self._mazeCells[r-1, c] is not self.TRIED_TOKEN:
        #     if self._mazeCells[r, c+1] is self.PATH_TOKEN:
        #         self._markTried(r, c)
        #         path.pop()
        #     curCell = self._mazeCells[r, c+1]
        #     path.push(curCell)

        # elif self._ValidCell(r+1, c) and self._mazeCells[r-1, c] is not self.TRIED_TOKEN:
        #     if self._mazeCells[r+1, c] is self.PATH_TOKEN:
        #         self._markTried(r, c)
        #         path.pop()
        #     curCell = self._mazeCells[r+1, c]
        #     path.push(curCell)

        # elif self._ValidCell(r, c-1) and self._mazeCells[r-1, c] is not self.TRIED_TOKEN:
        #     if self._mazeCells[r, c-1] is self.PATH_TOKEN:
        #         self._markTried(r, c)
        #         path.pop()
        #     curCell = self._mazeCells[r, c-1]
        #     path.push(curCell)

        else:
            return self
