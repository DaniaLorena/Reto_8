'''
Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.
'''

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