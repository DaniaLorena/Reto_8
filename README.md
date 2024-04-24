# Reto_8
### Primer punto
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```
#Implementa el ciclo for
#Se pone un rango del 1 hasta el 101 para que se implima la lista solicitada
for i in range(1, 101):
  #El ciclo se repite y en cada iteracion i aumenta y se multiplica por si mismo
  cuadrado : int = i*i
  print (f"EL cuadrado de {i} es {cuadrado}")
```
### Segundo punto
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```
#Se imprime el titulo de la lista
print ("lista numeros impares:")
#Se implementa el bucle for y se inializa en 1 hasta 1000 aumentando en 2 
for i in range(1, 1000, 2): print(i)
print ("La lista de numeros pares es: ")
#Se implementa el bucle for y se inializa en 0 hasta 1001 aumentando en 2 
for i in range(2, 1001, 2): print(i)
```
### Tercer punto
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```
#Se declara el tipo de variable a utilizar
num : int
#Se ingresa el valor de la variable por teclado
num = int( input ("Ingrese un numero"))
#Con if se verificar si el numero es par o no
if (num % 2 != 0):
    #Si es impar se le resta 1 a la cantidad y num toma un numero valor
    num = num-1
#Cuando num cumple que es par se incializa el ciclo con el valor de num hasta llega a 1 dismunuyendo su valor en i
for i in range(num, 1, -2): 
    #Imprime cada iteracion
    print(i)
```

### Cuarto punto
Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```
#Se inicia con declara e inicializar algunas variables
num : int; factorial : int = 1
#Se ingresa por teclado el valor
num = int( input ("Ingrese hasta que numero desea realizar el factorial"))
#Se incializa el ciclo for, el cual va desde 1 hasta en numer ingresado +1
for i in range(1, num+1): 
    #Según la logica del factorial es el producto del un numero por todos los anteriores
    factorial = factorial * i
    #Luego de cada iteracion el valor de factorial va cambiando su valor
    print (f"El factorial de {i} es {factorial}")
 
```
### Quinto punto
Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```
#Se declara e incializan algunas de las variable a utilizar
num : int; potencia : int = 1
num = int (input("Ingrese a el numero de la potencia del 2: "))
#Se implementa el bucle for
for i in range (1, num+1):
    #En cada iteracion se multiplica el valor de potencia por 2 (la base de la potencia) hasta llegar al numero de exponente 
    potencia *= 2 
print (f"La potencia de 2 elevado a {num} es {potencia}")
```
### Sexto punto
Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```
#Se declaran e inicializan las variables
num_1 : int; num_2 : float ; potencia : float = 1
#Se ingresan las variables por teclado
num_1 = int(input ("Ingrese un numero natural: "))
num_2 = float (input("Ingrese un numero real: "))
# se implementa en ciclo for, el cual se va a ejecutar de uno hasta que llegue a numero de la potencia deseada
for i in range (1, num_1+1):
#En cada iteracion se multiplica el valor de la base por la misma hasta llegar al numero de exponente 
    potencia *= num_2

#Se imprime los resultados
print (f"La potencia de {num_2} elevado a {num_1} es {potencia}")
```
### Séptimo punto
Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```
#Se declara e inicializa la variable tabla, la cual va a almacenar los valores
tabla : int = 1
#El ciclo for va desde 1 hasta 9 aumentado en 1
#En este ciclo for "i" va a variar el numero del multiplicador
for i in range (1 , 10, 1):
    #Se imprime un titulo de la tabla que se esta ejecutando
    print("Tabla del " + str(i))
    #Este ciclo for, recorre los valores del multiplicando de cada table
    #Estan en un rango de (1, 11) y va a mostar las multiplicaciones de 1 hasta 10
    for j in range (1, 11):
        #Se realiza la multiplicacion de cada tabla
        tabla = i*j
        #Se imprime las tablas
        print (f"{i} x {j} es: {tabla}")
    #Se deja un espacio entre cada una   
    print()
    
```
### Octavo punto
Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
[![Captura-de-pantalla-2024-04-24-114524.png](https://i.postimg.cc/3wVTGr7w/Captura-de-pantalla-2024-04-24-114524.png)](https://postimg.cc/ns4gbJX8)

```
#Se importa la libreria de math
from math import *
#Se realiza la funcion que evaluara la aproximacion de la serie de Maclaurin
def aproximacion_exponencial (x: float, num: int)-> float:
    #Se declaran e inicializa las variables locales a utilizar
    sumatoria : float = 0
    #Se implementar el ciclo for para realizar la sumatoria
    for i in range(num+1):
        #Se utiliza una funcion externa para calcular el factorial en la expresion 
        factoria = factorial (i)
        #En cada iteracion se va sumando el valor de cada iteración
        sumatoria += (x**i)/factoria
    #Se calcula el valor real 
    valor_real : float = exp(x)
    #Se calcula la diferencia entre el valor real y la sumatoria / su valor aproximado
    dif  : float = valor_real - sumatoria
    #Retorna los valores que se utilizaran en la funcion principal
    return sumatoria, dif

#Se crea una funcion para calcular el factorial de un numero 
def factorial (i: int)->float:
    factorial : int = 1
    #Se incializa el ciclo for, el cual va desde 1 hasta en numer ingresado +1
    for j in range(1, i+1): 
        #Según la logica del factorial es el producto del un numero por todos los anteriores
        factorial = factorial * j
        #Se va dismunuyendo el numero de "i" para que vaya cambiando el valor de en la iteracion de for en la funcion aproximacion_exponencial
        i -=1
    return factorial

#Se implementa la funcion para calcular el numero de terminos para que el porcentaje de error entrela aproximacion y el valor real sea menor de 0.1%
def error (x)-> int:
    #Se declaran e inicializar las variables
    num_terminos : int = 0
    valor_error : float = 0.001 * exp(x)
    #El ciclo while se repite siempre que sea verdadero
    while True:
        #Se inicizan variables siendo igual a las retornadas por la funcion 
        sumatoria, dif = aproximacion_exponencial (x,num_terminos) 
        # Si la diferencia es menor al valor del error se va a ir sumando el numero de terminos necesarios para cumplir con el porcentaje
        if dif < valor_error:  
            #Si esta condicion se cumple se para el ciclo while
            break
        #Si es la diferencia es mayor al valor de error se aumenta 1 en el numeros de terminos 
        num_terminos +=1
    return num_terminos

#Funcion principal
if __name__ == "__main__":
    #Se ingresan los valores por teclado
    x = float (input("Ingrese un valor real: "))
    num = int (input("Ingrese un numero de terminos hasta donde quiere que vaya la serie: "))
    #Se inicizan variables siendo igual a las retornadas por la funcion
    #Se ejecutan las funciones de acuerdo a los valores ingresados por consola
    sumatoria, dif= aproximacion_exponencial (x,num)
    num_termino = error (x)
    print (f"La aproximacion de la funcion exponencial es: {sumatoria}")
    print (f"El valor real es: {exp(x)}")
    print(f"La diferencia entre el valor real y la aproximacion es: {dif}")
    print(f"Se necesitan {num_termino} para que el porcentaje sera menos al 0.1%")

```
### Noveno punto
Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
[![Captura-de-pantalla-2024-04-24-114528.png](https://i.postimg.cc/wT2YVQHZ/Captura-de-pantalla-2024-04-24-114528.png)](https://postimg.cc/BXjzZDjB)
```
#Se importa la libreria de math
from math import *

#Se realiza la funcion que evaluara la aproximacion de la serie de Maclaurin
def serie_maclaurin (x: float, num:int)->float:
    #Se declaran e inicializa las variables locales a utilizar
    sumatoria : int =0
    #Se implementar el ciclo for para realizar la sumatoria
    for i in range (num+1):
         #Se utiliza una funcion externa para calcular el factorial en la expresion
        factoria : float = exp_factorial(i)
        #En cada iteracion se va sumando el valor de cada iteración
        sumatoria += ((-1)**i)*(x**(2*i+1))/factoria
    #Se calcula el valor real  y la diferencia
    valor_real :float = sin (x)
    diferencia :float = valor_real - sumatoria
     #Retorna los valores que se utilizaran en la funcion principal
    return sumatoria, diferencia 

#Se crea una funcion para calcular el factorial basico
def base_factorial (i)->float:
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    return factorial

#Se crea una funcion para calcular el factorial utilizandolo a una expresion 
def exp_factorial (num)->float:
    expresion  = 2 * num + 1
     #Se utiliza una funcion externa para calcular el factorial de la expresion
    exp_factoria = base_factorial (expresion)
    #print (f"El factorial de {num} es en la expresion {expresion} y su valor es : {exp_factoria}")
    return exp_factoria

def error (x)-> int:
    num_terminos : int = 0
    valor_error = 0.001 * sin(x)
    while True:
        sumatoria, diferencia = serie_maclaurin (x,num_terminos) 
        if diferencia < valor_error:  
            break
        num_terminos +=1
    return num_terminos

#Funcion principal
if __name__ == "__main__":
    #Se ingresan los valores por teclado
    x = float (input("Ingrese un valor real: "))
    num = int (input("Ingrese un numero de terminos hasta donde quiere que vaya la serie: "))
    #Se inicizan variables siendo igual a las retornadas por la funcion
    #Se ejecutan las funciones de acuerdo a los valores ingresados por consola
    sumatoria, diferencia = serie_maclaurin (x,num)
    num_terminos = error (x)
    #Se imprimen los valores necesarios
    print (f"La aproximacion de la funcion del seno es: {sumatoria}")
    print (f"El valor real es: {sin(x)}")
    print(f"La diferencia entre el valor real y la aproximacion es: {diferencia}")
    print(f"Se necesitan {num_terminos} para que el porcentaje sera menos al 0.1%")
    
```
### DEcimo punto
Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
[![Captura-de-pantalla-2024-04-24-114534.png](https://i.postimg.cc/vmpJBPLg/Captura-de-pantalla-2024-04-24-114534.png)](https://postimg.cc/Jy56Y5FM)
```
#Se importa la libreria de math
from math import *

#Se realiza la funcion que evaluara la aproximacion de la serie de Maclaurin
def serie_maclaurin (x: float, num: int)-> float:
    #Se evalua si el numero ingresado cumple con el rango establecido
    if (x>= -1 and x<=1):
        #Se declaran e inicializa las variables locales a utilizar
        sumatoria : int = 0
        #Se implementar el ciclo for para realizar la sumatoria
        for i in range (num+1):
            expresion : float = 2*i+1
            #En cada iteracion se va sumando el valor de cada iteración
            sumatoria += ((-1)**i)*(x**expresion) / expresion
        #print (f"LA SUMATORIA ES {sumatoria}")
        #Se calcula el valor real  y la diferencia
        valor_real = atan(x)
        diferencia : float = valor_real - sumatoria
         #Retorna los valores que se utilizaran en la funcion principal
        return sumatoria, diferencia
    #Si el numero esta fuera del rango establecido se muestra el siguiente mensaje
    else :
        print ("ERORR, Debe ingresar un valor entre [-1, 1]")

#Se implementa la funcion para calcular el numero de terminos para que el porcentaje de error entrela aproximacion y el valor real sea menor de 0.1%
def error (x)-> int:
    #Se declaran e inicializar las variables
    num_terminos : int = 0
    valor_error = 0.001 * atan(x)
    #El ciclo while se repite siempre que sea verdader
    while True:
        #Se inicizan variables siendo igual a las retornadas por la funcion 
        sumatoria, diferencia = serie_maclaurin (x,num_terminos) 
        # Si la diferencia es menor al valor del error se va a ir sumando el numero de terminos necesarios para cumplir con el porcentaje
        if diferencia < valor_error:  
             #Si esta condicion se cumple se para el ciclo while
            break
        #Si es la diferencia es mayor al valor de error se aumenta 1 en el numeros de terminos 
        num_terminos +=1
    return num_terminos


 #Funcion principal
if __name__ == "__main__":
    #Se ingresan los valores por teclado
    x = float (input("Ingrese un valor real en el rango de [-1, 1]: "))
    num = int (input("Ingrese un numero de terminos hasta donde quiere que vaya la serie: "))
    #Se inicizan variables siendo igual a las retornadas por la funcion
    #Se ejecutan las funciones de acuerdo a los valores ingresados por consola
    sumatoria, diferencia = serie_maclaurin (x,num)
    num_terminos = error (x)
    print (f"La aproximacion de la funcion arcotangente es: {sumatoria}")
    print (f"El valor real es: {atan(x)}")
    print(f"La diferencia entre el valor real y la aproximacion  de maclaurin en la funcion de ArcoTangete es: {diferencia}")
    print(f"Se necesitan {num_terminos} para que el porcentaje sera menos al 0.1%")
   

```
