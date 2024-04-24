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