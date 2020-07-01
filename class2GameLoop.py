import pygame

# para probar estos programas (separados por un comentario) comenta y descomenta los distintos
# bloques para ver las diferencias de comportamiento, ¿sabes qué hace cada línea de código?

""" SIN LOOP, SÓLO UN FRAME """
# pygame.init()
# gameDisplay = pygame.display.set_mode((200, 200))
#
# gameDisplay.fill((0, 255, 0))
# pygame.display.update()
#
# pygame.quit()
# quit()

""" USER INPUT """
# pygame.init()
# gameDisplay = pygame.display.set_mode((200, 200))
#
# for event in pygame.event.get():
#     print(event)
# gameDisplay.fill((0, 255, 0))
# pygame.display.update()
#
# pygame.quit()
# quit()

""" CON LOOP INFINITO """
# pygame.init()
# gameDisplay = pygame.display.set_mode((200, 200))
#
# while True:
#     gameDisplay.fill((0, 255, 0))
#     pygame.display.update()
#
# pygame.quit()
# quit()

""" CON LOOP LEYENDO INPUT """
# pygame.init()
# gameDisplay = pygame.display.set_mode((200, 200))
#
# while True:
#     for event in pygame.event.get():
#         print(event)
#     gameDisplay.fill((0, 255, 0))
#     pygame.display.update()
#
# pygame.quit()
# quit()

""" CON LOOP PERO SÓLO UNA ITERACIÓN """
# pygame.init()
# gameDisplay = pygame.display.set_mode((200, 200))
#
# sigue_jugando = True
# while sigue_jugando:
#     gameDisplay.fill((0, 255, 0))
#     pygame.display.update()
#     sigue_jugando = False
#
# pygame.quit()
# quit()

""" CON LOOP ACABADO POR INPUT """
# pygame.init()
# gameDisplay = pygame.display.set_mode((200, 200))
#
# sigue_jugando = True
# while sigue_jugando:
#     for event in pygame.event.get():
#         print(event)
#         if event.type == pygame.QUIT:
#             sigue_jugando = False
#     gameDisplay.fill((0, 255, 0))
#     pygame.display.update()
#
# pygame.quit()
# quit()

""" CAMBIO DE COLOR CON INPUTS """
# pygame.init()
# gameDisplay = pygame.display.set_mode( (200, 200) )
#
# sigue_jugando = True
# while sigue_jugando:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             sigue_jugando = False
#         elif evento.type == pygame.MOUSEBUTTONUP:
#             gameDisplay.fill( (0, 255, 0) )
#         else:
#             gameDisplay.fill( (255, 0, 0 ) )
#
#     pygame.display.update()
#
# pygame.quit()
# quit()

""" CON LOOP ACABADO POR INPUT E IMPRIMIENDO CLICKS """

pygame.init()
gameDisplay = pygame.display.set_mode((200, 200))

sigue_jugando = True
while sigue_jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sigue_jugando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
    gameDisplay.fill((255, 0, 0))
    pygame.display.update()

pygame.quit()
quit()