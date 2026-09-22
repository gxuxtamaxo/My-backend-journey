"""

Ejercicios de práctica de sintaxis en Python:

1. Variables y tipos de datos
Crea variables para guardar tu nombre, tu edad y si eres estudiante (True/False).
Imprime cada una junto con su tipo usando type().


2. Operadores aritméticos
Pide dos números al usuario con input() y muestra el resultado de sumarlos, 
restarlos, multiplicarlos, dividirlos, la división entera y el módulo.

3. Concatenación e interpolación de strings
Crea dos variables nombre y apellido. Imprime un saludo combinándolas 
usando f-strings (ej: f"Hola {nombre} {apellido}").

4. Condicionales (if / elif / else)
Pide un número entero y determina si es positivo, negativo o cero, 
y además si es par o impar.

5. Bucle for con range()
Usa un for con range() para imprimir los números del 1 al 20, 
pero solo los múltiplos de 3.

6. Bucle while con contador
Crea un contador que empiece en 0 y use while para imprimir números hasta 
llegar a 10, incrementando con +=.

7. Listas y su indexación
Crea una lista con 5 nombres de frutas. Imprime la primera, la última, 
y todas menos la primera (usando slicing [1:]).

8. Funciones simples
Define una función es_par(numero) que reciba un número y retorne True si es par 
y False si es impar. Pruébala con varios valores.

9. Operadores lógicos
Pide la edad de una persona y si tiene licencia (True/False). 
Usa and/or para determinar si puede conducir (mayor de 18 y con licencia).

10. Combinando todo: FizzBuzz
Recorre los números del 1 al 30 con un for. Si el número es múltiplo de 3, 
imprime "Fizz"; si es múltiplo de 5, imprime "Buzz"; si es múltiplo de ambos, 
imprime "FizzBuzz"; si no, imprime el número.

"""

# Ejercicio 1: Variables y tipos de datos
nombre = "Jesus"
edad = 26
es_estudiante = True

print(nombre, type(nombre))
print(edad, type(edad))
print(es_estudiante, type(es_estudiante))

# Ejercicio 2: Operadores aritméticos
Primer_numero = int(input("Ingresa un numero: "))
Segundo_numero = int(input("Ingresa otro numero: "))

print("Suma:", Primer_numero + Segundo_numero)
print("Resta:", Primer_numero - Segundo_numero)
print("Multiplicación:", Primer_numero * Segundo_numero)
print("División:", Primer_numero / Segundo_numero)
print("División entera:", Primer_numero // Segundo_numero)
print("Módulo:", Primer_numero % Segundo_numero)

# Ejercicio 3: Concatenación e interpolación de strings
nombre = "Jesus"
apellido = "Tamayo"
#Ahora debo usar f-strings para imprimir un saludo combinando nombre y apellido
print (f"Hola {nombre}  {apellido}") # cuando se usa la f para concatenar strings, las variables se ponen entre llaves.

# Ejercicio 4: Condicionales (if / elif / else)
numero = int(input("ingrese un numero: "))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

# Ejercicio 5: Bucle for con range()
for i in range(1, 20):
    if i % 3 == 0:
        print (i)

# Ejecicio 6: Bucle while con contador
contador = 0

while contador <= 10:
    print(contador)
    contador += 1


# Ejercicio 7: Listas y su indexación
frutas= ["manzana", "pera", "sandia", "uva", "mora"]

print(frutas[0])
print (frutas[4])
print (frutas[1:])

# Ejercicio 8: Funciones simples
# se na (def) para definir una funcion
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Ejercicio 9: Operadores lógicos
edad = int(input("Ingrese su edad: "))
tiene_licencia = bool(input("Tiene usted una licencia activa (True/False): "))

if edad >= 18 and tiene_licencia == True:
    print("Puede conducir tranquilamente")
elif edad >= 18 and tiene_licencia == False:
    print("Usted no puede conducir, adquiera una licencia")
else:
    print("Usted es menor de edad, no puede conducir")


# Ejercicio 10: Combinando todo: FizzBuzz
for numero in range(1, 30):
    if numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    elif numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    else:
        print(numero)