'''
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
'''

#Implementa el ciclo for
#Se pone un rango del 1 hasta el 101 para que se implima la lista solicitada
for i in range(1, 101):
  #El ciclo se repite y en cada iteracion i aumenta y se multiplica por si mismo
  cuadrado : int = i*i
  print (f"EL cuadrado de {i} es {cuadrado}")