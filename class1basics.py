""" PRINTS Y COMENTARIOS"""
print("Hello World!")
print("Hello Bea!")

""" VARIABLES """
mis_manzanas = 10
tus_manzanas = 685462
numero_amigos = 10
pizza_ingerida = 0.5
print("Yo tengo", mis_manzanas, "manzanas y tú tienes", tus_manzanas)

# OPERACIONES CON VARIABLES
print(mis_manzanas+tus_manzanas)
print(tus_manzanas-mis_manzanas)
print(mis_manzanas*2)
print(mis_manzanas/2)
print(mis_manzanas**3)

# GUARDAR EL RESULTADO EN OTRA VARIABLE
nuestras_manzanas = mis_manzanas + tus_manzanas
print("Yo tengo", mis_manzanas, "manzanas y tú tienes", tus_manzanas)
print("Entre los dos tenemos", nuestras_manzanas, "manzanas")
mis_manzanas = mis_manzanas + 50
print("Ahora tengo", mis_manzanas, "manzanas")

""" COMPARAR VARIABLES (OPERADORES REACIONALES) """
# <
# >
# ==
# !=

print(mis_manzanas > 20)
print(mis_manzanas > tus_manzanas)
print(mis_manzanas < tus_manzanas)
print(mis_manzanas >= 60)
print(mis_manzanas <= 60)
print(mis_manzanas == tus_manzanas)
var1 = mis_manzanas == tus_manzanas
print(var1)
var1 = mis_manzanas != tus_manzanas
print(var1)

""" STRINGS Y OPERADORES RELACIONALES"""

mis_manzanas = "Royal Gala"
tus_manzanas = "Golden"
print("Mis manzanas son", mis_manzanas, "y tus manzanas son", tus_manzanas)
print(mis_manzanas*2)
print(mis_manzanas+" "+tus_manzanas)
print(mis_manzanas < "Royal Gaaa")

var1 = 5
var2 = 30
print(var1 > var2)

""" CASTS """
var1 = "54"
var2 = int(var1)
print(var1, var2)
print(var1*2, var2*2)
var3 = str(var2*2)
print(var3*2)

""" IF ELSE """
mis_manzanas = 40856423143
if mis_manzanas < 50:
    print("Ve a comprar manzanas urgentemente!")
elif mis_manzanas == 50:
    print("Estás en el límite")
elif mis_manzanas == 51:
    print("Estás en el límite")
elif mis_manzanas > 100:
    print("Tienes un montón")
else:
    print("No hace falta que compres manzanas")

""" BUCLES """
# WHILE LOOP
contador = 20
while contador > 0:
    print("Estoy mirando al alumno", contador)
    contador = contador - 1

# FOR LOOP
for x in range(0, 11):
    print(x)



























