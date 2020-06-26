from random import randint

# width and height of the 2D board
width = 6
height = 5

# create a board using the width and height variables
tablero = []
for i in range(height):
    fila = [0] * width  # un 0 representa una celda vacía
    tablero.append(fila)

# generate a random position for the player and the food and place both in the 2d board
player_pos = [0, 0]  # TODO: random xy player position (first value is fila, second is column)
objetivo_pos = [0, 0]  # TODO: random xy food position (first value is fila, second is column)
# TODO: pon un 1 en xy del jugador usando tablero[fila jugador][columna jugador] (un 1 representa al jugador)
# TODO: pon un 2 en xy del objetivo usando tablero[fila objetivo][columna objetivo] (un 2 representa al objetivo)
puntuacion = 0

# START OF GAME LOOP
while puntuacion < 100:
    # UPDATE SCENE
    # random walk, movimiento 50% del tiempo vertical, 50% horizontal
    # TODO: pon un 0 en la posición actual del jugador (el player desaparece de donde estaba)
    if randint(0, 1):  # número aleatorio entre 0 y 1 = tira una moneda (cara o cruz)
        player_pos[0] = max(0, min(player_pos[0] + randint(-1, 1), height - 1))  # cambia la posición x (sin salirse)
    else:
        player_pos[1] = max(0, min(player_pos[1] + randint(-1, 1), width - 1))  # cambia la posición y (sin salirse)
    # TODO: pon un 1 en la nueva posición del jugador (el player aparece en la posición nueva)

    # si player llega al objetivo, genera un nuevo objetivo
    if player_pos == objetivo_pos:
        objetivo_pos = [0, 0]  # TODO: random xy food position (first value is the row, second is column)
        # TODO: pon un 2 en xy del objetivo con tablero[fila objetivo][columna objetivo] (un 2 representa al objetivo)
        # TODO: suma uno a la puntuación

    # DRAW SCENE
    # TODO: muestra la puntuación por pantalla
    # dibuja el tablero
    print("+---" * len(tablero[0]) + "+")
    for fila in tablero:
        print("| ", end="")
        for column in fila:
            if column == 0:
                print(" ", end=" | ")  # si hay un 0, imprime un espacio = nada
            else:
                print(str(column)[0], end=" | ")  # si no, imprime el número
        print("\n" + "+---" * len(tablero[0]) + "+")
# END OF GAME LOOP