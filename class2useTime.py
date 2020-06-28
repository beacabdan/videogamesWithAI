import pygame
import math

pygame.init()
gameDisplay = pygame.display.set_mode((400, 400))

hand = pygame.image.load('assets/hand.png')
hand = pygame.transform.scale(hand, (50, 50))

while True:
    time = pygame.time.get_ticks() * 0.001

    gameDisplay.fill((0, 0, 0))

    gameDisplay.blit(hand, (50, 50))
    gameDisplay.blit(hand, (300, 300))

    gameDisplay.blit(hand, (int(175+100*math.sin(time)), int(175+100*math.cos(0.5*time))))
    print(time)
    pygame.display.update()

pygame.quit()
quit()