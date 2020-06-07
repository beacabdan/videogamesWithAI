# PRINTS
print("Hello Bea!")
print("Hello Mundo!")

mis_manzanas = 7
tipo_manzanas = "Royal Gala"
num_entero = 2
num_decimales = 2.5

print(mis_manzanas)
print(tipo_manzanas)
print(num_decimales, num_entero, tipo_manzanas)

print("-------------------")

# OPERACIONES CON VARIABLES
mis_manzanas = 20
manzanas_amigo = 5
mis_manzanas = mis_manzanas + manzanas_amigo
print(mis_manzanas)

mis_manzanas = mis_manzanas - manzanas_amigo
print(mis_manzanas)

numero_cajas = 3
manzanas_por_caja = 20
mis_manzanas = manzanas_por_caja*numero_cajas
print(mis_manzanas)

numero_amigos = 6
manzanas_por_cabeza = mis_manzanas / numero_amigos
print(manzanas_por_cabeza)
manzanas_por_cabeza = mis_manzanas // numero_amigos
print(manzanas_por_cabeza)
manzanas_restantes = mis_manzanas % numero_amigos
print(manzanas_restantes)

# OPERACIONES CON STRINGS
nombre = "María"
apellido = "García"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

print("-------------------")

# COMPARACIONES ENTRE VARIABLES
comparacion_manzanas = mis_manzanas < manzanas_amigo
print(comparacion_manzanas)

nombre_amigo = nombre
comparacion_nombres = (nombre == nombre_amigo)
print(comparacion_nombres)

# CONDICIONALES
if nombre == "María":
    print("Me gusta tu nombre, María!")
else:
    print("Ah, vale, no te llamas María!")

precipitaciones_medias = 25
precipitaciones_2020 = 10

if precipitaciones_2020 > precipitaciones_medias:
    print("Ha llovido por encima de la media!")
else:
    print("Ha llovido por debajo de la media!")

if precipitaciones_2020 < precipitaciones_medias:
    print("No ha llovido tanto como otros años!")

if not precipitaciones_2020 > precipitaciones_medias:
    print("No ha llovido tanto como otros años!")
print("-------------------")

edad = 28
if edad >= 18:
    print("Puedes entrar en...")
else:
    print("No puedes entrar en...")
print("-------------------")

# WHILE LOOP
edad = 8
while edad < 18:
    print("No puedes entrar aquí!")
    edad = edad + 1
print("Bienvenido!")
print("-------------------")

# FOR LOOPS
for x in range(0, 11):
    print("Hola mundo!", x)