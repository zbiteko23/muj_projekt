
   #zaklady 
import sys
import pygame
import random

pygame.init()

# Velikost okna
rozliseni_okna = (800, 800)
okno = pygame.display.set_mode(rozliseni_okna)

# Pozice velkého čtverce
pozice_ctverce_x = 200
pozice_ctverce_y = 100
rychlost_ctverce = 0.5
velikost_ctverce = 20

# náhodné pozice malých čtverců
mala_ctverce = []
for _ in range(random.randint(5, 15)):
    mala_ctverce.append((random.randint(20, 780), random.randint(20, 780)))

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#pohyb
    stisknute_klavesy = pygame.key.get_pressed()

    if stisknute_klavesy[pygame.K_RIGHT]:
        pozice_ctverce_x += rychlost_ctverce
    if stisknute_klavesy[pygame.K_LEFT]:
        pozice_ctverce_x -= rychlost_ctverce
    if stisknute_klavesy[pygame.K_UP]:
        pozice_ctverce_y -= rychlost_ctverce
    if stisknute_klavesy[pygame.K_DOWN]:
        pozice_ctverce_y += rychlost_ctverce

#barva okna
    okno.fill((255, 255, 255))
    
    #vykresleni ctverce
    pygame.draw.rect(okno, (0, 0, 0), (pozice_ctverce_x, pozice_ctverce_y, velikost_ctverce, velikost_ctverce))

    # Vykreslení malých čtverců a detekce kolizí
    for maly_x, maly_y in mala_ctverce:
        pygame.draw.rect(okno, (255, 0, 0), (maly_x, maly_y, 15, 15))

        # Detekce kolize s malým čtvercem
        if (
            pozice_ctverce_x < maly_x + 15
            and pozice_ctverce_x + velikost_ctverce > maly_x
            and pozice_ctverce_y < maly_y + 15
            and pozice_ctverce_y + velikost_ctverce > maly_y
        ):
            print("Kolize s malým čtvercem!")
            
            # Zvětšení velkého čtverce a změna rychlosti
            velikost_ctverce += 5
            rychlost_ctverce -= 0.05

            # Zmizení malého čtverce
            mala_ctverce.remove((maly_x, maly_y))
            mala_ctverce.append((random.randint(20, 780), random.randint(20, 780)))

    pygame.display.update()