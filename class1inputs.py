# EJEMPLO SIN CAPTURAR EXCEPCIONES
while True:
    num1 = int(input("Dime el primer número:"))
    num2 = int(input("Dime el segundo número:"))

    if num1 > num2:
        print("El primero es mayor!")
    elif num1 < num2:
        print("El segundo es mayor!")
    else:
        print("Son iguales!")

# CAPTURANDO EXCEPCIONES, PREGUNTANDO CONSTANTEMENTE
while True:
    try:
        num1 = int(input("Dime el primer número:"))
        num2 = int(input("Dime el segundo número:"))

        if num1 > num2:
            print("El primero es mayor!")
        elif num1 < num2:
            print("El segundo es mayor!")
        else:
            print("Son iguales!")
    except:
        print("Uno de los números no es válido.")

# CAPTURANDO EXCEPCIONES, PREGUNTANDO HASTA QUE SE DEN VALORES VÁLIDOS
num1 = None
num2 = None

while num1 == None:  # mientras num1 tenga un valor inváli do / hasta que num1 no tenga un valor válido
    try:
        num1 = int(input("Dime el primer número:"))
    except:
        print("No has introducido un número válido.")

while num2 == None:  # mientras num2 tenga un valor inválido / hasta que num2 no tenga un valor válido
    try:
        num2 = int(input("Dime el segundo número:"))
    except:
        print("No has introducido un número válido.")

# cuando haya valores para num1 y num2, comparamos
if num1 > num2:
    print("El primero es mayor!")
elif num1 < num2:
    print("El segundo es mayor!")
else:
    print("Son iguales!")