#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'\'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
#print("********")
#print("Programa para saber si la divisa que ingreses esta dentro de mi programacion.")
#def solicitar_divisa():
 #  while True:
  #      cadena = input("Ingrese el nombre de una divida, el nombre que contenga la primera letra mayuscula y las demas en minusculas: ")
   #     if cadena.isalpha():
    #        return cadena
     #   else:
      #      print("Entrada inválida. Por favor, ingrese solo letras.")

#def divisa_existe(nombre_divisa, lista_divisas):
 # """Verifica si un código de divisa existe y devuelve la información si es así."""

 # for divisa in lista_divisas:
  #  if divisa["nombre"] == nombre_divisa:
   #   return divisa
#  return None

#lista_divisas = [
 #   {"nombre": "Dólar estadounidense", "código": "USD", "símbolo": "$"},
  #  {"nombre": "Euro", "código": "EUR", "símbolo": "€"},
   # {"nombre": "Libra esterlina", "código": "JPY", "símbolo": "¥"},
 #   {"nombre": "Yen japonés", "código": "JPY", "símbolo": "¥"},
  #  {"nombre": "Dólar australiano", "código": "AUD", "símbolo": "A$"},
   # {"nombre": "Dólar canadiense", "código": "CAD", "símbolo": "C$"},
  #  {"nombre": "Franco suizo", "código": "CHF", "símbolo": "CHF"},
   # {"nombre": "Renminbi/yuan chino	", "código": "CNY", "símbolo": "元"},
 #   {"nombre": "Dólar de Hong Kong", "código": "HKD	", "símbolo": "HK$"},
  #  {"nombre": "Dólar de Nueva Zelanda", "código": "NZD	", "símbolo": "NZ$"},
#]

#while True:
 # nombre_divisa = solicitar_divisa()
  #if nombre_divisa.lower() == 'salir':
   # break

  #divisa_encontrada = divisa_existe(nombre_divisa, lista_divisas)

  #if divisa_encontrada:
   # print(f"Información de la divisa {nombre_divisa}:")
   # print(f"Nombre: {divisa_encontrada['nombre']}")
   # print(f"Símbolo: {divisa_encontrada['símbolo']}")
 # else:
  #  print(f"La divisa {nombre_divisa} no existe en nuestra base de datos.")
    
#2. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
print("********")
print("Programa para registrar tus datos")

nombre_usario = input("Ingresa tu nombre completo: ")
edad_usuario = input("Ingresa la edad que tienes: ")
direccion_usuario = input("Ingresa tu direccion: ")
telefono_usuario = input("Ingresa tu numero telefonico: ")

usuario = {
    "nombre" : nombre_usario,
    "edad" : edad_usuario,
    "direccion" : direccion_usuario,
    "telefono" : telefono_usuario
}

print(f"Usted {usuario['nombre']}, tiene {usuario['edad']} años, su direccion es: {usuario['direccion']} y su telefono de contacto es: {usuario['telefono']}")