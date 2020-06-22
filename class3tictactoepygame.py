import pygame
from random import randint
import colours
import config
import time

""" ARRIBA IMPORTS; DEBAJO FUNCIONES """


# dibuja el tablero con líneas (bonito)
def pinta_tablero_pygame(tablero):
    gameDisplay.fill(colours.white)
    pygame.draw.line(gameDisplay, colours.black, (config.display_width / 3, 0),
                     ((config.display_width / 3, config.display_height)), 10)
    pygame.draw.line(gameDisplay, colours.black, (2 * config.display_width / 3, 0),
                     ((2 * config.display_width / 3, config.display_height)), 10)
    pygame.draw.line(gameDisplay, colours.black, (0, config.display_height / 3),
                     ((config.display_width, config.display_height / 3)), 10)
    pygame.draw.line(gameDisplay, colours.black, (0, 2 * config.display_height / 3),
                     ((config.display_width, 2 * config.display_height / 3)), 10)

    for i in range(len(tablero)):
        row = tablero[i]
        for j in range(len(row)):
            column = row[j]
            if column == 1:
                pygame.draw.line(gameDisplay, colours.black,
                                 (int(config.display_width / 6 + j * config.display_width / 3 - config.display_width/7),
                                  int(config.display_height / 6 + i * config.display_height / 3 - config.display_height/7)),
                                 (int(config.display_width / 6 + j * config.display_width / 3 + config.display_width/7),
                                  int(config.display_height / 6 + i * config.display_height / 3 + config.display_height/7)), 15)
                pygame.draw.line(gameDisplay, colours.black,
                                 (int(config.display_width / 6 + j * config.display_width / 3 + config.display_width / 7),
                                  int(config.display_height / 6 + i * config.display_height / 3 - config.display_height / 7)),
                                 (int(config.display_width / 6 + j * config.display_width / 3 - config.display_width / 7),
                                  int(config.display_height / 6 + i * config.display_height / 3 + config.display_height / 7)), 15)
            elif column == 2:
                pygame.draw.circle(gameDisplay, colours.black, (
                    int(config.display_width / 6 + j * config.display_width / 3),
                    int(config.display_height / 6 + i * config.display_height / 3)), int(config.display_height/7), 10)


# pide al usuario dónde quiere poner su ficha y comprueba si es válido
def pregunta_posición(tablero):
    x = -1
    y = -1
    posición_ocupada = True
    # mientras no haya escogido una posición válida, sigue preguntando
    while posición_ocupada:
        try:
            # pide x e y, puede fallar por el cast
            x = int(input("¿En qué fila quieres poner tu ficha?"))
            y = int(input("¿En qué columna quieres poner tu ficha?"))

            # mira si la posición está vacía, puede fallar por el índice
            if tablero[x][y] == 0:
                posición_ocupada = False
            else:
                print("Esa posición ya está ocupada")
        except:
            # si fallan casts o índices, no es una posición válida (no es un número o está fuera de rango)
            print("No es una posición válida.")
    # cuando haya una posición válida, return
    return x, y


# pide al usuario dónde quiere poner su ficha y comprueba si es válido
def celda_segun_click(tablero):
    mouse_pos = pygame.mouse.get_pos()
    y = int(mouse_pos[0] / config.display_width * 3)
    x = int(mouse_pos[1] / config.display_height * 3)
    if tablero[x][y] != 0:
        return None, None
    return x, y


# escoge una posición usando una estrategia (mala), ¿cómo la mejoraríamos?
def escoge_posición_ai_simple(tablero):
    x = -1
    y = -1
    posición_ocupada = True
    # mientras no haya escogido una posición válida, sigue preguntando
    while posición_ocupada:
        x = randint(0, 2)
        y = randint(0, 2)

        # mira si la posición está vacía: no puede fallar por el índice -> no hace falta el try except
        if tablero[x][y] == 0:
            posición_ocupada = False
    # cuando haya una posición válida, return
    return x, y


# comprueba las filas, las columnas y las diagonales
def comprueba_ganador(tablero):
    for row in tablero:
        # si en una fila, las tres fichas son iguales y diferentes de 0, hay ganador
        if row[0] == row[1] == row[2] != 0:
            return True

    for y in range(3):
        # por cada columna, si las tres filas son iguales y diferentes de 0, hay ganador
        if tablero[0][y] == tablero[1][y] == tablero[2][y] != 0:
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != 0:
        # si la diagonal izquierda contiene el mismo número y es distinto de 0, hay ganador
        return True
    if tablero[2][0] == tablero[1][1] == tablero[0][2] != 0:
        # si la diagonal derecha contiene el mismo número y es distinto de 0, hay ganador
        return True

    # si no se ha devuelto true (se han mirado todos los casos), no hay ganador
    return False


# retorna true si hay al menos un sitio libre en el tablero (se puede jugar)
def comprueba_sitios_libres(tablero):
    sitios_libres = False
    for fila in tablero:
        for posicion in fila:
            if posicion == 0:
                return True
    return False


# gestiona los cambios de turno
def cambio_turno(jugador):
    if jugador == 1:
        return 2
    return 1


""" ARRIBA FUNCIONES; DEBAJO MAIN LOOP"""


def game_loop():
    clock = pygame.time.Clock()

    tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # crea tablero vacío

    jugador = 1  # siempre empieza a jugar el humano
    hay_ganador = False  # al principio, aún no ha ganado nadie
    sitios_libres = True

    closed = False
    while not closed and not hay_ganador and sitios_libres:
        # GET USER INPUT
        hay_cambios = False  # por defecto asumimos que nada cambia (hasta que algo diga lo contrario)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
            if event.type == pygame.MOUSEBUTTONUP:
                if jugador == 1:
                    print("¡Jugamos! Te toca, jugador", jugador)
                    x, y = celda_segun_click(tablero)  # pide posición al usuario
                    if x != None:
                        hay_cambios = True  # el usuario ha escogido casilla, así que hay cambios

        if jugador == 2:
            x, y = escoge_posición_ai_simple(tablero)  # pide posición a la IA
            print("La IA ha escogido aleatoriamente la posición x:" + str(x), "y:" + str(y))
            hay_cambios = True
            time.sleep(1)

        if hay_cambios:
            tablero[x][y] = jugador  # pon la ficha donde el jugador haya escogido
            hay_ganador = comprueba_ganador(tablero)  # comprueba si ha ganado
            if not hay_ganador:
                jugador = cambio_turno(jugador)  # cambio de jugador/turno
                sitios_libres = comprueba_sitios_libres(tablero)

        # DRAW NEW FRAME
        pinta_tablero_pygame(tablero)

        # UPDATE DISPLAY AND INCREASE TIME
        pygame.display.update()
        clock.tick()

    # di algo al final
    if hay_ganador:
        print("El jugador", jugador, "ha ganado la partida.")
    elif not sitios_libres:
        print("Os habéis quedado sin casillas libres, no ha ganado nadie.")


""" ARRIBA, MAIN LOOP Y FUNCIONES; DEBAJO, EL PROGRAMA (MAIN)"""

if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

    # GAME LOOP
    game_loop()

    # CLOSE THE GAME
    pygame.quit()
    quit()
