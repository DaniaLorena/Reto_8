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
   