from random import randint
import pygame
import config
import csv
import colours
import math
import random

pygame.init()
gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

# instead of creating a board, we load it from a file
tablero = []
with open('assets/mymap1.csv') as csvfile:
    counter = 0
    reader = csv.reader(csvfile)
    for row in reader:
        if counter > 0:  # skip first line
            nrow = []
            for val in row:
                nrow.append(int(val))
            tablero.append(nrow)
        counter += 1

# width and height of the 2D board
width = len(tablero[0])
height = len(tablero)
tile_size = int(config.display_width/width)

# cargar el tile set (piezas del puzzle)
image = pygame.image.load('assets/tileset.png')  # add .convert() at the end if you do not want to keep transparency
image_width, image_height = image.get_size()
tile_table = []
for tile_x in range(0, int(image_width/8)):
    line = []
    tile_table.append(line)
    for tile_y in range(0, int(image_height/8)):
        rect = (tile_x*8, tile_y*8, 8, 8)
        line.append(image.subsurface(rect))

# generate a random position for the player and the food and place both in the 2d board
player_pos = [randint(0, height-1), randint(0, width-1)]
old_player_pos = [player_pos[0], player_pos[1]]
objetivo_pos = [randint(0, height-1), randint(0, width-1)]
puntuacion = 0
lerp = 0

continue_playing = True
while continue_playing:
    # GET USER INPUT
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            continue_playing = False  # saldremos del bucle principal en la siguiente iteración
        elif evento.type == pygame.KEYDOWN:
            lerp = 0
            old_player_pos = [player_pos[0], player_pos[1]]
            if evento.key == pygame.K_LEFT:
                player_pos[1] -= 1  # mueve izquerda (x decrece)
            elif evento.key == pygame.K_RIGHT:
                player_pos[1] += 1  # mueve derecha (x augmenta)
            elif evento.key == pygame.K_UP:
                player_pos[0] -= 1  # mueve arriba (y decrece)
            elif evento.key == pygame.K_DOWN:
                player_pos[0] += 1  # muebe abajo (y augmenta)
            player_pos[0] = max(0, min(player_pos[0], height - 1))  # nos aseguramos de que esté dentro del rango (vert)
            player_pos[1] = max(0, min(player_pos[1], width - 1))  # nos aseguramos de que esté dentro del rango (horz)

    lerp += 0.05
    lerp = min(lerp, 1)

    # UPDATE SCENE
    # si player llega al objetivo, genera un nuevo objetivo
    if player_pos == objetivo_pos:
        objetivo_pos = [randint(0, height - 1), randint(0, width - 1)]  #posición xy aleatoria
        puntuacion += 1  # sumarle 1 a la puntuación
        print("Score:", puntuacion)

    # DRAW SCENE
    gameDisplay.fill( (255, 255, 255) )

    # dibuja una cuadrícula numerada
    gameDisplay.fill(colours.darkgrey)
    for row in range(len(tablero)):
        for column in range(len(tablero[row])):
            tile_x = tablero[row][column] % 16
            tile_y = int(tablero[row][column] / 16)
            tile = pygame.transform.scale(tile_table[tile_x][tile_y], (tile_size, tile_size))
            gameDisplay.blit(tile, (column * tile_size, row * tile_size))

    playerx = config.display_width / width * (player_pos[1] + 0.5) - 25
    playery = config.display_width / height * (player_pos[0] + 0.5) - 25
    oldplayerx = config.display_width / width * (old_player_pos[1] + 0.5) - 25
    oldplayery = config.display_width / height * (old_player_pos[0] + 0.5) - 25
    gameDisplay.blit(config.handImg, (int(playerx * lerp + oldplayerx*(1 - lerp)), int(playery * lerp + oldplayery*(1 - lerp))))
    gameDisplay.blit(config.handGreenImg, (int(config.display_width / width * (objetivo_pos[1] + 0.5) - 25),
                                           int(config.display_width / height * (objetivo_pos[0] + 0.5)) - 25))

    # UPDATE DISPLAY AND INCREASE TIME
    pygame.display.update()



pygame.quit()
quit()