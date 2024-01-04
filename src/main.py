import sys

import pygame
pygame.init()

okno = pygame.display.set_mode((800, 600))

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    okno.fill((255, 255, 255))
    
    pygame.display.update()
