# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
try:
    pygame.init()
    a=pygame.font.get_default_font()
    print(a)
    screen = pygame.display.set_mode((640, 480), 0, 32)

    font = pygame.font.Font(a, 40)
    text_surface = font.render('lin', True, (0, 0, 255))

    x = 0
    y = (480 - text_surface.get_height())/2

    background = pygame.image.load('sushiplate.jpg')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.blit(background, (0, 0))

        x -= 2
        if x < -text_surface.get_width():
            x = 640 - text_surface.get_width()
        screen.blit(text_surface, (x, y))
        pygame.display.update()
except pygame.error as e:
    print('error is ', e)
    exit()
