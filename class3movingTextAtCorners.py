import pygame
import math


""" ARRIBA IMPORTS, ABAJO FUNCIONES """


def text_objects(text, font, colour = (0, 0, 0)):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def messageDisplay(text, pos, size = 20):
    largeText = pygame.font.Font('assets/Roboto-Regular.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = pos
    gameDisplay.blit(TextSurf, TextRect)


""" FUNCIONES ARRIBA, MAIN LOOP DEBAJO """


def game_loop():
    # INICIALIZAMOS LA APP
    pygame.display.set_caption('My game')
    clock = pygame.time.Clock()

    # VARIABLES DE LA APP
    white = (255, 255, 255)
    black = (0, 0, 0)

    # LOOP DEL JUEGO
    finalizado = False
    while not finalizado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finalizado = True
                print("Quit game.")

        gameDisplay.fill(white)

        """ EJERCICIO SOBRE HACER LAS POSICIONES RELATIVAS AL TAMAÑO """
        size = 30
        margin_x = 100 + 50*math.cos(pygame.time.get_ticks()/1000)
        margin_y = 50 + 50*math.sin(pygame.time.get_ticks()/1000)
        messageDisplay("Top left", (0+margin_x, 0+margin_y), size)
        messageDisplay("Top", (display_width/2, 0+margin_y), size)
        messageDisplay("Top right", (display_width-margin_x, 0+margin_y), size)
        messageDisplay("Left", (0+margin_x, display_height/2), size)
        messageDisplay("Center", (display_width/2, display_height/2), size)
        messageDisplay("Right", (display_width-margin_x, display_height/2), size)
        messageDisplay("Bottom left", (0+margin_x, display_height-margin_y), size)
        messageDisplay("Bottom", (display_width/2, display_height-margin_y), size)
        messageDisplay("Bottom right", (display_width-margin_x, display_height-margin_y), size)

        """ EJERCICIO SOBRE HACER LAS POSICIONES RELATIVAS AL TAMAÑO """

        # UPDATEAMOS EL DISPLAY Y AVANZAMOS EN EL TIEMPO
        pygame.display.update()
        clock.tick()


""" MAIN LOOP Y FUNCIONES ARRIBA, EL PROGRAMA DEBAJO """


# ALTO Y ANCHO DE LA PANTALLA
display_width = 600
display_height = 600

# LO DEJAREMOS COMO GLOBALES
pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))

game_loop()
pygame.quit()
quit()