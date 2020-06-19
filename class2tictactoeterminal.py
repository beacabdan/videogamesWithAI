from random import randint

tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # crea tablero vacío
# dibuja el tablero con líneas (bonito)
print("+---+---+---+")
for row in tablero:
    print("| ", end="")
    for column in row:
        if column == 1:
            print("X", end=" | ")
        elif column == 2:
            print("O", end=" | ")
        else:
            print(" ", end=" | ")
    print("\n+---+---+---+")

jugador = randint(1, 2)  # decidimos aleatoriamente quién empieza a jugar
hay_ganador = False
sitios_libres = True

# mientras no haya ganador = mientras siga el juego y se pueda seguir jugando
while not hay_ganador and sitios_libres:
    print("Sigue jugando, turno de", jugador)
    # pregunta al usuario dónde quiere una ficha <- comprobar que sea una posición válida

    posicion_valida = False
    # mientras no haya escogido una posición válida, sigue preguntando
    while not posicion_valida:
        try:
            # pide x e y, puede fallar por el cast
            fila = int(input("Dime qué fila quieres:"))
            columna = int(input("Dime qué columna quieres:"))

            # mira si la posición está vacía, puede fallar por el índice
            if tablero[fila][columna] == 0:
                posicion_valida = True
        except:
            print("La fila o la columna no eran válidas!")

    # pon la ficha donde el jugador haya escogido
    tablero[fila][columna] = jugador

    # comprueba si ha ganador
    # si en una fila, las tres fichas son iguales y diferentes de 0, hay ganador
    for row in tablero:
        if row[0] == row[1] == row[2] != 0:
            hay_ganador = True
    # por cada columna, si las tres filas son iguales y diferentes de 0, hay ganador
    for y in range(3):
        if tablero[0][y] == tablero[1][y] == tablero[2][y] != 0:
            hay_ganador = True
    # si la diagonal izquierda contiene el mismo número y es distinto de 0, hay ganador
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != 0:
        hay_ganador = True
    # si la diagonal derecha contiene el mismo número y es distinto de 0, hay ganador
    if tablero[2][0] == tablero[1][1] == tablero[0][2] != 0:
        hay_ganador = True

    # comprueba si hay sitios libres
    if not hay_ganador:
        sitios_libres = False
        for fila in tablero:
            for posicion in fila:
                if posicion == 0:
                    sitios_libres = True

        # cambio de jugador/turno
        if jugador == 1:
            jugador = 2
        elif jugador == 2:
            jugador = 1

    # dibuja el tablero con líneas (bonito)
    print("+---+---+---+")
    for row in tablero:
        print("| ", end="")
        for column in row:
            if column == 1:
                print("X", end=" | ")
            elif column == 2:
                print("O", end=" | ")
            else:
                print(" ", end=" | ")
        print("\n+---+---+---+")

# di quién ha ganado
print("Ha ganado el jugador", jugador)