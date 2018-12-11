import pygame


pygame.init()

screen = pygame.display.set_mode((640, 480))

all_colors = pygame.Surface((4096, 4096), depth=24)

for r in range(256):
    y = (r // 16)
    x = (r - 16 * y)
    y=y*256
    x=x*256
    print(x,y)
    for g in range(256):
        for b in range(256):
            all_colors.set_at((x+g, y+b), (r, g, b))
pygame.image.save(all_colors, 'allcolors.png')

