import colours
import pygame

# WINDOW SIZE
display_width = 640
display_height = 640

# SPRITES AND MORE
handImg = pygame.image.load('assets/hand.png')

# FOR THE TRIVIAL
center_message = (display_width//2, 3*display_height//7)
colors_tauler = [(200,0,0), (0,200,0), (0,0,200), (200,200,0), (0,200,200), (200,0,200), (200,100,100), (100,200,100), (100,100,200), colours.grey]
temas_tauler = ["Matemáticas", "Arte y literatura", "Pelis y TV", "Ciencia", "Tecnología", "Música"]
game_version = 0