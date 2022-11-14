from pygame_functions import *

class World():
    def __init__(self):
        self.grid = [ [0 for x in range(18)] for y in range(18)]
        self.grid[6][10] = 1
        self.tileGrid = [ [None for x in range(18)] for y in range(18)]

        self.tileImages = ["path.png","wall.png"]

        
        for row in range(18):
            for col in range(18):
                self.tileGrid[row][col] = makeSprite(self.tileImages[self.grid[row][col]])
                showSprite(self.tileGrid[row][col])
        self.player = Player(5,6)
        self.update()

    def update(self):
        # move player
        if keyPressed("right"):
            self.player.move(0,1)
        if keyPressed("left"):
            self.player.move(0,-1)
        if keyPressed("up"):
            self.player.move(-1,0)
        if keyPressed("down"):
            self.player.move(1,0)
        
        topleftcol = self.player.col-3
        topleftrow = self.player.row-1

        # move all sprites into position
        for row in range(18):
            for col in range(18):
                y = (row-topleftrow)*100
                x = (col-topleftcol)*100
                moveSprite(self.tileGrid[row][col], x,y)
        

class Player():
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.sprite = makeSprite("player.png")
        showSprite(self.sprite)
        moveSprite(self.sprite,400,400)

    def move(self,rowdiff,coldiff):
        self.row += rowdiff
        self.col += coldiff
        

screenSize(900,900)
setAutoUpdate(False)

w = World()
while True:
    w.update()
    updateDisplay()
    tick(5)


endWait()