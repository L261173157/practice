import pygame
from pygame.locals import *
from sys import exit
from pygameobjects.Vec2d import *

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'
pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename)
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vec2d(100.0, 100.0)
heading = Vec2d(0, 0)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, position)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 参数前面加*意味着把列表或元组展开
    destination = Vec2d(*pygame.mouse.get_pos()) - Vec2d(*sprite.get_size()) / 2
    # 计算鱼儿当前位置到鼠标位置的向量
    vector_to_mouse = destination-position
    # 向量规格化
    vector_to_mouse.normalized()
    # 这个heading可以看做是鱼的速度，但是由于这样的运算，鱼的速度就不断改变了
    # 在没有到达鼠标时，加速运动，超过以后则减速。因而鱼会在鼠标附近晃动。
    heading =(vector_to_mouse * 1)

    position += heading * time_passed_seconds
    pygame.display.update()
