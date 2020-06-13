""" INPUTS INESPERADOS """
edad = input("Dime tu edad:")
try:
    edad = int(edad)  # si esto no falla, continua
    print("El doble de tu edad es", edad * 2)
except ValueError:  # si el cast a int falla, se salta a aquí
    print("¡Eso no es un número! No puedo calcular el doble.")
print("--------------------------------")

""" VALORES POR DEFECTO EN EL EXCEPT """
try:
    numero = int(input("Dime número:"))  # si esto falla, salta al except
except:  # no hace falta decir qué tipo de excepción capturamos
    numero = -1  # valor por defecto si falla
print("El número escogido es:", numero)
print("--------------------------------")

""" SALIRSE DEL ARRAY """
lista = ["1r elem.", "2o elem.", "3r elem."]  # lista tiene 3 posiciones (0,1, y 2)
try:
    for i in range(5):  # no tiene sentido mirar la 4a y 5a posición!
        print(lista[i])  # el 4o fallará, saldrá del for y saltará al except
except IndexError:
    print("El índice está fuera del rango (lista[i] no existe)")  # sólo se imprime una vez, ¿por qué?
print("--------------------------------")

i = 0
while i < 5:  # lo mismo que el anterior pero con un while (que no acaba con la primera excepción!)
    try:
        print(lista[i]) # si esto falla, se va al except y luego se sigue con el while
    except IndexError:
        print("El índice está fuera del rango (lista[i] no existe)")  # ahora sí se repite!!, ¿por qué?
    i += 1  # lo probamos con el siguiente elemento
print("--------------------------------")