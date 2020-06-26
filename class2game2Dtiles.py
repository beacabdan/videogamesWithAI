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
player_pos = [0, 0]  # TODO: random xy player position (first value is fila, second is column)
objetivo_pos = [0, 0]  # TODO: random xy food position (first value is fila, second is column)
puntuacion = 0

continue_playing = True
while continue_playing:
    # GET USER INPUT
    for evento in pygame.event.get():
        # TODO: si evento es quit, saldremos del bucle principal en la siguiente iteración
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_pos[1] -= 1  # mueve izquerda (x decrece)
            # TODO: si flecha derecha, mueve hacia derecha (x augmenta)
            # TODO: si flecha arriba, mueve hacia arriba (y decrece)
            # TODO: si flecha abajo, mueve abajo (y augmenta)
            player_pos[0] = max(0, min(player_pos[0], height - 1))  # nos aseguramos de que esté dentro del rango (vert)
            player_pos[1] = max(0, min(player_pos[1], width - 1))  # nos aseguramos de que esté dentro del rango (horz)

    # UPDATE SCENE
    # si player llega al objetivo, genera un nuevo objetivo
    if player_pos == objetivo_pos:
        objetivo_pos = [0, 0]  # TODO: random xy food position (first value is the row, second is column)
        # TODO: pon un 2 en xy del objetivo con tablero[fila objetivo][columna objetivo] (un 2 representa al objetivo)
        # TODO: suma uno a la puntuación

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

    # TODO: pon un sprite en la posición del jugador
    # TODO: pon otro sprite en la posición del objetivo
    # TODO: muestra la puntuación por pantalla

    # UPDATE DISPLAY AND INCREASE TIME
    pygame.display.update()


pygame.quit()
quit()