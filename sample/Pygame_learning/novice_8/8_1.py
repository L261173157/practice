import pygame
from pygame.locals import *

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename)
sprite = pygame.image.load(sprite_image_filename)
clock = pygame.time.Clock()
x = 0
y = 0
speed_x = 250
speed_y = 200

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))
    time_passed = clock.tick()
    time_passed_second = time_passed / 1000
    distance_x = speed_x * time_passed_second
    distance_y = speed_y * time_passed_second
    x += distance_x
    y += distance_y
    if x >= (640-150) or x <= 0:
        speed_x = -speed_x
    if y >= (480-122) or y <= 0:
        speed_y = -speed_y
    pygame.display.update()
