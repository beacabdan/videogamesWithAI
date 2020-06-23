import pygame

""" LAS FUNCIONES, TODAS JUNTAS AL PRINCIPIO DEL PROGRAMA, JUSTO DEBAJO DE LOS IMPORTS """

def text_objects(text, font, colour = (0, 0, 0)):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def messageDisplay(text, pos, size = 20):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = pos
    gameDisplay.blit(TextSurf, TextRect)


def hand(img, x, y):
    halfSize = 25
    gameDisplay.blit(img, (x-halfSize, y-halfSize))

""" TUS FUNCIONES AQUI DEBAJO (DE MOMENTO) """

def drawHands(img):
    y = display_height * 0.65
    reps = 6
    oneOut = pygame.time.get_ticks() // 1000 % (reps-1)+1

    messageDisplay("por cada valor de x en el rango(1,"+str(reps)+")", (display_width/2, 200))
    messageDisplay("si x es diferente de " + str(oneOut), (display_width / 2, 230))
    messageDisplay("dibuja una mano", (display_width/2, 260))

    for i in range(1,reps):
        x = i * display_width / reps
        if i != oneOut:
            hand(img, x, y)
        messageDisplay(str(i), (x, y - 40))

""" TUS FUNCIONES POR ENCIMA DE ESTA LINEA """

def game_loop():
    # INICIALIZAMOS LA APP
    pygame.display.set_caption('Juego')
    clock = pygame.time.Clock()

    # VARIABLES DE LA APP
    white = (255, 255, 255)
    black = (0, 0, 0)

    handImg = pygame.image.load('assets/hand.png')

    # LOOP DEL JUEGO
    finalizado = False
    while not finalizado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finalizado = True

        gameDisplay.fill(white)
        drawHands(handImg)

        # UPDATEAMOS EL DISPLAY Y AVANZAMOS EN EL TIEMPO
        pygame.display.update()
        clock.tick(60)


""" LAS FUNCIONES POR ENCIMA DE ESTA LINEA, EL PROGRAMA POR DEBAJO """

# ALTO Y ANCHO DE LA PANTALLA
display_width = 600
display_height = 600

# LO DEJAREMOS COMO GLOBALES
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))

game_loop()
pygame.quit()
quit()