import pygame
import time
import random
from PIL import Image
import colorsys
import math
import os

def CreateColorWheel(sizeX, sizeY):

    imageObject = Image.new("RGB", (sizeX, sizeY))
    radius = min(imageObject.size) / 2.0
    centre = imageObject.size[0] / 2, imageObject.size[1] / 2
    pix = imageObject.load()

    for x in range(imageObject.width):
        for y in range(imageObject.height):
            rx = x - centre[0]
            ry = y - centre[1]
            s = ((x - centre[0]) ** 2.0 + (y - centre[1]) ** 2.0) ** 0.5 / radius
            if s <= 1.0:
                h = ((math.atan2(ry, rx) / math.pi) + 1.0) / 2.0
                rgb = colorsys.hsv_to_rgb(h, s, 1.0)
                pix[x, y] = tuple([int(round(c * 255.0)) for c in rgb])
            else:
                pix[x, y] = (200, 200, 200)

    # im.show()
    # Then at the end we need to convert this into something pygame can pick up

    pygameImage = pygame.image.fromstring(imageObject.tobytes(), imageObject.size, imageObject.mode)

    return pygameImage
#
# def colorWheel():
#
#     imageObject = Image.new("RGB", (300, 300))
#     radius = min(imageObject.size) / 2.0
#     centre = imageObject.size[0] / 2, imageObject.size[1] / 2
#     pix = imageObject.load()
#
#     for x in range(imageObject.width):
#         for y in range(imageObject.height):
#             rx = x - centre[0]
#             ry = y - centre[1]
#             s = ((x - centre[0]) ** 2.0 + (y - centre[1]) ** 2.0) ** 0.5 / radius
#             if s <= 1.0:
#                 h = ((math.atan2(ry, rx) / math.pi) + 1.0) / 2.0
#                 rgb = colorsys.hsv_to_rgb(h, s, 1.0)
#                 pix[x, y] = tuple([int(round(c * 255.0)) for c in rgb])
#             else:
#                 pix[x, y] = (200, 200, 200)
#
#     # im.show()
#     # Then at the end we need to convert this into something pygame can pick up
#
#     pygameImage = pygame.image.fromstring(imageObject.tobytes(), imageObject.size, imageObject.mode)
#
#     return pygameImage

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

pygameColorWheel = CreateColorWheel(400, 400)


def DisplayPixelCounts(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Pixels: " + str(count), True, black)
    gameDisplay.blit(text, (5, 5))
    pygame.display.update()

def DisplayPosX(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("X: " + str(count), True, black)
    gameDisplay.blit(text, (5, 30))
    pygame.display.update()

def DisplayPosY(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Y: " + str(count), True, black)
    gameDisplay.blit(text, (5, 55))
    pygame.display.update()


# def things(thingx, thingy, thingw, thingh, color):
#     pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def DisplayWheel():
    gameDisplay.blit(pygameColorWheel, (100, 100))


# def text_objects(text, font):
#     textSurface = font.render(text, True, black)
#     return textSurface, textSurface.get_rect()
#
#
# def message_display(text):
#     largeText = pygame.font.Font('freesansbold.ttf', 115)
#     TextSurf, TextRect = text_objects(text, largeText)
#     TextRect.center = ((display_width / 2), (display_height / 2))
#     gameDisplay.blit(TextSurf, TextRect)
#
#     pygame.display.update()
#
#     time.sleep(200)
#
#     game_loop()


# def crash():
#     message_display('You Crashed')

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
                DisplayPosX(pos[0])
                DisplayPosY(pos[1])

                # get a list of all sprites that are under the mouse cursor
                # clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]

        gameDisplay.fill(white)

        DisplayPixelCounts(27)
        DisplayPosX(12)
        DisplayPosY(14)

        DisplayWheel()

        pygame.display.update()
        clock.tick(60)


def RunApp():

    game_loop()
    pygame.quit()
    quit()


RunApp() # This is the actual call that calls the rest of the code