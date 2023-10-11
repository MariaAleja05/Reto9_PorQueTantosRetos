# Reto número 9 repo
### Fecha:  09-10-2023
**1.** De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

* Mirar archivo Punto_1.ipynb

### Primera función:
**Enunciado: (reto 6, punto 3)**

* Sin usar lambda:
      
```pseudocode
def CalcularCantidadCarne(N:float, M:float, K:float) -> float:
  cantidad_carne = (6*N) + (7*M) + (1*K)
  return cantidad_carne

if __name__ == "__main__":
  N = float(input("Ingrese el número de gallinas:"))
  M = float(input("Ingrese el número de gallos:"))
  K = float(input("Ingrese el número de pollitos:"))
  carne_total = CalcularCantidadCarne(N, M, K)
  print("----------------------------------------------------------------")
  print("La cantidad de carne de aves en kilos es " + str(carne_total))
```

* Usando lambda:
  
```pseudocode
if __name__ == "__main__":
  N = float(input("Ingrese el número de gallinas:"))
  M = float(input("Ingrese el número de gallos:"))
  K = float(input("Ingrese el número de pollitos:"))
  carne_total = (lambda N, M, K: ((6*N) + (7*M) + (1*K)))(N,M,K)
  print("----------------------------------------------------------------")
  print("La cantidad de carne de aves en kilos es " +       str(carne_total))
```

### Segunda función:
**Enunciado: (reto 6, punto 4)**

* Sin usar lambda:
      
```pseudocode
def CalcularVueltas(P:int, M:int, H:int, B:int) -> int:
  precio = (300*P) + (3300*M) + (350*H)
  vueltas = B-precio
  return vueltas

if __name__ == "__main__":
  P = int(input("Ingrese el número de panes:"))
  M = int(input("Ingrese el número de bolsas de leche:"))
  H = int(input("Ingrese el número de huevos:"))
  B = int(input("Ingrese el billete con el que va a pagar:"))
  vueltas_t = CalcularVueltas(P, M, H, B)
  print("----------------------------------------------------------------")
  if vueltas_t>0:
    print("Las vueltas son " + str(vueltas_t))
  elif vueltas_t<0:
    print("Se deben al vendedor " + str(vueltas_t))
  else:
    print("No hay vueltas " + str(vueltas_t))
```

* Usando lambda:

```pseudocode
if __name__ == "__main__":
  P = int(input("Ingrese el número de panes:"))
  M = int(input("Ingrese el número de bolsas de leche:"))
  H = int(input("Ingrese el número de huevos:"))
  B = int(input("Ingrese el billete con el que va a pagar:"))
  vueltas_t = (lambda P, M, H, B: (B-((300*P) + (3300*M) + (350*H))))(P,M,H,B)
  print("----------------------------------------------------------------")
  if vueltas_t>0:
    print("Las vueltas son " + str(vueltas_t))
  elif vueltas_t<0:
    print("Se deben al vendedor " + str(vueltas_t))
  else:
    print("No hay vueltas " + str(vueltas_t))
```

### Tercera función:
**Enunciado: (reto 6, punto 5)**

* Sin usar lambda:
      
```pseudocode
def CalcularPrestamo(c:float, i:float, n:float) -> float:
  interes_mes = i/12
  total = c*((1+interes_mes)**n)
  return total

if __name__ == "__main__":
  c = float(input("Ingrese el valor del prestamo inicial:"))
  i = float(input("Ingrese el interés anual:"))
  n = float(input("Ingrese la cantidad de meses:"))
  total_f = CalcularPrestamo(c, i, n)
  print("----------------------------------------------------------------")
  print("El interes compuesto es " + str(total_f))
```

* Usando lambda:

```pseudocode
if __name__ == "__main__":
  c = float(input("Ingrese el valor del prestamo inicial:"))
  i = float(input("Ingrese el interés anual:"))
  n = float(input("Ingrese la cantidad de meses:"))
  total_f = (lambda c, i, n: c*((1+(i/12))**n))(c,i,n)
  print("----------------------------------------------------------------")
  print("El interes compuesto es " + str(total_f))
```

**2.** De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

* Mirar archivo Punto_2.ipynb

### Primera función:
**Enunciado: (reto 6, punto 3)**

* Sin usar *args:
      
```pseudocode
def CalcularCantidadCarne(N:float, M:float, K:float) -> float:
  cantidad_carne = (6*N) + (7*M) + (1*K)
  return cantidad_carne

if __name__ == "__main__":
  N = float(input("Ingrese el número de gallinas:"))
  M = float(input("Ingrese el número de gallos:"))
  K = float(input("Ingrese el número de pollitos:"))
  carne_total = CalcularCantidadCarne(N, M, K)
  print("----------------------------------------------------------------")
  print("La cantidad de carne de aves en kilos es " + str(carne_total))
```

* Usando *args:
  
```pseudocode
def CalcularCantidadCarne(*args) -> float:
  cantidad_carne = (6*N) + (7*M) + (1*K)
  return cantidad_carne

if __name__ == "__main__":
  N = float(input("Ingrese el número de gallinas:"))
  M = float(input("Ingrese el número de gallos:"))
  K = float(input("Ingrese el número de pollitos:"))
  carne_total = CalcularCantidadCarne(N, M, K)
  print("----------------------------------------------------------------")
  print("La cantidad de carne de aves en kilos es " + str(carne_total))
```

### Segunda función:
**Enunciado: (reto 6, punto 4)**

* Sin usar *args:
      
```pseudocode
def CalcularVueltas(P:int, M:int, H:int, B:int) -> int:
  precio = (300*P) + (3300*M) + (350*H)
  vueltas = B-precio
  return vueltas

if __name__ == "__main__":
  P = int(input("Ingrese el número de panes:"))
  M = int(input("Ingrese el número de bolsas de leche:"))
  H = int(input("Ingrese el número de huevos:"))
  B = int(input("Ingrese el billete con el que va a pagar:"))
  vueltas_t = CalcularVueltas(P, M, H, B)
  print("----------------------------------------------------------------")
  if vueltas_t>0:
    print("Las vueltas son " + str(vueltas_t))
  elif vueltas_t<0:
    print("Se deben al vendedor " + str(vueltas_t))
  else:
    print("No hay vueltas " + str(vueltas_t))
```

* Usando *args:

```pseudocode
def CalcularVueltas(*args) -> int:
  precio = (300*P) + (3300*M) + (350*H)
  vueltas = B-precio
  return vueltas

if __name__ == "__main__":
  P = int(input("Ingrese el número de panes:"))
  M = int(input("Ingrese el número de bolsas de leche:"))
  H = int(input("Ingrese el número de huevos:"))
  B = int(input("Ingrese el billete con el que va a pagar:"))
  vueltas_t = CalcularVueltas(P, M, H, B)
  print("----------------------------------------------------------------")
  if vueltas_t>0:
    print("Las vueltas son " + str(vueltas_t))
  elif vueltas_t<0:
    print("Se deben al vendedor " + str(vueltas_t))
  else:
    print("No hay vueltas " + str(vueltas_t))
```

### Tercera función:
**Enunciado: (reto 6, punto 5)**

* Sin usar *args:
      
```pseudocode
def CalcularPrestamo(c:float, i:float, n:float) -> float:
  interes_mes = i/12
  total = c*((1+interes_mes)**n)
  return total

if __name__ == "__main__":
  c = float(input("Ingrese el valor del prestamo inicial:"))
  i = float(input("Ingrese el interés anual:"))
  n = float(input("Ingrese la cantidad de meses:"))
  total_f = CalcularPrestamo(c, i, n)
  print("----------------------------------------------------------------")
  print("El interes compuesto es " + str(total_f))
```

* Usando *args:

```pseudocode
def CalcularPrestamo(*args) -> float:
  interes_mes = i/12
  total = c*((1+interes_mes)**n)
  return total

if __name__ == "__main__":
  c = float(input("Ingrese el valor del prestamo inicial:"))
  i = float(input("Ingrese el interés anual:"))
  n = float(input("Ingrese la cantidad de meses:"))
  total_f = CalcularPrestamo(c, i, n)
  print("----------------------------------------------------------------")
  print("El interes compuesto es " + str(total_f))
```

**3.** Escriba una función recursiva para calcular la operación de la potencia.
* EXPLICACION
* Mirar archivo Punto_3.py
```pseudocode
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
```
**4.** Utilice la siguiente plantilla de code para contar el tiempo:
```pseudocode
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.

* EXPLICACION
* Mirar archivo Punto_4.py
```pseudocode

```

**5.** Crear cuenta en stackoverflow y adjuntar imagen en el repo

<img width="960" alt="Screenshot 2023-10-10 202249" src="https://github.com/MariaAleja05/Reto9/assets/141857519/7a948f5b-129f-498d-8cf2-27de0fc71d2d">

**6.** Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.
  * EXPLICACION
www.linkedin.com/in/maría-alejandra-niño-peña-7075b0295
