from PIL import Image
import colorsys
import math

if __name__ == "__main__":

    im = Image.new("RGB", (300, 300))
    radius = min(im.size) / 2.0
    centre = im.size[0] / 2, im.size[1] / 2
    pix = im.load()

    for x in range(im.width):
        for y in range(im.height):
            rx = x - centre[0]
            ry = y - centre[1]
            s = ((x - centre[0]) ** 2.0 + (y - centre[1]) ** 2.0) ** 0.5 / radius
            if s <= 1.0:
                h = ((math.atan2(ry, rx) / math.pi) + 1.0) / 2.0
                rgb = colorsys.hsv_to_rgb(h, s, 1.0)
                pix[x, y] = tuple([int(round(c * 255.0)) for c in rgb])
            else:
                pix[x, y] = (200, 200, 200)

    im.show()


#####################
import pygame
import time
import random
from PIL import Image
import colorsys
import math
import os



def colorWheel():

    imageObject = Image.new("RGB", (300, 300))
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

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

block_color = (53, 115, 255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Color visualizer')
clock = pygame.time.Clock()

pygameColorWheel = colorWheel()


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Pixels: " + str(count), True, black)
    gameDisplay.blit(text, (5, 5))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(pygameColorWheel, (100, 100))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(200)

    game_loop()


def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.LEFT:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        #
        # x += x_change
        gameDisplay.fill(white)
        #
        # # things(thingx, thingy, thingw, thingh, color)
        # things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        #
        # thing_starty += thing_speed
        # car(x, y)
        things_dodged(dodged)
        #
        # if x > display_width - car_width or x < 0:
        #     crash()
        #
        # if thing_starty > display_height:
        #     thing_starty = 0 - thing_height
        #     thing_startx = random.randrange(0, display_width)
        #     dodged += 1
        #     thing_speed += 1
        #     thing_width += (dodged * 1.2)
        #
        # if y < thing_starty + thing_height:
        #     print('y crossover')
        #
        #     if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
        #         print('x crossover')
        #         crash()

        car(0, 0)

        pygame.display.update()
        clock.tick(60)





print(colorWheel())
game_loop()
pygame.quit()
quit()