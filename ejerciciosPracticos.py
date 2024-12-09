#Ejercicio 1 del curso de python de soy Dalto

#Parte 1: Diferencia de porcentaje entre el curso actual y: -el más rápido de otros cursos. -el más lento de otros cursos. - el promedio de los cursos.

#min_curso = 2.5 
#max_curso = 7
#promedio_curso = 4
#curso_actual = 1.5

#Haciendo la diferencia.

#if curso_actual < min_curso and curso_actual < min_curso and curso_actual < promedio_curso :
 #   print("El curso actual es el más rápido")
#elif min_curso <= curso_actual and min_curso < max_curso and min_curso <= promedio_curso :
#    print("El curso de promedio minimo se encuentra entre el promedio y el curso de dalto")
#else : print("Este curso es el más lento de todos")

#Parte 2: Calculando el material basura de otros cursos.

#basura_cursos = promedio_curso - curso_actual

#print(f"La basura que hay en otros cursos es de: {basura_cursos} horas.")

#print("Opino que ver un curso con este profe nos hace la nasa xdxdxdxdxddd.")

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

import getpass

password = getpass.getpass("Ingrese su contraseña: ")
lonPassword = len(password)

print(f"La contraseña ingresada es: {password} y tiene {lonPassword} de caracteres.")

#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

print("Programa para que veas la division entre 2 numeros.")

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

try:
    division = num1 / num2
    print("El resultado de la división es:", division)
except ZeroDivisionError:
    print("Error: División entre cero.")
    
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

print("Este es un programa para saber si el numero es par o impar.")

num = float(input("Ingrese el numero: "))

if num % 2 == 0 : print("El numero es par")
else : print("El numero es impar.")

#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

print("Programa para saber si puedes tributar o no.")

edad = int(input("Ingresa tu edad: "))
ingresos = float(input("Digita tus ingresos mensuales en Euros: "))

if edad >= 16 and ingresos > 1000 : print("No puedes tributar.")
elif edad <16 and ingresos >= 1000 : print("Puedes tributar")
else : print("No puedes tributar.")
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

# Pedir al usuario su nombre y sexo
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ").upper()

# Validar el sexo ingresado
while sexo not in ['M', 'F']:
  print("Sexo inválido. Por favor, ingrese 'M' para masculino o 'F' para femenino.")
  sexo = input("Ingrese su sexo (M/F): ").upper()

# Asignar el grupo
if sexo == 'F' and nombre[0] < 'M':
  grupo = 'A'
elif sexo == 'M' and nombre[0] > 'N':
  grupo = 'A'
else:
  grupo = 'B'

# Mostrar el resultado
print("El alumno", nombre, "pertenece al grupo", grupo)

#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

print("Este es un programa para saber si debes pagar o no la entrada a la sala de juegos para todas las edades.")

edad = int(input("Ingresa tu edad: "))

if edad < 4 : print("Tu entrada es gratuita.")
elif edad >= 4 and edad <= 18: print("Debes pagar un total de 5 euros para ingresar a la sala.")
elif edad > 18 : print("Debes pagar 10 euros para entrar a la sala.")


#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

print("Programa para imprimir la palabra que ingreses 10 veces.")

palabra = input("Ingresa la palabra: ")

for i in range(1, 11):
    i += i
    print(palabra)
    
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("¿Cuántos años tienes? "))

print("Has cumplido los siguientes años:")
for i in range(1, edad + 1):
    print(i)
    
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Ingrese un número entero positivo: "))

print("Los números impares desde 1 hasta", numero, "son:")

for i in range(1, numero+1, 2):
    print(i, end=", ")