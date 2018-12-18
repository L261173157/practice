import pygame
import random
from pygame.locals import *
from pygameobjects.Vec2d import *

pygame.init()

screen = pygame.display.set_mode((800, 480), 0, 32)
background_image = pygame.image.load('background.png')


class Player(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('airplane.png')
        self.speed = speed
        self.pos = Vec2d((400 - self.image.get_width() / 2), (240 - self.image.get_height() / 2))

    def update(self, time_passed_sce):
        airplane_dir = Vec2d(*pygame.mouse.get_pos()) - (
            (self.pos.x + self.image.get_width() / 2), (self.pos.y + self.image.get_height() / 2))
        airplane_dir.normalized()
        self.pos += airplane_dir * self.speed * time_passed_sce


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type):
        pygame.sprite.Sprite.__init__(self)
        self.type = enemy_type
        if self.type == 1:
            self.image = pygame.image.load('enemy1.png')
            self.pos = Vec2d(random.randint(0, (800 - self.image.get_width() / 2)), 0)
        elif self.type == 2:
            self.image = pygame.image.load('enemy2.png')
            self.pos = Vec2d(random.randint(0, (800 - self.image.get_width() / 2)), 0)
        elif self.type == 3:
            self.image = pygame.image.load('enemy3.png')
            self.pos = Vec2d(random.randint(0, (800 - self.image.get_width() / 2)), 0)

    def update(self, time_passed_sce):
        if self.type == 1:
            enemy_dir = Vec2d(0, 10)
            enemy_dir.normalized()
            self.pos += enemy_dir * 10 * time_passed_sce
        if self.type == 2:
            enemy_dir = Vec2d(0, 1)
            enemy_dir.normalized()
            self.pos += enemy_dir * 10 * time_passed_sce
        if self.type == 3:
            enemy_dir = Vec2d(0, 1)
            enemy_dir.normalized()
            self.pos += enemy_dir * 10 * time_passed_sce


clock = pygame.time.Clock()
Add_enemy = pygame.USEREVENT + 1
pygame.time.set_timer(Add_enemy, 1000)

player = Player(10)
enemy1 = Enemy(1)
enemys = pygame.sprite.Group()
all_sprite = pygame.sprite.Group()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == Add_enemy:
            enemy1 = Enemy(1)

    enemys.add(enemy1)
    all_sprite.add(enemys, player)
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    all_sprite.update(time_passed_seconds)

    screen.blit(background_image, (0, 0))
    for sprite in all_sprite:
        screen.blit(sprite.image, sprite.pos)

    pygame.display.update()
