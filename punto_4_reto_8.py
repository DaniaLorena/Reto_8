'''
Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
'''

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
 