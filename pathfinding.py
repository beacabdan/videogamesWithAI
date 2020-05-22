import numpy as np
import heapq
DEBUG = False


def draw_board(board, pos):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if x == pos[0] and y == pos[1]:
                print("--", end=" ")
            else:
                print(board[y][x], end=" ")
        print()


def debug(s):
    if DEBUG:
        for word in s:
            print(word, end=" ")
        print()


def heuristic(x, y, x2, y2):
    return abs(x-x2)+abs(y-y2)


def reconstruct_path(cameFrom, start, current):
    total_path = [current]
    while True:
        for y in range(len(cameFrom)):
            for x in range(len(cameFrom[0])):
                if [y, x] == current:
                    debug((current, "came from", cameFrom[y][x]))
                    current = cameFrom[y][x]
                    total_path.append(current)
                    if current == start:
                        return total_path[::-1]


# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def a_star(start_x, start_y, goal_x, goal_y, walkable, map):
    if start_x < 0 or start_x >= len(map[0]) or start_y < 0 or start_y >= len(map):
        return None
    if goal_x < 0 or goal_x >= len(map[0]) or goal_y < 0 or goal_y >= len(map):
        return None

    # map[goal_y][goal_x] = 0

    openSet = []  # Initially, only the start node is known
    heapq.heappush(openSet, (heuristic(start_x, start_y, goal_x, goal_y), [start_y, start_x]))

    cameFrom = []  # For node n, cameFrom[n] = node preceding it on cheapest path from start to n currently known
    [cameFrom.append([[start_y, start_x]] * len(map[0])) for _ in range(len(map))]

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known
    gScore = np.ones((len(map), len(map[0]))) * np.inf
    gScore[start_y][start_x] = 0

    # fScore[n] = best guess on how short a path from start to finish is if it goes through n
    fScore = np.ones((len(map), len(map[0]))) * np.inf
    fScore[start_y][start_x] = map[start_y][start_x]

    while len(openSet) > 0:
        current = heapq.heappop(openSet)[1]
        debug(("CURRENTLY EXPLORING", current, "GOAL IS", [goal_x, goal_y]))

        if current == [goal_x, goal_y]:
            debug("GOAL FOUND!")
            return reconstruct_path(cameFrom, [start_y, start_x], current)

        for deltax, deltay in [(0, +1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            # CHECK IF NEIGHBOUR IS WALKABLE
            if current[0]+deltay < 0 or current[0]+deltay >= len(map) or current[1]+deltax < 0 or current[1]+deltax >= len(map[0]):
                continue
            if map[current[1] + deltax][current[0] + deltay] not in walkable and map[current[1] + deltax][current[0] + deltay] != 0:
                continue

            debug(("CHECKING NEIGHBOUR", [current[0] + deltay, current[1] + deltax]))

            tentative_gScore = gScore[current[0]][current[1]] + 1
            if tentative_gScore < gScore[current[0]+deltay][current[1]+deltax]:
                debug(("A BETTER PATH TO", [current[0]+deltay, current[1]+deltax], "WAS FOUND!"))
                cameFrom[current[0]+deltay][current[1]+deltax] = current
                gScore[current[0]+deltay][current[1]+deltax] = tentative_gScore
                fScore[current[0]+deltay][current[1]+deltax] = gScore[current[0]][current[1]] + heuristic(current[1] + deltax, current[0] + deltay, goal_x, goal_y)

                appendTo = True
                for pos in openSet:
                    if [current[0]+deltay, current[1]+deltax] == pos[1]:
                        debug((pos, "already in", openSet))
                        appendTo = False
                if appendTo:
                    heapq.heappush(openSet, (fScore[current[0]+deltay][current[1]+deltax], [current[0] + deltay, current[1] + deltax]))
                    debug(([current[0] + deltay, current[1] + deltax], "now in", openSet))

    return None
