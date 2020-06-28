from random import random

state = "OK"

counter = 20
while counter > 0:
    counter -= 1
    if state == "OK":
        if random() < 0.2:  # 20% of the time you are OK, you get hungry
            state = "Hungry"
            print("You were OK but now you are hungry!")
        else:
            print("You are OK!")
    elif state == "Hungry":
        if random() < 0.5: # you find food with probability 50%
            state = "Eating"
            print("You finally found food, you are now eating")
        else:
            print("You are hungry and looking for food")
    elif state == "Eating":
        if random() < 0.3:  # food is poisoned 1/3 of the times
            state = "Dead"
            print("You ate poisoned food and now you are dead")
            counter = -1
        else:
            state = "OK"
            print("You ate the food and now you are OK!")