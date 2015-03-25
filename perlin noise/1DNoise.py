from tkinter import *
import random
import time

app = Tk()
app.title("1D noise")
c = Canvas(app,width="500",height="10")
c.pack()

noiseGrid = []
noiseDotProducts = []

# fills the grid with either -1, 0 or 1 for the random noise genaration
def fillGrid(grid):
    for i in range(100):
        grid.append(random.randint(-1,1))
    return grid

# gets the dot product of the two nodes either side of it
def getDotProduct(grid,dotProductGrid):
    for i in range(len(grid)):
        # gets the dot product of the current node and the one before it
        dotN = grid[i-1] * grid[i]
        # gets the dot product of the current node and the one after it
        try:
            dotP = grid[i] * grid[i+1]
        except:
            dotP = grid[i]

        # gets the mean of the two dot products
        dotProductGrid.append((dotN+dotP)/2)

    return dotProductGrid

def drawGrid(grid):
    for i in range(len(grid)):
        if grid[i] == 1:
            colour = "white"
        elif grid[i] == 0.5:
            colour = "gray75"
        elif grid[i] == 0:
            colour = "gray50"
        elif grid[i] == -0.5:
            colour = "gray25"
        else:
            colour = "black"

        c.create_rectangle(i*5,0,(i+1)*5,10,fill=colour)


noiseGrid = fillGrid(noiseGrid)
noiseDotProducts = getDotProduct(noiseGrid,noiseDotProducts)
drawGrid(noiseDotProducts)

mainloop()
