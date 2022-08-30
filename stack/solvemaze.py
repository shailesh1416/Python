# program for building and solving a maze.
from maze import Maze


def main():
    maze = buildMaze("mazefile.txt")
    # maze.draw()
    if maze.findpath():
        print("Path  found")
        maze.draw()
    else:
        print("Path not found")

# build a maze on a text format in the govel file


def buildMaze(filename):
    infile = open(filename, 'r')

    # read the size of maze
    nrows, ncols = readValuePair(infile)

    maze = Maze(nrows, ncols)

    # read the start and exit position
    row, col = readValuePair(infile)
    print(row, col)
    maze.setStart(row, col)
    row, col = readValuePair(infile)
    maze.setExit(row, col)

    # Reas the maze itself
    for row in range(nrows):
        line = infile.readline()
        for col in range(ncols):
            # print(line[col])
            if line[col] == "*":
                maze.setWall(row, col)

    # close the maze file and return newly constructed file
    infile.close()
    return maze

# extract an integer value from a given input file


def readValuePair(infile):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)


# call the main function
main()
