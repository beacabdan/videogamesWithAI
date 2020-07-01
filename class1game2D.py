from random import randint

# width and height of the 2D board
width = 6
height = 5

# create a board using the width and height variables
tablero = []
for i in range(height):
    row = [0]*width  # un 0 representa una celda vacía
    tablero.append(row)

# generate a random position for the player and the food and place both in the 2d board
player_pos = [randint(0, height-1), randint(0, width-1)]
objetivo_pos = [randint(0, height-1), randint(0, width-1)]
tablero[player_pos[0]][player_pos[1]] = 1  # un 1 representa al jugador
tablero[objetivo_pos[0]][objetivo_pos[1]] = 2  # un 2 representa al objetivo
puntuacion = 0

# START OF GAME LOOP
while puntuacion < 100:
    # UPDATE SCENE
    # random walk, movimiento 50% del tiempo vertical, 50% horizontal
    tablero[player_pos[0]][player_pos[1]] = 0  # el player desaparece de donde estaba
    if randint(0, 1):
        player_pos[0] = max(0, min(player_pos[0] + randint(-1, 1), height - 1))  # cambia la posición x (sin salirse)
    else:
        player_pos[1] = max(0, min(player_pos[1] + randint(-1, 1), width - 1))  # cambia la posición y (sin salirse)
    tablero[player_pos[0]][player_pos[1]] = 1  # pon al player en la posición nueva

    # si player llega al objetivo, genera un nuevo objetivo
    if player_pos == objetivo_pos:
        objetivo_pos = [randint(0, height - 1), randint(0, width - 1)]  #posición xy aleatoria
        tablero[objetivo_pos[0]][objetivo_pos[1]] = 2  # un 2 en el tablero simboliza el objetivo
        puntuacion += 1  # sumarle 1 a la puntuación

    # DRAW SCENE
    print("Score board:", puntuacion)
    columns = len(tablero[0])
    print("+---" * columns + "+")
    for row in tablero:
        print("| ", end="")
        for column in row:
            if column == 0:
                print(" ", end=" | ")
            else:
                print(str(column)[0], end=" | ")
        print("\n" + "+---" * columns + "+")
# END OF GAME LOOP