def solicitar_rango():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo para solicitar hasta donde vamos a encontrar los números primos gemelos: "))
            if numero >= 0:
                return numero
            else:
                print("Por favor, ingrese un número entero no negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
rango = solicitar_rango()
def es_primo(num):
  """Verifica si un número es primo."""
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def encontrar_primos_gemelos(limite):
  """Encuentra todos los pares de primos gemelos hasta un límite dado."""
  primos_gemelos = []
  for num in range(2, limite):
    if es_primo(num) and es_primo(num + 2):
      primos_gemelos.append((num, num + 2))
  return primos_gemelos

# Encontrar y mostrar los primos gemelos
resultado = encontrar_primos_gemelos(rango)
print("Los pares de primos gemelos encontrados son:", resultado)
