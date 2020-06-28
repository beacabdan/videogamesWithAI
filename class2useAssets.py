import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((200, 800))

hand = pygame.image.load('assets/hand.png')
hand = pygame.transform.scale(hand, (100, 100))

while True:
    gameDisplay.blit(hand, (100, 200))
    gameDisplay.blit(hand, (100, 400))
    pygame.display.update()

pygame.quit()
quit()