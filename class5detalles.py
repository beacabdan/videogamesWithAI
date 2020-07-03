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


def carga_info(infomap):
    tablero = []
    with open(infomap) as csvfile:
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


def dibuja_tablero(tablero, zoom = 1):
    width = len(tablero[0])
    height = len(tablero)
    tile_size_x = int(config.display_width / width)
    tile_size_y = int(config.display_height / height)

    tile_size_x *= zoom
    tile_size_y *= zoom
    delayx = 0
    delayy = 0
    if zoom != 1:
        delayx = config.display_width//2 - player_pos[1]*tile_size_x
        delayy = config.display_height//2 - player_pos[0]*tile_size_y

    gameDisplay.fill(colours.darkgrey)
    for row in range(len(tablero)):
        for column in range(len(tablero[row])):
            tile_x = tablero[row][column] % 16
            tile_y = int(tablero[row][column] / 16)
            tile = pygame.transform.scale(tile_table[tile_x][tile_y], (tile_size_x, tile_size_y))
            gameDisplay.blit(tile, (column * tile_size_x + delayx, row * tile_size_y + delayy))


def dibuja_tablero_miniatura(delayx, delayy, size):
    width = len(tablero[0])
    height = len(tablero)
    tile_size_x = size // width
    tile_size_y = int(size / width * height) // height

    pygame.draw.rect(gameDisplay, colours.darkgrey, pygame.Rect(delayx, delayy, width*tile_size_x, height*tile_size_y))
    pygame.draw.rect(gameDisplay, colours.white, pygame.Rect(delayx, delayy, width * tile_size_x, height * tile_size_y), 3)

    for row in range(len(tablero)):
        for column in range(len(tablero[row])):
            tile_x = tablero[row][column] % 16
            tile_y = int(tablero[row][column] / 16)
            tile = pygame.transform.scale(tile_table[tile_x][tile_y], (tile_size_x, tile_size_y))
            if player_pos == [row, column]:
                tile = jugador
            gameDisplay.blit(tile, (column * tile_size_x + delayx, row * tile_size_y + delayy))


def dibuja_sprite(img, y, x, zoom = 1):
    img = pygame.transform.scale(img, (int(config.display_width / grid_width * zoom), int(config.display_height / grid_height * zoom)))
    if zoom == 1:
        gameDisplay.blit(img, (int(config.display_width / grid_width * x) * zoom,
                               int(config.display_height / grid_height * y) * zoom))  # pon un sprite en la posición xy
    else:
        gameDisplay.blit(img, (config.display_width //2, config.display_height //2 ))  # pon un sprite en la posición xy


def dibuja_sprite(img, y, x, zoom = 1):
    img = pygame.transform.scale(img, (int(config.display_width / grid_width * zoom), int(config.display_height / grid_height * zoom)))
    if zoom == 1:
        gameDisplay.blit(img, (int(config.display_width / grid_width * x) * zoom,
                               int(config.display_height / grid_height * y) * zoom))  # pon un sprite en la posición xy
    else:
        gameDisplay.blit(img, (config.display_width //2, config.display_height //2 ))  # pon un sprite en la posición xy


def mueve_player():
    steppable_tiles = [0, 1, 2]  # completadlo vosotros según vuestro tileset

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

    try:
        if tablero[x + deltax][y + deltay] in steppable_tiles:
            player_pos[0] += deltax
            player_pos[1] += deltay
    except:
        return

    player_pos[0] = max(0, min(player_pos[0], grid_height - 1))  # nos aseguramos de que esté dentro del rango (vert)
    player_pos[1] = max(0, min(player_pos[1], grid_width - 1))  # nos aseguramos de que esté dentro del rango (horz)


def ia_instrucciones():
    for i in range(len(info)):
        for j in range(len(info[0])):
            if info[i][j] == 3:
                if player_pos[0] < i and player_pos[1] == j:
                    return "El tesoro está hacia abajo"
                elif player_pos[0] > i and player_pos[1] == j:
                    return "El tesoro está hacia arriba"
                if player_pos[0] == i and player_pos[1] < j:
                    return "Ve hacia la derecha"
                elif player_pos[0] == i and player_pos[1] > j:
                    return "Tienes que ir hacia la izquierda"
    return None


def recoge_espada():
    print("Hace algo con la espada")


def muestra_logo_y_nombre():
    dibuja_tablero(tablero_logo)
    pygame.display.update()
    pygame.time.wait(500)


def rellena_con_objetivos(tablero):
    counter = 0
    mapa = []
    for row in tablero:
        mapa.append(row.copy())
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if mapa[i][j] == 0:
                if random.random() < 0.05:
                    mapa[i][j] = 3
                    counter += 1
    return mapa, counter


"""PROGRAMA"""

pygame.init()
# pygame.mixer.music.load('assets/foo.mp3')

tablero_logo, tile_table = carga_tablero('assets/mymapBea.csv', 'assets/tilesetChars.png')
tablero, tile_table = carga_tablero('assets/mymapCharsMap.csv', 'assets/tilesetChars.png')
info, contador_objetivos = rellena_con_objetivos(tablero)

grid_height = len(tablero)
grid_width = len(tablero[1])
config.display_height = int(config.display_width / grid_width * grid_height)
gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

jugador = tile_table[1][0]
jugador = pygame.transform.scale(jugador, (int(config.display_width / grid_width), int(config.display_height / grid_height)))

player_pos = [0, 0]  # generate a position for the player
puntuacion = 0
turno = 0
zoom = 1
contador_mensajes = 0
objetivo1 = [random.randint(0, 5),random.randint(10, 15)]
objetivo2 = [random.randint(0, 5),random.randint(10, 15)]


print(info)

muestra_logo_y_nombre()
# pygame.mixer.music.play(-1)

continue_playing = True
while continue_playing and contador_objetivos > 0:
    # GET USER INPUT
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            continue_playing = False
        if evento.type == pygame.KEYDOWN:
            mueve_player()
            if evento.key == pygame.K_SPACE:
                if zoom == 1:
                    zoom = 2
                else:
                    zoom = 1

    # ACTUALIZA
    direction = ia_instrucciones()
    if info[player_pos[0]][player_pos[1]] > 0:
        info[player_pos[0]][player_pos[1]] = 0
        puntuacion += 1
        if contador_mensajes > 0:
            contador_mensajes += 200
        else:
            contador_mensajes = 200
        contador_objetivos -= 1

    if player_pos == objetivo1:
        objetivo1 = [-1, -1]
        puntuacion += 1
        if contador_mensajes > 0:
            contador_mensajes += 200
        else:
            contador_mensajes = 200
        contador_objetivos -= 1

    if player_pos == objetivo2:
        objetivo2 = [random.randint(0, 5), random.randint(10, 15)]
        puntuacion += 1
        if contador_mensajes > 0:
            contador_mensajes += 200
        else:
            contador_mensajes = 200
        contador_objetivos -= 1


    # DRAW SCENE
    dibuja_tablero(tablero, zoom)
    dibuja_sprite(jugador, player_pos[0], player_pos[1], zoom)

    # si el zoom está activado, dibuja la miniatura en la esquina inferior derecha
    if zoom > 1:
        dibuja_tablero_miniatura(config.display_width - 210, config.display_height - 110, 200)

    if contador_mensajes > 0:
        escribe_texto("¡Has encontrado un tesoro!", config.display_width //2, config.display_height - 40)
    elif direction != None:
        escribe_texto(direction, config.display_width // 2, config.display_height - 40)
    else:
        escribe_texto("Quedan " + str(contador_objetivos) + " objetivos.", config.display_width // 2, config.display_height - 40)
    contador_mensajes -= 1
    print(contador_mensajes)

    mensaje = "Puntuación: " + str(puntuacion)
    escribe_texto(mensaje, config.display_width //2, config.display_height - 15)

    # UPDATE DISPLAY AND INCREASE TIME
    pygame.display.update()

muestra_logo_y_nombre()
pygame.quit()
quit()