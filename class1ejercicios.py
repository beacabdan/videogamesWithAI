# Realiza la suma de 2 números enteros y multiplica un número entero por un float (número con decimales)

4+5
2*3.5

# Almacena los resultados de las operaciones anteriores en una variable y visualiza los resultados usando print()

var1 = 4+5
var2 = 2*3.5
print(var1, var2)

# Calcula la media de tres números y visualiza el resultado usando print()

var1 = 4
var2 = 5
var3 = 10
media = (var1 + var2 + var3) / 3
print(media)

year = input('year')
year = int(year)

operador400 = year % 400
operador100 = year % 100
operador4 = year % 4

if operador400 == 0:
    print('bisiesto')
elif operador100 == 0:
    print('no bisiesto')
elif operador4 == 0:
    print('bisiesto')
else:
    print ('no bisiesto')