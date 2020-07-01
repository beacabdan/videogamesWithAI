from random import randint
import pygame
import config
import csv
import colours
import math
import random

def carga_tablero():
    # instead of creating a board, we load it from a file
    tablero = []
    with open('assets/mymap.csv') as csvfile:
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
    tile_size = int(config.display_width / width)

    # cargar el tile set (piezas del puzzle)
    image = pygame.image.load(
        'assets/tilesetOriginal.png')  # add .convert() at the end if you do not want to keep transparency
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, int(image_width / 8)):
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(image_height / 8)):
            rect = (tile_x * 8, tile_y * 8, 8, 8)
            line.append(image.subsurface(rect))

    return tablero, tile_table

def dibuja_tablero():
    gameDisplay.fill(colours.darkgrey)
    for row in range(len(tablero)):
        for column in range(len(tablero[row])):
            tile_x = tablero[row][column] % 16
            tile_y = int(tablero[row][column] / 16)
            tile = pygame.transform.scale(tile_table[tile_x][tile_y], (tile_size, tile_size))
            gameDisplay.blit(tile, (column * tile_size, row * tile_size))

def dibuja_jugador():
    gameDisplay.blit(config.handImg, (config.display_width / width * player_pos[1],
                                      config.display_height / height * player_pos[
                                          0]))  # pon un sprite en la posición del jugador

def escribe_texto(texto, x, y):
    largeText = pygame.font.Font('assets/Roboto-Regular.ttf', 25)
    TextSurf = largeText.render(texto, True, colours.white)
    TextRect = TextSurf.get_rect()
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def mueve_player():
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

def ia_algo():
    print("Hola")

"""PROGRAMA"""

pygame.init()
gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

tablero, tile_table = carga_tablero()
height = len(tablero)
width = len(tablero[1])
tile_size = int(config.display_width / width)

# generate a random position for the player and the food and place both in the 2d board
player_pos = [randint(0, height-1), randint(0, width-1)]
puntuacion = 0
tiles_pisables = [16, 18, 3, 35]

continue_playing = True
while continue_playing:
    # GET USER INPUT
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            continue_playing = False
        if evento.type == pygame.KEYDOWN:
            mueve_player()

    # UPDATE SCENE
    # según vuestras reglas, la puntuación cambiará o no

    puntuacion += 2

    # DRAW SCENE
    dibuja_tablero()
    dibuja_jugador()
    mensaje = "La puntuación es: " + str(puntuacion)
    escribe_texto(mensaje, config.display_width//2, 100)

    # UPDATE DISPLAY AND INCREASE TIME
    pygame.display.update()


pygame.quit()
quit()