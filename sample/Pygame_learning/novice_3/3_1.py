background_image_filename = 'sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename)

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print('exit')
            exit()
        if event.type == KEYDOWN:
            print('you have press')
            if event.key == K_f:
                print('you have press f')
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((640, 480), 0, 32)
    screen.blit(background, (0, 0))
    pygame.display.update()

