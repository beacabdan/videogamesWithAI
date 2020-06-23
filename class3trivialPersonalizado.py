import pygame
import random
import math
import csv

import config
import colours


""" ARRIBA IMPORTS; DEBAJO FUNCIONES """


def carga_base_datos(filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            nrow = []
            for val in row:
                nrow.append(val)
            data.append(nrow)
    return data


def escribe_texto(text, pos=(config.display_width//2, config.display_height//2), size=20, colour=(0, 0, 0)):
    largeText = pygame.font.Font('assets/Roboto-Regular.ttf', size)
    TextSurf = largeText.render(text, True, colour)
    TextRect = TextSurf.get_rect()
    TextRect.center = pos
    gameDisplay.blit(TextSurf, TextRect)


# retorna la suma de N daus
def lanzar_dados(N=1):
    # TODO: genera N números aleatorios entre 1 y 6 (o más, depende del dado)
    return 0


# crea todas las casillas en forma de polígono regular y devuelve una lista de las posiciones
def inicializar_tablero(sides=6, casillas=6):
    tablero = []

    # calcular la posición del tablero en el centro de la pantalla
    centerx = config.display_width//2
    centery = config.display_height//2
    diam_centre = min(centerx, centery) * 0.8

    # por cada lado del tablero (de quesito a quesito)
    for i in range(sides):
        origin_x = centerx + diam_centre * math.sin(i * 2 * math.pi / sides + math.pi)
        origin_y = centery + diam_centre * math.cos(i * 2 * math.pi / sides + math.pi)
        end_x = centerx + diam_centre * math.sin((i+1) * 2 * math.pi / sides + math.pi)
        end_y = centery + diam_centre * math.cos((i+1) * 2 * math.pi / sides + math.pi)
        # por cada casilla de cada lado del tablero
        for j in range(casillas):
            linear_interpolation = j/casillas
            tablero.append((int(origin_x * (1 - linear_interpolation) + end_x * linear_interpolation),
                              int(origin_y * (1 - linear_interpolation) + end_y * linear_interpolation),
                              i % sides if j == 0 else (j + i) % sides if j != casillas // 2 else -1))

    # tablero es una lista de casillas, cada casilla es una posición x, y + una categoría
    return tablero


# dibuixa el tauler guardat a la matriu de posicions
def dibuja_tablero(positions, sides=6):
    # cálculos para el tamaño de las casillas
    centerx = config.display_width // 2
    centery = config.display_height // 2
    casillas = len(positions)//sides
    endx = centerx + min(centerx, centery) * 0.8 * math.sin(2 * math.pi / sides)
    endy = centery + min(centerx, centery) * 0.8 * math.cos(2 * math.pi / sides)
    side_len = math.sqrt((centerx - endx) ** 2 + ((centery + centerx * 0.8) - endy) ** 2)

    # TODO: dibujar el tablero
    # TODO: escribir los nombres de las categorias (con el color que pertoca)
    return None


def dibuja_tablero_image():
    # TODO: dibuja la imagen del tablero (en assets)
    return None


def dibuja_jugador(casilla, jugador):
    # TODO: dibuja al jugador en la casilla
    return None


def dibuja_dado(N=1):
    # TODO: if state == 0, dibujar n dados o algo
    return None


def dibuja_barra_tiempo(maxTime, elapsedTime):
    wasted = max((maxTime - elapsedTime) / maxTime, 0)
    pygame.draw.line(gameDisplay, (colours.grey[0], colours.grey[1]*wasted**0.5, colours.grey[2]*wasted**0.5), (0, 4), (wasted*config.display_width, 4), 10)


def generar_pregunta(tauler, position, data):
    categoria = tauler[position][2]  # de qué color es la casilla en que hemos caído?
    random.shuffle(data)  # mezclamos las respuestas para que no salga la correcta siempre en el mismo sitio

    # TODO: genera las preguntas (el tipo debería ser aleatorio), si la casilla es vuelve a tirar... ¿qué?
    return None


def dibuja_2o4_botones(answers, mouse=False):
    button_halfsizex = config.display_width//7
    button_halfsizey = config.display_height//28
    displacementx = button_halfsizex + 10
    displacementy = button_halfsizey + 10
    centerx = config.display_width // 2
    centery = 4 * config.display_height // 7

    # TODO: Dibuja los botones y devuelve cuál se ha presionado
    return None


# código de https://pythonprogramming.net/placing-text-pygame-buttons/?completed=/making-interactive-pygame-buttons/
def button(msg, x, y, w, h, ic):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, ic, (x - w // 2, y - h // 2, w, h))

    if x+w//2 > mouse[0] > x-w//2 and y+h//2 > mouse[1] > y-h//2:
        escribe_texto(msg, (x, y), 25, colours.white)
        if click[0] == 1:
            return True
    else:
        escribe_texto(msg, (x, y), 20, colours.white)
    return False


""" ARRIBA FUNCIONES; DEBAJO MAIN LOOP"""


def game_loop():
    # el tiempo empieza cuando empieza el juego
    clock = pygame.time.Clock()
    timer_start = pygame.time.get_ticks()

    # creamos el tablero y cargamos los datos al empezar el juego
    tauler = inicializar_tablero()
    data = carga_base_datos("assets/datos_trivial.csv")

    # posiciones iniciales de los jugadores aleatorias
    player_a = random.randint(0, len(tauler)-1)
    player_b = random.randint(0, len(tauler)-1)
    turn_a = True  # siempre empieza a jugar el jugador A

    # valores por defecto
    state = -1
    timer = 10000
    respuesta_user = None
    respuesta_correcta = None
    message = ""

    # booleanos de control
    click = False
    change_state = True

    # game loop
    closed = False
    while not closed:
        # GET USER INPUT -----------------------------------------------------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
            if event.type == pygame.MOUSEBUTTONDOWN and click == False:
                click = True

        # lógica del cambio de estado
        if pygame.time.get_ticks() - timer_start > timer or click and state == 0 or change_state:
            timer_start = pygame.time.get_ticks()
            state = (state + 1) % 3
            change_state = False
            click = False
            if state == 0:
                # la respuesta es correcta si es igual que la respuesta correcta (y)
                if respuesta_user != respuesta_correcta:
                    turn_a = not turn_a  # el jugador ha perdido el turno, le toca al otro
            elif state == 1:
                dado = lanzar_dados()  # pasamos por parámetro cuántos dados lanzamos, por defecto, 1
            elif state == 2:
                if respuesta_user == None:
                    respuesta_user = random.choice([-1, 1])
                else:
                    respuesta_user = 1 if respuesta_user == "<-" else -1

                if turn_a:  # si le toca al jugador a, mueve su ficha hacia un lado u otro
                    player_a = (player_a + dado * respuesta_user) % len(tauler)
                else:  # si no, mueve al jugador b
                    player_b = (player_b + dado * respuesta_user) % len(tauler)

                # sólamente buscamos una pregunta al mover la ficha (una vez) en lugar de hacerlo por cada frame!
                message, respuesta_correcta, otras_respuestas = generar_pregunta(tauler, player_a if turn_a else player_b, data)

                # si el jugador ha caído en una casilla de volver a tirar (con valor -1)
                if respuesta_correcta == -1:
                    change_state = True
                    respuesta_user = respuesta_correcta
                else:  # si toca responder pregunta, mezcla las respuestas
                    todas_respuestas = [respuesta_correcta] + otras_respuestas
                    random.shuffle(todas_respuestas)
                    print("JUGADOR", ("A" if turn_a else "B") + ":", message)

        # DRAW NEW FRAME -----------------------------------------------------------------------------------------------
        gameDisplay.fill(colours.white)
        dibuja_tablero(tauler)

        if state == 0:  # DIBUJAR ESTADO DE LANZAR DADO
            # TODO: darle instrucciones al usuario
            dibuja_dado()
        elif state == 1:  # DIBUJAR ESTADO DE MOVER CASILLA (BOTONES)
            # TODO: darle instrucciones al usuario
            respuesta_user = dibuja_2o4_botones(["<<", ">>"], click)
            if respuesta_user != None:
                change_state = True
                click = False
        elif state == 2:  # DIBUJAR ESTADO DE ESPERAR RESPUESTA (BOTONES)
            escribe_texto(message, config.center_message)
            if respuesta_correcta != -1:
                respuesta_user = dibuja_2o4_botones(todas_respuestas, click)
                if respuesta_user != None:  # si hay una respuesta
                    click = False
                    change_state = True

        # el texto, el contador y los jugadores se dibujan lo último para que queden "encima" del tablero
        dibuja_barra_tiempo(timer, pygame.time.get_ticks() - timer_start)
        dibuja_jugador(tauler[player_a], "A")
        dibuja_jugador(tauler[player_b], "B")

        # UPDATE DISPLAY AND INCREASE TIME -----------------------------------------------------------------------------
        pygame.display.update()
        clock.tick()


""" ARRIBA, MAIN LOOP Y FUNCIONES; DEBAJO, EL PROGRAMA (MAIN)"""

if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

    # GAME LOOP
    game_loop()

    # CLOSE THE GAME
    pygame.quit()
    quit()
