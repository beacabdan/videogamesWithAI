import pygame
import math
import random


""" LAS FUNCIONES, TODAS JUNTAS AL PRINCIPIO DEL PROGRAMA, JUSTO DEBAJO DE LOS IMPORTS """


def text_objects(text, font, colour = (0, 0, 0)):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def messageDisplay(text, pos, size = 20):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = pos
    gameDisplay.blit(TextSurf, TextRect)


""" TUS FUNCIONES AQUI DEBAJO (DE MOMENTO) """


def rotate(shape, angle = math.pi):
    shapeTemp = []
    for i in range(len(shape)):
        shapeTemp.append(shape[i].copy())

    for i in range(len(shapeTemp)):
        shapeTemp[i][0] = shape[i][0] * math.cos(angle) - shape[i][1] * math.sin(angle)
        shapeTemp[i][1] = shape[i][0] * math.sin(angle) + shape[i][1] * math.cos(angle)
    return shapeTemp


def translateToCenterAndDraw(shape, fill, colour):
    shapeTemp = []
    for i in range(len(shape)):
        shapeTemp.append(shape[i].copy())
    if fill:
        shapeTemp.append([0,0])

    for i in range(len(shapeTemp)):
        shapeTemp[i][0] += display_width / 2
        shapeTemp[i][1] += display_height / 2
    if fill:
        pygame.draw.polygon(gameDisplay, colour, shapeTemp)
    else:
        pygame.draw.lines(gameDisplay, (0, 0, 0), False, shapeTemp)


def flip(shape, horizontal = True):
    angle = math.pi
    shapeTemp = []
    for i in range(len(shape)):
        shapeTemp.append(shape[i].copy())

    for i in range(len(shapeTemp)):
        if horizontal:
            shapeTemp[i][0] = shape[i][0] * math.cos(angle) - shape[i][1] * math.sin(angle)
        else:
            shapeTemp[i][1] = shape[i][0] * math.sin(angle) + shape[i][1] * math.cos(angle)
    return shapeTemp


def shapeToMandala(shape8, divisions, angle = 0, fill = False, colour = (255,255,255)):
    translateToCenterAndDraw(rotate(shape8, angle), fill, colour)
    shape1 = flip(shape8, False)
    translateToCenterAndDraw(rotate(shape1, angle), fill, colour)

    for i in range(0, divisions-1, 2):
        shape2 = rotate(shape8, i * math.pi / divisions * 2)
        translateToCenterAndDraw(rotate(shape2, angle), fill, colour)
        shape2 = rotate(shape1, i * math.pi / divisions * 2)
        translateToCenterAndDraw(rotate(shape2, angle), fill, colour)


def mandala(shapes):
    time = pygame.time.get_ticks() * 0.00001

    for shape, div, fill, colour in shapes:
        shapeToMandala(shape, div, time, fill, colour)


def createShapes():
    shapes = []

    for j in range(2,10,2):
        division = random.randint(4,7)*2
        radius = 300-j * 30
        steps = 10-j
        shape = []
        for i in range(0,steps+1):
            randRad = random.randint(43, 45)/j
            x = math.cos(math.pi*2/steps/division*i)*(radius+math.sin(i)*randRad)
            y = math.sin(math.pi*2/steps/division*i)*(radius+math.sin(i)*randRad)
            shape.append([x, y])
        shapes.append([shape, division, True, ((1-steps/9)*100+100, division/30*100+125, (1-division/30)*steps/9*100+100)])
        shapes.append([shape, division, False, None])

        shapeCopy = []
        for i in range(len(shape)):
            shapeCopy.append([shape[i][0] * 0.95, shape[i][1] * 0.95])
        shapes.append([shapeCopy, division, True, ((1-steps/9)*100+155, division/30*100+155, (1-division/30)*steps/9*100+155)])
        shapes.append([shapeCopy, division, False, None])

        for i in range(len(shape)):
            shape2 = []
            shape2.append([shape[i][0], shape[i][1]])
            shape2.append([shapeCopy[i][0], shapeCopy[i][1]])
            shapes.append([shape2, division, False, None])

    return shapes


""" TUS FUNCIONES POR ENCIMA DE ESTA LINEA """

def game_loop():
    # INICIALIZAMOS LA APP
    pygame.display.set_caption('Mandala')
    clock = pygame.time.Clock()

    # VARIABLES DE LA APP
    white = (255, 255, 255)

    shapes = createShapes()

    # LOOP DEL JUEGO
    finalizado = False
    while not finalizado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finalizado = True

        gameDisplay.fill(white)
        mandala(shapes)

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