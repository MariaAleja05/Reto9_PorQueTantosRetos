##**Punto 3**
"""

def potencia(x, n):
  if n == 0:
    return 1
  else:
    return x * potencia(x, n - 1)

if __name__ == "__main__":
  n = int(input("Ingrese la potencia: "))
  x = float(input("Ingrese la base: "))
  rta = potencia(x, n)
  print("La potencia de " + str(x) + " elevado a " + str(n) + " es: " + str(rta))