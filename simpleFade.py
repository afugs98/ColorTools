import pygame
import time
import random
from PIL import Image
import colorsys
import math
import os


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

block_color = (53, 115, 255)


class ColorWheel:

    def __init__(self, gameDisplay, sizeX, sizeY, xPos=0, yPos=0):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.xPos = xPos
        self.yPos = yPos
        self.gameDisplay = gameDisplay

        imageObject = Image.new("RGB", (self.sizeX, self.sizeY))
        self.radius = min(imageObject.size) / 2.0
        self.center = (self.sizeX / 2 + self.xPos, self.sizeY / 2 + self.yPos)
        pix = imageObject.load()

        for x in range(self.sizeX):
            for y in range(self.sizeY):
                rx = x - self.center[0] + self.xPos
                ry = y - self.center[1] + self.yPos
                s = ((x - self.center[0] + self.xPos) ** 2.0 + (y - self.center[1] + self.yPos) ** 2.0) ** 0.5 / self.radius
                if s <= 1.0:
                    h = ((math.atan2(ry, rx) / math.pi + math.pi) + 1.0) / 2.0
                    rgb = colorsys.hsv_to_rgb(h, s, 1.0)
                    pix[x, y] = tuple([int(round(c * 255.0)) for c in rgb])
                else:
                    pix[x, y] = (200, 200, 200)

        pygameImage = pygame.image.fromstring(imageObject.tobytes(), imageObject.size, imageObject.mode)
        self.wheel = pygameImage

    def getColorWheel(self):
        return self.wheel

    def show(self):
        self.gameDisplay.blit(self.getColorWheel(), (self.xPos, self.yPos))

    def distanceToCenter(self, coords):
        if not isinstance(coords, tuple):
            raise ValueError('Fam this gotta be a tuple of coords')
        else:
            return ((((self.center[0] - coords[0]) ** 2) + ((self.center[1] - coords[1]) ** 2)) ** 0.5)

    def isInWheel(self, coords):
        # This just checks to see if the passes point is in the box, returns bool
        if not isinstance(coords, tuple):
            raise ValueError('Fam this gotta be a tuple of coords')
        else:
            if(coords[0] <= self.sizeX + self.xPos and coords[0] > self.xPos):
                if (coords[1] <= self.sizeY + self.yPos and coords[1] > self.yPos):

                    # Now have to make sure that it is in the wheel, not just the box
                    if self.distanceToCenter(coords) < self.radius:
                        return True

        return False

    def getRGB(self, coords):

        rx = coords[0] - self.center[0] + self.xPos
        ry = coords[1] - self.center[1] + self.yPos
        s = ((coords[0] - self.center[0] + self.xPos) ** 2.0 + (coords[1] - self.center[1] + self.yPos) ** 2.0) ** 0.5 / self.radius
        if s <= 1.0:
            h = ((math.atan2(ry, rx) / math.pi + math.pi) + 1.0) / 2.0

            return colorsys.hsv_to_rgb(h, s, 1.0)

        else:
            print("Got a probelm")




class TextObject:

    def __init__(self, gameDisplay, displayText, xPos, yPos, size=25, initialValue=0):
        self.xPos = xPos
        self.yPos = yPos
        self.displayText = displayText
        self.font = pygame.font.SysFont(None, size)
        self.value = initialValue
        self.gameDisplay = gameDisplay

    def updateText(self, newTextWords):
        if not isinstance(newTextWords, str):
            raise ValueError('Hey fam that needs to be a string')
        else:
            self.displayText = newTextWords

    def show(self):
        text = self.font.render(self.displayText + str(self.value), True, black)
        self.gameDisplay.blit(text, (self.xPos, self.yPos))
        pygame.display.update()

    def updateValue(self, value):
        self.value = value


class Display:

    def __init__(self, xSize=1200, ySize=700):
        self.xSize = xSize
        self.ySixe = ySize

        pygame.init()

        self.gameDisplay = pygame.display.set_mode((self.xSize, self.ySixe))
        pygame.display.set_caption('Color visualizer, now with classes')
        self.clock = pygame.time.Clock()

    def getGameDisplay(self):
        return self.gameDisplay

    def getClock(self):
        return self.clock

class ColorCheckerApp:

    def __init__(self):
        self.display = Display(1200, 700)
        self.colorWheel = ColorWheel(self.display.getGameDisplay(), 400, 400, 100, 100)
        self.redValue = TextObject(self.display.getGameDisplay(), 'Red: ', 5, 5, initialValue=0)
        self.greenValue = TextObject(self.display.getGameDisplay(), 'Green: ', 5, 30, initialValue=0)
        self.blueValue = TextObject(self.display.getGameDisplay(), 'Blue: ', 5, 55, initialValue=0)

    def loop(self):
        while 1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:


                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    # This means that there was a click
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if self.colorWheel.isInWheel(pos):
                        print(self.colorWheel.getRGB(pos))

            self.display.getGameDisplay().fill(white)

            pygame.display.update()
            self.display.getClock().tick(60)

            self.colorWheel.show()
            self.redValue.show()
            self.greenValue.show()
            self.blueValue.show()



############### Below is the program ##############

def RunApp():

    app = ColorCheckerApp()
    app.loop()
    pygame.quit()
    quit()

RunApp() # This is the actual call that calls the rest of the code