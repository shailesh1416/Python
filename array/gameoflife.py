# program for playing th game of life
from life import LifeGrid

# Define the initial congiguration of cell
INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]

# set the size of the grid
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of generations.
NUM_GENS = 8


def main():
    # construct the game grid and configure it
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # play Game
    draw(grid)
    for i in range(NUM_GENS):
        grid = evolve(grid)
        draw(grid)

# Generates the next gneration of organisms


def evolve(grid):
    # List for storing the live cells of next generation
    liveCells = list()

    # Iterate over the element of the grid
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            # Determine the number of living neighbours of the cell
            neighbours = grid.numLivingNeighbours(i, j)

            # Add the (i,j) tuple to liveCells if this cell contains a living organism in next generation
            if(neighbours == 2 or neighbours == 3) and grid.isLivingCell(i, j):
                liveCells.append((i, j))
    # Reconfigure the grid using the living Cells coord list.
    grid.configure(liveCells)
    return grid

# Print a text-based representation of the game grid


def draw(grid):
    pass
# main()
