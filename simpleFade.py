import pygame
import time
import random
from PIL import Image
import colorsys
import math
import os

class ColorWheel:

    def __init__(self, sizeX, sizeY, xPos=0, yPos=0):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.xPos = xPos
        self.yPos = yPos

        imageObject = Image.new("RGB", (self.sizeX, self.sizeY))
        radius = min(imageObject.size) / 2.0
        center = imageObject.size[0] / 2, imageObject.size[1] / 2
        pix = imageObject.load()

        for x in range(imageObject.width):
            for y in range(imageObject.height):
                rx = x - center[0]
                ry = y - center[1]
                s = ((x - center[0]) ** 2.0 + (y - center[1]) ** 2.0) ** 0.5 / radius
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
        gameDisplay.blit(pygameColorWheel.getColorWheel(), (self.xPos, self.yPos))


class TextObject:

    def __init__(self, displayText, xPos, yPos, size=25, initialValue=0):
        self.xPos = xPos
        self.yPos = yPos
        self.displayText = displayText
        self.font = pygame.font.SysFont(None, size)
        self.value = initialValue

    def updateText(self, newTextWords):
        if not isinstance(newTextWords, str):
            raise ValueError('Hey fam that needs to be a string')
        else:
            self.displayText = newTextWords

    def show(self):
        text = self.font.render(self.displayText + str(self.value), True, black)
        gameDisplay.blit(text, (self.xPos, self.yPos))
        pygame.display.update()

    def updateValue(self, value):
        self.value = value




pygame.init()

display_width = 1000
display_height = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

block_color = (53, 115, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Color visualizer')
clock = pygame.time.Clock()




pygameColorWheel = ColorWheel(400, 400)
redValue = TextObject('Red: ', 5, 5, initialValue=0)
greenValue = TextObject('Green: ', 5, 30, initialValue=0)
blueValue = TextObject('Blue: ', 5, 55, initialValue=0)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)

        gameDisplay.fill(white)


        pygame.display.update()
        clock.tick(60)

        pygameColorWheel.show()
        redValue.show()
        greenValue.show()
        blueValue.show()



def RunApp():

    game_loop()
    pygame.quit()
    quit()




RunApp() # This is the actual call that calls the rest of the code