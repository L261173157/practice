# -*- coding: utf-8 -*-
my_name = 'lin'

import pygame


pygame.init()
my_font = pygame.font.SysFont('my_font.ttf', 64)
name_surface = my_font.render(my_name, True, (0, 0, 0),(255, 255, 255))
pygame.image.save(name_surface, 'name.jpg')  # 保存图片

