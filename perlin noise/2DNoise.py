from tkinter import *
import random

random.seed(input("What seed do you want to use? "))

app = Tk()
app.title("2D noise")
c = Canvas(app,width="500",height="500")
c.pack()

noiseGrid= []
dotProducts = []

# fills the grid with 100x100 random integers -1, 0 or 1
def fillGrid(grid):
    for x in range(250):
        grid.append([])
        for y in range(250):
            grid[x].append(random.randint(-1,1))
    return grid

def getDotProduct(grid):
    dotProducts = []
    for x in range(len(grid)):
        row = []
        for y in range(len(grid[x])):
            # Gets the dot products for all surrounding nodes
            # Access multidimensional array with arr[x][y]
            try:
                dotYN = grid[x-1][y] * grid[x][y]
            except:
                dotYN
            try:
                dotXN = grid[x][y-1] * grid[x][y]
            except:
                dotXN = grid[x][y]
            try:
                dotYP = grid[x+1][y] * grid[x][y]
            except:
                dotYP = grid[x][y]
            try:
                dotXP = grid[x][y+1] * grid[x][y]
            except:
                dotXP = grid[x][y]

            # finds the midpoint between all four points (maybe not interpolating)
            lerpDot = (dotXN + dotYN + dotXP + dotYP)/4
            row.append(lerpDot)
        dotProducts.append(row)
    return dotProducts

def drawGrid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            # Gets the colour for the square depending on its value (heightmap)
            if grid[x][y] == -1:
                colour = "black"
            elif grid[x][y] == -0.75:
                colour = "gray12"
            elif grid[x][y] == -0.5:
                colour = "gray25"
            elif grid[x][y] == -0.25:
                colour = "gray38"
            elif grid[x][y] == 0:
                colour = "gray50"
            elif grid[x][y] == 0.25:
                colour = "gray62"
            elif grid[x][y] == 0.5:
                colour = "gray75"
            elif grid[x][y] == 0.75:
                colour = "gray88"
            else:
                colour = "white"

            c.create_rectangle(x*2,y*2,(x+1)*2,(y+1)*2,fill=colour)

# runs the code once
noiseGrid = fillGrid(noiseGrid)
dotProducts = getDotProduct(noiseGrid)
drawGrid(dotProducts)

mainloop()
