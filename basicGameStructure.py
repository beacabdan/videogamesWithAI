import pygame
import config
import math

""" ARRIBA IMPORTS; DEBAJO FUNCIONES """


# TODO: Implementar les funcions que calguin per fer el joc


""" ARRIBA FUNCIONES; DEBAJO MAIN LOOP"""


def game_loop():
    clock = pygame.time.Clock()

    closed = False
    while not closed:
        # GET USER INPUT, TODO: Llegir quins botons ha fet servir l'usuari

        # DRAW NEW FRAME, TODO: Dibuixar el frame

        # UPDATE DISPLAY AND INCREASE TIME
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
