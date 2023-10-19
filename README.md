# Reto número 9 repo
### Fecha:  09-10-2023
**1.** De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

* Mirar archivo Punto_1.ipynb

### Primera función:
**Enunciado: (reto 6, punto 3)** Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

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
**Enunciado: (reto 6, punto 4)** Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

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
**Enunciado: (reto 6, punto 5)** Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

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
**Enunciado: (reto 6, punto 3)** Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

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
**Enunciado: (reto 6, punto 4)** Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

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
**Enunciado: (reto 6, punto 5)** Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

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
* Lo primero que hice fue crear una función de la potencia, donde se llama a ella misma para realizar la multiplicación y cada vez se le irá restando una unidad a la potencia hasta que se multiplique las n veces en total. En la función main le solicite al usuario ingresar la potencia, la base de la potencia, llamé la función que había creado y se imprimió el resultado.
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

* ATENCIÓN: EN CLASE NOS DIJERON QUE PARA ESTE EJERCICIO SE REALIZABAN 2 CÓDIGOS EN TOTAL
* Mirar archivo Punto_4.py
* Para este primer código usé la función import time que nos pedía el enunciado y use la función que desarrollamos en clase para calcular fibonacci con recursión. En la función main inicié el tiempo, le solicité al usuario ingresar el número de la serie, llamé la serie. Cuando se imprima el resultado de fibonacci, el temporizador se detendrá y se restá la hora de inicio con la hora de fin para mostrar en cuanto tiempo se ejecutó el programa.
```pseudocode
#Para calcular el tiempo cuando un valor es ingresado por el usuario

import time
def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)  

if __name__ == "__main__":
  start_time = time.time()
  num = int(input("Ingrese numero: "))
  serieFibo = fiboRecursivo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
  end_time = time.time()

  timer = end_time - start_time
  print("El tiempo que se demoró el programa fue de: " + str(timer))
```
* Para este segundo código, usé la función import time que nos pedía el enunciado, creé una bandera para usarla en el while la cuál me funcionará para detener todas la operaciones de la función de fibonacci cuando ya se haya demorado un tiempo considerable. Dentro de este while está la función, la función main, inicié el tiempo, establecí un número inicial i el cuál irá aumentando cada vez que se cumpla la condición de que no supere el tiempo de ejecución (para esto hay un condicional if donde mira si el timer lleva más de 5seg), llamé la serie. Cuando el timer de superior a 5seg el proceso se dentendrá, se imprima el resultado de fibonacci hasta el número que se llegó. Se imprimirá tambien el número apartir del cual ya se considera tiempo considerable.
```pseudocode
#Para calcular desde que número de la serie la diferencia de tiempo se vuelve sorgnificativa

import time

bandera = True
i : int = 1  

while bandera == True:

  def fiboRecursivo(n : int )-> int:
   if n <=1:
     # caso base
    return 1
   else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)

  if __name__ == "__main__":
    start_time = time.time()
    num = i
    serieFibo = fiboRecursivo(num)
    end_time = time.time()
    timer = end_time - start_time

  if timer > 5.0: #necesitamos agilidad
    break
  else:
    i=i+1 
print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
print("A partir de este numero se debe considerar un tiempo considerable superior a 5seg")
print("Su tiempo de ejecución hasta aquí fue de : " +str(timer))
```

**5.** Crear cuenta en stackoverflow y adjuntar imagen en el repo

<img width="960" alt="Screenshot 2023-10-10 202249" src="https://github.com/MariaAleja05/Reto9/assets/141857519/7a948f5b-129f-498d-8cf2-27de0fc71d2d">

**6.** Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.
  * Definitivamente eso es algo de adultos, ni siquiera tengo una carrera terminada, ni trabajos anteriores para relacionar 🫤 somos mis idiomas y yo contra el mundo. Ni tengo una foto decente, sería, de alguien que busque trabajo para colocar en mi perfil jajajaj. Es necesario definir la palabra del enunciado: "mamalón", quizás es muy subjetiva, en especial cuando no tienes nada más que añadir en tu perfil jajaaj por ahora, en mis años de juventud me quedaré con Instagram, TikTok y VSCO...porque Facebook también es para viejitos.

www.linkedin.com/in/maría-alejandra-niño-peña-7075b0295
