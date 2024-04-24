'''
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
'''


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