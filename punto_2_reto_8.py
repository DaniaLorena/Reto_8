'''
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

'''


#Se imprime el titulo de la lista
print ("lista numeros impares:")
#Se implementa el bucle for y se inializa en 1 hasta 1000 aumentando en 2 
for i in range(1, 1000, 2): print(i)
print ("La lista de numeros pares es: ")
#Se implementa el bucle for y se inializa en 0 hasta 1001 aumentando en 2 
for i in range(2, 1001, 2): print(i)