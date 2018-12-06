import pygame
import random
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.surf = pygame.image.load('jet.png').convert()
        # self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.rect = self.surf.get_rect(center=(400, 300))
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(400, 300))

    def update(self, pressed_keys):
        if pygame.key.get_pressed()[K_UP]:
            self.rect.move_ip(0, -1)
        if pygame.key.get_pressed()[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pygame.key.get_pressed()[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pygame.key.get_pressed()[K_RIGHT]:
            self.rect.move_ip(1, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


class Enemy(pygame.sprite.Sprite):
    number = 0

    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(random.randint(0, 780), 0))
        self.speed = random.randint(20, 50)

    def update(self, *args):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 600:
            self.kill()
            Enemy.number += 1

    @classmethod
    def num(cls):
        print('打到了', cls.number)


pygame.init()
screen = pygame.display.set_mode([800, 600])  # 设定一个窗口

Add_enemy = pygame.USEREVENT+1  # 添加敌人自定义事件
Enemy_move = pygame.USEREVENT+2  # 敌人移动
pygame.time.set_timer(Add_enemy, 500)  # 设置敌人出现时间
pygame.time.set_timer(Enemy_move, 100)  # 设置敌人出现时间


player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
new_enemy = Enemy()
while running:
    enemies.add(new_enemy)
    all_sprites.add(new_enemy)
    for event in pygame.event.get():
        if event.type == KEYDOWN:  # 检测键盘按下
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == Add_enemy:
            new_enemy = Enemy()
        elif event.type == Enemy_move:
            for enemy in enemies:
                enemy.update()
    pressed_keys1 = pygame.key.get_pressed()
    player.update(pressed_keys1)
    if pygame.sprite.spritecollideany(player, enemies):
        enemy.num()
        player.kill()
        running = False

    screen.fill((0, 0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()  # 显示出来




