"""
Operadores Leccion 2 
"""
# Operadores Aritmeticos
print(f"Suma: 20 + 6 = {20 + 6}")
print(f"Resta: 15 - 6 = {15 - 6}")
print(f"Multiplicacion: 10 * 5 = {10 * 5}")
print(f"Division: 75 / 4 = {75 / 4}")
print(f"Modulo: 15 % 4 = {15 % 4}") # El modulo es el remainder que queda de una division.
print(f"Exponente: 5 ** 3 = {5 ** 3}")
print(f"Division Entera: 74 // 4 = {74 // 4}") #La division entera toma el numero entero que se da a partide una division.

"""
Operadores de Comparacion 
"""
# Hacen y manejan comparaciones

# Igualdad
print(f"Tgualdad: 15 == 15 es {15 == 15}")
# Desigualdad
print(f"Desigualdad: 15 != 14 es {15 != 14}")
# Mayor Que 
print(f"Mayor Que: 15 > 10 es {15 > 10}")
# Menor Que 
print(f"Menor Que: 10 < 15 es {10 < 15}")
# Mayor o igual que
print(f"Mayor o igual que : 15 >= 15 es {15 >= 15}")
# Menor o igual que 
print(f"Menor o igual que: 15 <= 15 es {15 <= 15}")

"""
Operadores Logicos
"""
# And: Dos condiciones que son iguales
print(f"AND &&: 2 + 2 = 4 and 2 + 1 = 3 es {2 + 2 = 4 and 2 + 1 = 3}")
# Or: Veracidad de minimo una de las condiciones
print(f"OR ||: 2 + 2 = 78 and 2 + 1 = 3 es {2 + 2 = 78 and 2 + 1 = 3}")
# Not: No es no da
print(f"NOT !: 2 + 2 = 78 and 2 + 1 = 35 es {2 + 2 = 78 and 2 + 1 = 35}") 
# Not especial de Doble Negacion
print(f"NOT !: not 2 + 2 = 4  es {not 2 + 2 = 4}")

"""
Operadores de Asignacion
"""
# Se asignan valores a variables.
my_number = 11

my_personal_number += 1 # Se suma y se asigna
my_personal_number -= 1 # Se resta y se asigna
my_personal_number *= 1 # Se multiplica y se asigna
my_personal_number /= 1 # Se divide y se asigna
my_personal_number %= 1 # Se modula y se asigna
my_personal_number **= 1 # Se exponencia y se asigna
my_personal_number //= 1 # Se divide en el entero y se asigna

"""
Operadores de Identidad
"""
# Para comparar el valor de la posicion de memoria, cada variable es su memoria.
my_nummer = 5.5
my_numero = 5.5

print(f"my_nummer is my_numero es {my_nummer is my_numero}")

my_nummer = 5.5
my_numero = 5.2
print(f"my_nummer is not my_numero es {my_nummer is not my_numero}")

"""
Operadores de Pertenencia
"""
# Mirar a ver si algo pertence a un conjunto o algo asi.
# IN
print(f" 'o' in 'salado' = {'o' in 'salado'}")

# NOT IN
print(f" 'z' not in 'salado' = {'z' in 'salado'}")

"""
Operadores de Bit
"""
# Operadores con codigo binario, poco importantes pero parte del aprendizaje
a = 10
b = 3
# 10 3n binario es 1010 y 3 en binario es 0011

# Operador AND Si son iguales los dos entonces es el digito y lo demas es cero
print(f"AND: 10 & 3 = {10 & 3}") # 1010 0011       0010 o sea 2

# Operador Or, si al menos hay un uno pos es uno.
print(f"OR: 10 | 3 = {10 | 3}") # 1011

# Operador XOR si los bits son difetentes es 1 si son iguales 0
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001

# Operador NOT Intercambia el valor de los bits
print(f"NOT: ~ 10 = {~ 10}") #0101

# Operador Desplazamiento Derecha, el segundo numero es el digito que marca la pauta pal desplazamiento
print(f"Desplazamiento a la derecha: 10 >> 1 = {10 >> 1}") # 0101

# Operador Desplazamiento Izquierda
print(f"Desplazamiento a la izquierda: 10 >> 1 = {10 >> 1}") # 10100



"""
ESTRUCTURAS DE CONTROL 
"""

# Condicionales
my_string = "pangutangu"

if my_string == "pangutangu":
print("my_string es "pangutangu")

else:
print("my_string no es "pangutangu")

# Elif, comprobacion intermedia
elif: 
my_string == "pangolo":
print(my_string es "pangolo")

# Estructuras Iterativas
# FOR, recorrer estructuras de mas de un elemento o ejecutar una accion varias veces

for i in range (11):
print (i)

# WHILE, Condicion para que un bucle se de mientras la condicion sea verdadera
i = 0
while i <= 10:
print (i)

# Estructuras de Control para Manejo de excepciones 
try:
print{1 / 0}
except:
print ("Se ha producido un error")
finally:
print ("ha finalizado el manejo de excepciones)

"""
VUAMOOOS
"""


