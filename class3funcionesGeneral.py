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

def escribe_texto(texto, x, y, size = 20):
    largeText = pygame.font.Font('assets/Roboto-Regular.ttf', size)
    TextSurf = largeText.render(texto, True, colours.white)
    TextRect = TextSurf.get_rect()
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def dibuja_tablero():
    gameDisplay.fill(colours.darkgrey)
    for row in range(len(tablero)):
        for column in range(len(tablero[row])):
            tile_x = tablero[row][column] % 16
            tile_y = int(tablero[row][column] / 16)
            tile = pygame.transform.scale(tile_table[tile_x][tile_y], (tile_size, tile_size))
            gameDisplay.blit(tile, (column * tile_size, row * tile_size))

def dibuja_sprite(img, y, x):
    gameDisplay.blit(img, (config.display_width / width * x, config.display_height / height * y))  # pon un sprite en la posición xy

def mueve_player():
    steppable_tiles = [18, 16, 3, 35, 70, 92, 69]

    deltax = 0
    deltay = 0

    if evento.key == pygame.K_LEFT:
        deltay = -1  # mueve izquerda (x decrece)
    elif evento.key == pygame.K_RIGHT:
        deltay = 1  # mueve derecha (x augmenta)
    elif evento.key == pygame.K_UP:
        deltax = -1  # mueve arriba (y decrece)
    elif evento.key == pygame.K_DOWN:
        deltax = 1  # muebe abajo (y augmenta)

    x = player_pos[0]
    y = player_pos[1]
    print(player_pos, "antes", tablero[x][y])

    try:
        if tablero[x + deltax][y + deltay] in steppable_tiles:
            player_pos[0] += deltax
            player_pos[1] += deltay
    except:
        return

def ia_algo():
    print("Hola")

def recoge_espada():
    print("Hace algo con la espada")

def muestra_logo_y_nombre():
    return None

"""PROGRAMA"""


pygame.init()
gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

tablero, tile_table = carga_tablero()
height = len(tablero)
width = len(tablero[1])
tile_size = int(config.display_width / width)

jugador = tile_table[5][0]
jugador = pygame.transform.scale(jugador, (int(config.display_width/width), int(config.display_height/height)))

# generate a random position for the player and the food and place both in the 2d board
player_pos = [5, 5]
puntuacion = 0
turno = 0

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
    if turno == 0:
        puntuacion += 2
        turno = 1
    else:
        turno = 0

    # DRAW SCENE
    dibuja_tablero()
    dibuja_sprite(jugador, player_pos[0], player_pos[1])

    mensaje = "La puntuación es: " + str(puntuacion)
    escribe_texto(mensaje, config.display_width//2, 100)

    # UPDATE DISPLAY AND INCREASE TIME
    pygame.display.update()


pygame.quit()
quit()