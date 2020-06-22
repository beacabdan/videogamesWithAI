from random import randint


""" FUNCIONES """


# dibuja el tablero con líneas (bonito)
def dibuja_tablero(tablero):
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
        else:
            print("Esa posición ya está ocupada")
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


""" PROGRAMA """

tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # crea tablero vacío
dibuja_tablero(tablero)

jugador = 1  # siempre empieza a jugar el humano
hay_ganador = False  # al principio, aún no ha ganado nadie
sitios_libres = True

# mientras no haya ganador = mientras siga el juego
while not hay_ganador and sitios_libres:
    if jugador == 1:
        print("¡Jugamos! Te toca, jugador", jugador)
        x, y = pregunta_posición(tablero)  # pide posición al usuario
    else:
        x, y = escoge_posición_ai_simple(tablero)  # pide posición a la IA
        print("La IA ha escogido aleatoriamente la posición x:" + str(x), "y:" + str(y))

    tablero[x][y] = jugador  # pon la ficha donde el jugador haya escogido
    hay_ganador = comprueba_ganador(tablero)  # comprueba si ha ganador

    # cambio de jugador/turno
    if not hay_ganador:
        # comprueba si hay sitios libres
        sitios_libres = False
        for fila in tablero:
            for posicion in fila:
                if posicion == 0:
                    sitios_libres = True

        if jugador == 1:
            jugador = 2
        else:
            jugador = 1

    # dibuja el tablero con la nueva ficha
    dibuja_tablero(tablero)

# di algo al final
if hay_ganador:
    print("El jugador", jugador, "ha ganado la partida.")
elif not sitios_libres:
    print("Os habéis quedado sin casillas libres, no ha ganado nadie.")
