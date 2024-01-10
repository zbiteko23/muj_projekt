import sys

import pygame
pygame.init()

import random

#velikost okna
rozliseni_okna = (800, 800)

okno = pygame.display.set_mode(rozliseni_okna)

#pozice ctverce
pozice_ctverce_x = 500
pozice_ctverce_y = 100

#ryclost ctverce
rychlost_ctverce = 0.2

#nahodna pozice ctevercku
def random_pozice():
    x = random.randint(0, -20)
    y = random.randint(0, -20)
    return x, y


#ukonceni hry
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
#pohyb ctverce
    stisknute_klavesy = pygame.key.get_pressed()
    
    if stisknute_klavesy[pygame.K_RIGHT]:
        pozice_ctverce_x += rychlost_ctverce
        
    if stisknute_klavesy[pygame.K_LEFT]:
        pozice_ctverce_x -= rychlost_ctverce
        
    if stisknute_klavesy[pygame.K_UP]:
        pozice_ctverce_y -= rychlost_ctverce
        
    if stisknute_klavesy[pygame.K_DOWN]:
        pozice_ctverce_y += rychlost_ctverce
            
#vytvoreni malych cteverku
    pygame.draw.rect(okno, (x, y, 15, 15))
        
    
    
#barva okna
    okno.fill((255, 255, 255))
    
#vytvoreni ctverce
    pygame.draw.rect(okno, (0, 0, 0), (pozice_ctverce_x, pozice_ctverce_y, 20, 20))
    
#vytvoreni malych ctvercu
    
    
    pygame.display.update()
