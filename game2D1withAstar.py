import pygame
import random
import csv
import math
import pathfinding
from time import sleep


""" ARRIBA IMPORTS, ABAJO FUNCIONES """


def load_map(filename):
    map = []
    with open(filename) as csvfile:
        counter = 0
        reader = csv.reader(csvfile)
        for row in reader:
            if counter > 0:
                nrow = []
                for val in row:
                    if val == "0":
                        val = 64
                    nrow.append(int(val))
                map.append(nrow)
            counter += 1
    return map


def text_objects(text, font, colour = (0, 0, 0)):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def messageDisplay(text, pos, size = 20):
    largeText = pygame.font.Font('assets/Roboto-Regular.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = pos
    gameDisplay.blit(TextSurf, TextRect)


def load_tile_table(filename, width, height):
    image = pygame.image.load(filename)  # add .convert() at the end if you do not want to keep transparency
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, int(image_width/width)):
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(image_height/height)):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table


def update_player_pos(player, deltax, deltay):
    x = player[0]
    y = player[1]

    # 141 = water
    if map[round(y+deltay)][round(x+deltax)] in steppable_tiles:
        player[0] += deltax
        player[1] += deltay
    elif map[round(y)][round(x + deltax)] in steppable_tiles:
        player[0] += deltax
    elif map[round(y+deltay)][round(x)] in steppable_tiles:
        player[1] += deltay

    return player


def draw_image(player, player_facing_east):
    gameDisplay.fill(black)
    for row in range(len(map)):
        for column in range(len(map[row])):
            tile_x = map[row][column] % 16
            tile_y = int(map[row][column] / 16)
            tile = pygame.transform.scale(tile_table[tile_x][tile_y], (tile_size, tile_size))
            if map[row][column] == 137 and random.random() > 0.9:
                tile = pygame.transform.flip(tile, True, False)
            if map[row][column] == 117:
                ry = row - abs(math.sin(pygame.time.get_ticks() * 0.001 + column))
                gameDisplay.blit(tile, (column * tile_size, ry * tile_size))
                continue
            gameDisplay.blit(tile, (column * tile_size, row * tile_size))

    tile = pygame.transform.scale(tile_table[6][0], (tile_size, tile_size))
    if player_facing_east:
        tile = pygame.transform.flip(tile, True, False)
    gameDisplay.blit(tile, ((player[0]) * tile_size, (player[1]) * tile_size))


def use_a_star(x_change, y_change, player_facing_east, plan, step):
    finalizado = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizado = True
            print("Quit game.")



    return finalizado, x_change, y_change, x_change>0


def read_user_input(x_change, y_change, player_facing_east):
    finalizado = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizado = True
            print("Quit game.")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -increase
                player_facing_east = True
            elif event.key == pygame.K_RIGHT:
                x_change = increase
                player_facing_east = False
            elif event.key == pygame.K_DOWN:
                y_change = increase
            elif event.key == pygame.K_UP:
                y_change = -increase
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    return finalizado, x_change, y_change, player_facing_east


""" FUNCIONES ARRIBA, MAIN LOOP DEBAJO """


def game_loop():
    # INICIALIZAMOS LA APP
    pygame.display.set_caption('My game')
    clock = pygame.time.Clock()

    x_change = 0
    y_change = 0
    player = [15, 8]
    goal_x = 15
    goal_y = 22

    player_facing_east = True

    path = pathfinding.a_star(player[1], player[0], goal_x, goal_y, steppable_tiles, map)
    print(path, end="\n\n")
    step = 0

    # GAME LOOP
    finished = False
    while not finished:
        # DRAW THE FRAME WITH THE NEEDED TILES
        draw_image(player, player_facing_east)

        # READ USER INPUT
        # finished, x_change, y_change, player_facing_east = read_user_input(x_change, y_change, player_facing_east)
        # player = update_player_pos(player, x_change, y_change)

        if step > 0:
            if path != None and step < len(path):
                player = path[step]
            else:
                finished = True
        print(player, end=", ")
        step += 1

        sleep(0.5)

        # UPDATEAMOS EL DISPLAY Y AVANZAMOS EN EL TIEMPO
        pygame.display.update()
        clock.tick()


""" MAIN LOOP Y FUNCIONES ARRIBA, EL PROGRAMA DEBAJO """


if __name__ == "__main__":
    # ALTO Y ANCHO DE LA PANTALLA
    display_width = 640
    display_height = 640

    # LO DEJAREMOS COMO GLOBALES
    pygame.init()
    gameDisplay = pygame.display.set_mode((display_width, display_height))

    tile_table = load_tile_table('assets/tileset.png', 8, 8)
    tile_size = int(display_width/32)
    map = load_map('assets/mymap.csv')

    # none, floor, floor, door, door, bushes, bridge
    steppable_tiles = [18, 16, 3, 35, 70, 92]
    increase = 0.01

    # VARIABLES DE LA APP
    white = (255, 255, 255)
    black = (28, 30, 30)

    game_loop()
    pygame.quit()
    quit()