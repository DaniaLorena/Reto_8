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
    