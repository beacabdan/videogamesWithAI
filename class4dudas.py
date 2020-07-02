from random import randint
import pygame
import config
import csv
import colours
import math
import random

def carga_tablero(mapacsv, tileset):
    # instead of creating a board, we load it from a file
    tablero = []
    with open(mapacsv) as csvfile:
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
    # cargar el tile set (piezas del puzzle)
    image = pygame.image.load(tileset)  # add .convert() at the end if you do not want to keep transparency
    image_width, image_height = image.get_size()

    tile_size = image_width//16  # cambiad este número dependieno

    tile_table = []
    for tile_x in range(0, int(image_width / tile_size)):
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(image_height / tile_size)):
            rect = (tile_x * tile_size, tile_y * tile_size, tile_size, tile_size)
            line.append(image.subsurface(rect))

    return tablero, tile_table

def carga_info():
    tablero = []
    with open('assets/mymapCharsMap.csv') as csvfile:
        counter = 0
        reader = csv.reader(csvfile)
        for row in reader:
            if counter > 0:  # skip first line
                nrow = []
                for val in row:
                    nrow.append(int(val))
                tablero.append(nrow)
            counter += 1
    return tablero

def escribe_texto(texto, x, y, size = 20):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf = largeText.render(texto, True, colours.white)
    TextRect = TextSurf.get_rect()
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def dibuja_tablero():
    width = len(tablero[0])
    height = len(tablero)
    tile_size_x = int(config.display_width / width)
    tile_size_y = int(config.display_height / height)

    gameDisplay.fill(colours.darkgrey)
    for row in range(len(tablero)):
        for column in range(len(tablero[row])):
            tile_x = tablero[row][column] % 16
            tile_y = int(tablero[row][column] / 16)
            tile = pygame.transform.scale(tile_table[tile_x][tile_y], (tile_size_x, tile_size_y))
            gameDisplay.blit(tile, (column * tile_size_x, row * tile_size_y))

def dibuja_sprite(img, y, x):
    gameDisplay.blit(img, (int(config.display_width / grid_width * x), int(config.display_height / grid_height * y)))  # pon un sprite en la posición xy

def mueve_player(turno = 0):
    steppable_tiles = [0, 16, 18, 3, 35]  # completadlo vosotros según vuestro tileset

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
    elif evento.key == pygame.K_a:
        deltay = -1  # mueve izquerda (x decrece)
    elif evento.key == pygame.K_d:
        deltay = 1  # mueve derecha (x augmenta)
    elif evento.key == pygame.K_w:
        deltax = -1  # mueve arriba (y decrece)
    elif evento.key == pygame.K_s:
        deltax = 1  # muebe abajo (y augmenta)

    x = player_pos[0]
    y = player_pos[1]

    try:
        if tablero[x + deltax][y + deltay] in steppable_tiles:
            player_pos[0] += deltax
            player_pos[1] += deltay
    except:
        return

    player_pos[0] = max(0, min(player_pos[0], grid_height - 1))  # nos aseguramos de que esté dentro del rango (vert)
    player_pos[1] = max(0, min(player_pos[1], grid_width - 1))  # nos aseguramos de que esté dentro del rango (horz)

def ia_algo():
    if random.random() > 0.3:
        npc_pos[0] += 1
    elif random.random() > 0.3:
        npc_pos[0] -= 1
    else:
        return

def recoge_espada():
    print("Hace algo con la espada")

def muestra_logo_y_nombre():
    return None

"""PROGRAMA"""


pygame.init()

# importado el tablero
tablero, tile_table = carga_tablero('assets/mymap.csv', 'assets/tileset.png')
grid_height = len(tablero)
grid_width = len(tablero[0])

# creado la ventana
config.display_height = int(config.display_width / grid_width * grid_height)
gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

# creado la imagen del jugador
jugador = tile_table[5][0]
npc = tile_table[6][0]
jugador = pygame.transform.scale(jugador, (int(config.display_width / grid_width), int(config.display_height / grid_height)))
npc = pygame.transform.scale(npc, (int(config.display_width / grid_width), int(config.display_height / grid_height)))

# posiciones, puntuaciones, etc
player_pos = [0, 0]  # generate a position for the player
npc_pos = [1, 0]  # generate a position for the player
puntuacion = 0
turno = 0

continue_playing = True
while continue_playing:  # se sale cuando continue_playing == False
    # GET USER INPUT
    for evento in pygame.event.get():  # por cada evento de la lista de eventos
        if evento.type == pygame.QUIT:  # si el evento es de tipo quit
            continue_playing = False  # sal del bucle
        if evento.type == pygame.KEYDOWN:
            mueve_player()
            if turno == 0:
                turno = 1
            else:
                turno = 0
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Ha hecho click")
            recoge_espada()

    # UPDATE SCENE
    # según vuestras reglas, la puntuación cambiará o no
    # si el jugador toca al npc entonces lo mata y el npc aparece en otro sitio
    if turno == 0:
        if player_pos == npc_pos:
            puntuacion += 2
            npc_pos = [random.randint(0, 5), random.randint(0, 20)]
    else:
        ia_algo()
        turno = 0

    # DRAW SCENE
    dibuja_tablero()
    dibuja_sprite(jugador, player_pos[0], player_pos[1])
    dibuja_sprite(npc, npc_pos[0], npc_pos[1])

    mensaje = "Puntuación: " + str(puntuacion)
    escribe_texto(mensaje, config.display_width //2, config.display_height - 15)

    # UPDATE DISPLAY AND INCREASE TIME
    pygame.display.update()


escribe_texto("Se ha salido del bucle principal", 100, 100)
pygame.display.update()  # necesario para ver el mensaje o cualquier cambio en la pantalla
pygame.time.wait(500)  # para que no se cierre inmediatamente

pygame.quit()
quit()