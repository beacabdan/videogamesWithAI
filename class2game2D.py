from random import randint
import pygame
import config
import colours

pygame.init()
gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

# width and height of the 2D board
width = 8
height = 10

# create a board using the width and height variables
tablero = []
for i in range(height):
    row = [-1]*width
    tablero.append(row)

# generate a random position for the player and the food and place both in the 2d board
player_pos = [randint(0, height-1), randint(0, width-1)]
objetivo_pos = [randint(0, height-1), randint(0, width-1)]
tablero[objetivo_pos[0]][objetivo_pos[1]] = 2
tablero[player_pos[0]][player_pos[1]] = 1
puntuacion = 0

continue_playing = True
while continue_playing:
    # GET USER INPUT
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            continue_playing = False  # saldremos del bucle principal en la siguiente iteración
        elif evento.type == pygame.KEYDOWN:
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

    # UPDATE SCENE
    # si player llega al objetivo, genera un nuevo objetivo
    if player_pos == objetivo_pos:
        objetivo_pos = [randint(0, height - 1), randint(0, width - 1)]  #posición xy aleatoria
        puntuacion += 1  # sumarle 1 a la puntuación
        print("Score:", puntuacion)

    # DRAW SCENE
    gameDisplay.fill( (255, 255, 255) )

    # dibuja una cuadrícula numerada
    for j in range(1, len(tablero) + 1):
        pygame.draw.line(gameDisplay, colours.black, (0, int(config.display_height / height * j)),
                         (config.display_width, int(config.display_height / height * j)))  # líneas horizontales (filas)
    for i in range(1, len(tablero[0])+1):
        pygame.draw.line(gameDisplay, colours.black, (int(config.display_width / width * i), 0),
                         (int(config.display_width / width * i), config.display_height))  # líneas verticales (columnas)
    for j in range(len(tablero)):
        for i in range(len(tablero[0])):
            largeText = pygame.font.Font('assets/Roboto-Regular.ttf', 10)
            TextSurf = largeText.render(str(i)+","+str(j), True, colours.black)
            TextRect = TextSurf.get_rect()
            TextRect.center = (int((i+0.5)*config.display_width/width), int((j+0.5)*config.display_height/height))
            gameDisplay.blit(TextSurf, TextRect)
    pygame.draw.circle(gameDisplay, colours.red, (int(config.display_width / width * (player_pos[1] + 0.5)), int(config.display_width / height * (player_pos[0] + 0.5))), 10)
    pygame.draw.circle(gameDisplay, colours.green, (int(config.display_width / width * (objetivo_pos[1] + 0.5)), int(config.display_width / height * (objetivo_pos[0] + 0.5))), 15)

    # UPDATE DISPLAY AND INCREASE TIME
    pygame.display.update()
    pygame.time.delay(200)


pygame.quit()
quit()