from random import randint
import pygame
import config
import colours

pygame.init()
gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))
tablero2D = pygame.image.load('assets/tableroMuestra.png')
tableroGame2D = pygame.transform.scale(tablero2D, (config.display_width, config.display_height))

# width and height of the 2D board
width = 16
height = 16

# create a board using the width and height variables
tablero = []
for i in range(height):
    row = [-1]*width
    tablero.append(row)

# generate a random position for the player and the food and place both in the 2d board
player_pos = [0, 0]  # TODO: random xy player position (first value is fila, second is column)
objetivo_pos = [0, 0]  # TODO: random xy food position (first value is fila, second is column)
puntuacion = 0

show_grid = False
continue_playing = True
while continue_playing:
    # GET USER INPUT
    for evento in pygame.event.get():
        # TODO: si evento es quit, saldremos del bucle principal en la siguiente iteración
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                show_grid = True  # when space is pressed, show grid
            # TODO: si flecha derecha, mueve hacia derecha (x augmenta)
            # TODO: si flecha arriba, mueve hacia arriba (y decrece)
            # TODO: si flecha abajo, mueve abajo (y augmenta)
            player_pos[0] = max(0, min(player_pos[0], height - 1))  # nos aseguramos de que esté dentro del rango (vert)
            player_pos[1] = max(0, min(player_pos[1], width - 1))  # nos aseguramos de que esté dentro del rango (horz)
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_SPACE:
                show_grid = False  # when space is released, hide grid

    # UPDATE SCENE
    # si player llega al objetivo, genera un nuevo objetivo
    if player_pos == objetivo_pos:
        objetivo_pos = [0, 0]  # TODO: random xy food position (first value is the row, second is column)
        # TODO: pon un 2 en xy del objetivo con tablero[fila objetivo][columna objetivo] (un 2 representa al objetivo)
        # TODO: suma uno a la puntuación

    # DRAW SCENE
    gameDisplay.blit(tableroGame2D, (0, 0))

    # when space is pressed, show grid
    if show_grid:
        for j in range(1, len(tablero) + 1):
            pygame.draw.line(gameDisplay, colours.grey, (0, int(config.display_height / height * j)),
                             (config.display_width, int(config.display_height / height * j)))  # líneas horizontales (filas)
        for i in range(1, len(tablero[0])+1):
            pygame.draw.line(gameDisplay, colours.grey, (int(config.display_width / width * i), 0),
                             (int(config.display_width / width * i), config.display_height))  # líneas verticales (columnas)
        for j in range(len(tablero)):
            for i in range(len(tablero[0])):
                largeText = pygame.font.Font('assets/Roboto-Regular.ttf', 10)
                TextSurf = largeText.render(str(i)+","+str(j), True, colours.grey)
                TextRect = TextSurf.get_rect()
                TextRect.center = (int((i+0.5)*config.display_width/width), int((j+0.5)*config.display_height/height))
                gameDisplay.blit(TextSurf, TextRect)
    # TODO: pon un sprite en la posición del jugador
    # TODO: pon otro sprite en la posición del objetivo
    # TODO: muestra la puntuación por pantalla

    # UPDATE DISPLAY AND INCREASE TIME
    pygame.display.update()


pygame.quit()
quit()