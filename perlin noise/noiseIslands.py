from tkinter import *
import random

seed = input("What seed do you want to use? ")
if seed != "r":
    random.seed(seed)

app = Tk()
app.title("Islands")
c = Canvas(app,width="700",height="700")
c.pack()

grid = []

# fills the grid with 100x100 random integers -1, 0 or 1
def fillGrid(grid):
    for x in range(350):
        grid.append([])
        for y in range(350):
            grid[x].append(random.randint(-1,1))
    return grid

# each integer returned will be between -1 and 3, at 0.5 intervals
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
            lerpDot = (dotXN + dotYN + dotXP + dotYP)/2
            row.append(lerpDot)
        dotProducts.append(row)
    return dotProducts

grid = fillGrid(grid)
grid = getDotProduct(grid)
drawGrid(grid)

mainloop()
