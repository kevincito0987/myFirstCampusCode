#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

#import getpass

#password = getpass.getpass("Ingrese su contraseña: ")
#lonPassword = len(password)

#print(f"La contraseña ingresada es: {password} y tiene {lonPassword} de caracteres.")

#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

#print("Programa para que veas la division entre 2 numeros.")

#num1 = float(input("Ingrese el primer numero: "))
#num2 = float(input("Ingrese el segundo numero: "))

#try:
 #   division = num1 / num2
#  print("El resultado de la división es:", division)
#except ZeroDivisionError:
 #   print("Error: División entre cero.")
    
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

#print("Este es un programa para saber si el numero es par o impar.")

#num = float(input("Ingrese el numero: "))

#if num % 2 == 0 : print("El numero es par")
#else : print("El numero es impar.")

#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

#print("Programa para saber si puedes tributar o no.")

#edad = int(input("Ingresa tu edad: "))
#ingresos = float(input("Digita tus ingresos mensuales en Euros: "))

#if edad >= 16 and ingresos > 1000 : print("No puedes tributar.")
#elif edad <16 and ingresos >= 1000 : print("Puedes tributar")
#else : print("No puedes tributar.")
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

# Pedir al usuario su nombre y sexo
#nombre = input("Ingrese su nombre: ")
#sexo = input("Ingrese su sexo (M/F): ").upper()

# Validar el sexo ingresado
#while sexo not in ['M', 'F']:
 # print("Sexo inválido. Por favor, ingrese 'M' para masculino o 'F' para femenino.")
 # sexo = input("Ingrese su sexo (M/F): ").upper()

# Asignar el grupo
#if sexo == 'F' and nombre[0] < 'M':
 # grupo = 'A'
#elif sexo == 'M' and nombre[0] > 'N':
#  grupo = 'A'
#else:
  #grupo = 'B'

# Mostrar el resultado
#print("El alumno", nombre, "pertenece al grupo", grupo)

#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

#print("Este es un programa para saber si debes pagar o no la entrada a la sala de juegos para todas las edades.")

#edad = int(input("Ingresa tu edad: "))

#if edad < 4 : print("Tu entrada es gratuita.")
#elif edad >= 4 and edad <= 18: print("Debes pagar un total de 5 euros para ingresar a la sala.")
#elif edad > 18 : print("Debes pagar 10 euros para entrar a la sala.")


#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

#print("Programa para imprimir la palabra que ingreses 10 veces.")

#palabra = input("Ingresa la palabra: ")

#for i in range(1, 11):
 #   i += i
  #  print(palabra)
    
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

#edad = int(input("¿Cuántos años tienes? "))

#print("Has cumplido los siguientes años:")
#for i in range(1, edad + 1):
#    print(i)
    
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

#numero = int(input("Ingrese un número entero positivo: "))

#print("Los números impares desde 1 hasta", numero, "son:")

#for i in range(1, numero+1, 2):
 #   print(i, end=", ")
 
 #Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
#print("Programa para que veas en pantalla la cuenta atras del número que ingresaste.") 
#num = int(input("Ingrese un número entero positivo: "))

#for i in range(num, 0, -1):
 #    print(i ,end=",")
 
 #Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

#print("En este programa podras calcular capital obtenido en $ en la inversión cada año que dura la inversión")
#cpi = int(input("Ingrese el capital con el que vas a empezar en pesos colombianos: "))
#ti = int(input("Ingrese el porcentaje de interes con el que vas a empezar: "))
#tic = ti / 100
#tiempo = int(input("Ingrese numero de años con los que vas a empezar: "))
#toi = input("Ingrese tipo de interes de tu inversion C para compuesto y S para simple: ")

#def calcular_capital_inversion(capital_inicial, tasa_interes, num_anos, tipo_interes):

 # capital_final = []
  #for ano in range(1, num_anos + 1):
   # if tipo_interes == "S":
    #  intereses = capital_inicial * tasa_interes * ano
     # capital_final.append(capital_inicial + intereses)
    #elif tipo_interes == "C":
     # capital_final.append(capital_inicial * (1 + tasa_interes) ** ano)
    #else: print("La opción que ingresaste no esta dentro del programa")
  #return capital_final

#dinero_obtenido = calcular_capital_inversion(cpi, tic, tiempo, toi)
#print(f"El dinero que vas a obtener después de {tiempo} es de: {dinero_obtenido}")

#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

#numero = int(input("Ingrese un número: "))
# Ciclo for para iterar del 1 al 10
#for i in range(1, 11):
 #   resultado = numero * i
  #  print(f"{numero} x {i} = {resultado}")
    
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
#import getpass
#contraseña_campus = "campus2023"
#def contraseña ():
 # while True:
  #      try:
   #        con_u = getpass.getpass("Ingrese la contraseña de campus: ")
    #       if con_u == contraseña_campus:
     #          lonPassword = len(con_u)
              # print(f"La contraseña ingresada es: {con_u} y tiene {lonPassword} de caracteres, esa es la contraseña correcta camper:).")
               #return con_u
           #else:
            #    print("Esa no es la contraseña, vuelve a ingresarla.")
       # except ValueError: print("Entrada inválida. Por favor, ingrese la contraseña correcta.")

#con_i = contraseña()

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
#def solicitar_numero():
 #   while True:
  #      try:
   #         numero = int(input("Ingrese un número entero positivo: "))
    #        if numero >= 0:
     #           return numero
      #      else:
       #         print("Por favor, ingrese un número entero no negativo.")
        #except ValueError:
         #   print("Entrada inválida. Por favor, ingrese un número entero.")
#numero = solicitar_numero()
#def es_primo(numero):
 # if numero <= 1:
  #  return False
  #if numero <= 3:
   # return True
  #if numero % 2 == 0 or numero % 3 == 0:
   # return False
  #i = 5
  #while i * i <= numero:
   # if numero % i == 0 or numero % (i + 2) == 0:
    #  return False
    #i += 6
  #return True

#if es_primo(numero):
 # print(numero, "es un número primo.")
#else:
 # print(numero, "no es un número primo.")
  
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
  
#palabra = input("Ingrese una palabra: ")

# Invertimos la palabra para mostrar las letras desde la última
#palabra_invertida = palabra[::-1]

# Recorremos la palabra invertida y mostramos cada letra
#print("".join(palabra_invertida))

#frase = input("Ingrese una frase: ")
#letra = input("Ingrese una letra: ")

# Convertimos tanto la frase como la letra a minúsculas para evitar problemas de mayúsculas y minúsculas
#frase = frase.lower()
#letra = letra.lower()

# Contamos las ocurrencias de la letra en la frase
#contador = frase.count(letra)

#print("La letra", letra, "aparece", contador, "veces en la frase.")

#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
#while True:
 #   texto = input("Escribe algo (o 'salir' para terminar): ")
  #  if texto.lower() == "salir":
   #     break
    #print(texto)
#print("Con este programa vas a hacer +-*/ sea cual sea tu caso.")

#def calculadora (operacion, num1, num2):
    
 # if operacion == "+":
  #    suma = num1+num2
   #   print(f"El resultado de la suma es de: {suma}")
  #elif operacion == "-":
   #   resta = num1 - num2
    #  print(f"El resultado de la resta es de: {resta}")
  #elif operacion == "*":
   #   multiplicacion = num1 * num2
    #  print(f"El resultado de la multiplicación es de: {multiplicacion}")
 # elif operacion == "/":
  #    division = num1 / num2
   #   print(f"El resultado de la division es de: {division}")
  #else : print("La operación que se seleccionó no esta dentro de las opciones programadas.")
  #return calculadora

#resultado1 = calculadora("/", 23, 12)
#resultado2 = calculadora(num2=23,operacion= "*" ,num1=12)   
    
    
#Ejercicio clase y review (Funciones):
#Escribir una función que reciba un número entero positivo y devuelva su factorial.
#print("Programa para hallar el factorial de un número.")

#def solicitar_numero():
 #   while True:
  #      try:
   #         numero = int(input("Ingrese un número entero positivo: "))
    #        if numero >= 0:
     #           return numero
      #      else:
       #         print("Por favor, ingrese un número entero no negativo.")
       # except ValueError:
        #    print("Entrada inválida. Por favor, ingrese un número entero.")

#numero = solicitar_numero()

#def factorial_iterativo(n):
 # if n == 0:
  #  factorial = 1
  #  return 1
  #for i in range(1, n + 1):
   # factorial *= i
  #return factorial

#resultado = factorial_iterativo(numero)
#print(f"El resultado de factorial de: {numero} es de {resultado}")
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
#def solicitar_precio():
 #   while True:
  #      try:
   #         numero = float(input("Ingrese el precio del producto: "))
    #        if numero >= 0:
     #           break
      #      else:
       #         print("Por favor, ingrese un número entero no negativo.")
        #except ValueError:
         #   print("Entrada inválida. Por favor, ingrese un número entero.")
   # return numero

#def solicitar_iva():
 #   while True:
  #      try:
   #         tasa_iva = float(input("Ingrese la tasa de IVA (en formato decimal): "))
    #        if tasa_iva >= 0:
     #           break
      #    else:
       #         print("Por favor, ingrese un número entero no negativo.")
        #except ValueError:
         #   print("Entrada inválida. Por favor, ingrese un número entero.")
    #return tasa_iva

#def calcular_precio_con_iva(precio_producto, tasa_iva):
 #   iva = tasa_iva * precio_producto / 100
  #  precio_final = precio_producto + iva
   # return precio_final

# Ejemplo de uso:
#precio_producto = solicitar_precio()
#tasa_iva = solicitar_iva()

#precio_total = calcular_precio_con_iva(precio_producto, tasa_iva)
#print(f"El precio total con IVA es: {precio_total}")
#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
#import math

#def area_circulo(radio):
  
 # area = math.pi * radio**2
  #return area

#def volumen_cilindro(radio, altura): 
  
  # Calculamos el área de la base del cilindro
 # area_base = area_circulo(radio)
  # Calculamos el volumen del cilindro
  #volumen = area_base * altura
  #return volumen

#def solicitar_radio_cilindro():
 #   while True:
  #      try:
   #         numero = float(input("Ingrese el radio del cilindro: "))
    #        if numero >= 0:
     #           break
      #      else:
       #         print("Por favor, ingrese un número entero no negativo.")
        #except ValueError:
        #    print("Entrada inválida. Por favor, ingrese un número entero.")
    #return numero
#def solicitar_altura_cilindro():
 #   while True:
  #      try:
   #         numero = float(input("Ingrese la altura del cilindro: "))
    #        if numero >= 0:
     #           break
      #      else:
       #         print("Por favor, ingrese un número entero no negativo.")
        #except ValueError:
         #   print("Entrada inválida. Por favor, ingrese un número entero.")
   # return numero

# Ejemplo de uso:
#radio_cilindro = solicitar_radio_cilindro()
#altura_cilindro = solicitar_altura_cilindro()

#area_base = area_circulo(radio_cilindro)
#volumen = volumen_cilindro(radio_cilindro, altura_cilindro)

#print("El área de la base del cilindro es:", area_base)
#print("El volumen del cilindro es:", volumen)
#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
#def mcd(a, b):
  
 # while b != 0:
  #  a, b = b, a % b
 # return a

#def mcm(a, b):

 # return a * b // mcd(a, b)

#def solicitar_num1():
 #   while True:
  #      try:
   #         numero = float(input("Ingrese el primer numero: "))
    #        if numero >= 0:
     #           break
      #      else:
       #         print("Por favor, ingrese un número entero no negativo.")
       # except ValueError:
        #    print("Entrada inválida. Por favor, ingrese un número entero.")
   # return numero
#def solicitar_num2():
 #   while True:
  #      try:
   #         numero = float(input("Ingrese el segundo numero: "))
    #        if numero >= 0:
     #           break
      #      else:
       #         print("Por favor, ingrese un número entero no negativo.")
        #except ValueError:
         #   print("Entrada inválida. Por favor, ingrese un número entero.")
    #return numero
# Ejemplo de uso:
#num1 = solicitar_num1()
#num2 = solicitar_num2()

#resultado_mcd = mcd(num1, num2)
#resultado_mcm = mcm(num1, num2)

#print("El máximo común divisor de", num1, "y", num2, "es:", resultado_mcd)
#print("El mínimo común múltiplo de", num1, "y", num2, "es:", resultado_mcm)
#Escribir un programa que reciba una cadena de caracteres e imprima el tamaño de la cadena, la cadena en mayusculas, la cadena en minusculas, la cadena invertida y la segunda mitad de la cadena.
#def manipular_cadena(cadena):

  # Tamaño de la cadena
 # tamaño = len(cadena)
  #print("El tamaño de la cadena es:", tamaño)

  # Cadena en mayúsculas
  #mayusculas = cadena.upper()
  #print("La cadena en mayúsculas es:", mayusculas)

  # Cadena en minúsculas
  #minusculas = cadena.lower()
  #print("La cadena en minúsculas es:", minusculas)

  # Cadena invertida
  #invertida = cadena[::-1]
  #print("La cadena invertida es:", invertida)

  # Segunda mitad de la cadena
  #mitad = len(cadena) // 2
  #segunda_mitad = cadena[mitad:]
  #print("La segunda mitad de la cadena es:", segunda_mitad)
#def solicitar_cadena_solo_letras():
  #  while True:
   #     cadena = input("Ingrese una cadena que contenga solo letras: ")
    #    if cadena.isalpha():
     #       return cadena
     #   else:
      #      print("Entrada inválida. Por favor, ingrese solo letras.")

# Ejemplo de uso:
#cadena_valida = solicitar_cadena_solo_letras()
#print("La cadena ingresada es:", cadena_valida)
# Llamamos a la función para manipular la cadena
#manipular_cadena(cadena_valida)
#Crea una función que ordene y retorne una lista o vector de números. La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.  No se pueden utilizar funciones incorporadas que lo resuelvan automáticamente.
def ordenar_burbuja(lista, orden):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if (orden == "Asc" and lista[j] > lista[j+1]) or (orden == "Desc" and lista[j] < lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]

def obtener_entrada_valida():
    while True:
        try:
            lista_str = input("Ingrese los números separados por comas: ")
            lista = [int(num) for num in lista_str.split(',')]
            # Validación adicional: si la conversión a int falla, se levantará una excepción
            return lista
        except ValueError:
            print("Entrada inválida. Por favor, ingrese solo números separados por comas.")

# Obtener la lista del usuario
lista = obtener_entrada_valida()

# Resto del código... (ordenamiento, etc.)

# Obtener el orden de ordenamiento
orden = input("Ingrese 'Asc' para ordenar ascendente o 'Desc' para descendente: ")

# Validar el orden
while orden not in ["Asc", "Desc"]:
    print("Orden inválido. Por favor, ingrese 'Asc' o 'Desc'.")
    orden = input("Ingrese 'Asc' para ordenar ascendente o 'Desc' para descendente: ")

# Ordenar la lista
ordenar_burbuja(lista, orden)

# Imprimir la lista ordenada con un mensaje descriptivo
if orden == "Asc":
    print("La lista ordenada de menor a mayor es:", lista)
else:
    print("La lista ordenada de mayor a menor es:", lista)
#Dado un listado de números, encuentra el SEGUNDO más grande 