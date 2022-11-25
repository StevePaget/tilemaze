from pygame_functions import *

class Coin():
    def __init__(self, image,row,col,value):
        self.image = makeSprite(image)
        showSprite(self.image)
        self.row = row
        self.col = col
        self.value = value
        self.valueLabel = makeLabel(str(self.value),24,0,0,"black")
        showLabel(self.valueLabel)
        
    def move(self,x,y):
        moveSprite(self.image,x,y)
        moveLabel(self.valueLabel,x+35,y+40)
        


class World():
    def __init__(self):
        self.grid = [ [0 for x in range(18)] for y in range(18)]
        self.tileGrid = [ [None for x in range(18)] for y in range(18)]

        self.tileImages = ["path.png","wall.png"]
        
        self.items=[]
        # demo wall
        for col in range(7,10):
            self.grid[9][col] = 1
        
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
        
        topleftcol = self.player.col-4
        topleftrow = self.player.row-4

        # move all tile sprites into position
        for row in range(18):
            for col in range(18):
                y = (row-topleftrow)*100
                x = (col-topleftcol)*100
                moveSprite(self.tileGrid[row][col], x,y)
        # move items
        for item in self.items:
            y = (item.row-topleftrow)*100
            x = (item.col-topleftcol)*100
            item.move(x,y)
        
    def addItem(self,newItem):
        self.items.append(newItem)

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
w.addItem(Coin("coin.png",5,5,15))
while True:
    w.update()
    updateDisplay()
    tick(5)


endWait()