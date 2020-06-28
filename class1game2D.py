from random import randint

# width and height of the 2D board

# create a board using the width and height variables

# generate a random position for the player and the objetivo and place both in the 2d board
player_pos = [0, 0]  # TODO: random xy player position (first value is fila, second is column)
objetivo_pos = [0, 0]  # TODO: random xy food position (first value is fila, second is column)
# TODO: pon un 1 en xy del jugador usando tablero[fila jugador][columna jugador] (un 1 representa al jugador)
# TODO: pon un 2 en xy del objetivo usando tablero[fila objetivo][columna objetivo] (un 2 representa al objetivo)

# START OF GAME LOOP
while puntuacion < 100:
    # UPDATE SCENE
    # random walk, movimiento 50% del tiempo vertical, 50% horizontal
    # TODO: pon un 0 en la posición actual del jugador (el player desaparece de donde estaba)
    # TODO: pon un 1 en la nueva posición del jugador (el player aparece en la posición nueva)

    # si player llega al objetivo, genera un nuevo objetivo
        # TODO: random xy objetivo position (first value is the row, second is column)
        # TODO: pon un 2 en xy del objetivo con tablero[fila objetivo][columna objetivo] (un 2 representa al objetivo)
        # TODO: suma uno a la puntuación

    # DRAW SCENE
    # TODO: muestra la puntuación por pantalla
    # dibuja el tablero
# END OF GAME LOOP