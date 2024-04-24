'''
Calcular el valor de 2 elevado a la potencia n usando ciclos for.
'''

#Se declara e incializan algunas de las variable a utilizar
num : int; potencia : int = 1
num = int (input("Ingrese a el numero de la potencia del 2: "))
#Se implementa el bucle for
for i in range (1, num+1):
    #En cada iteracion se multiplica el valor de potencia por 2 (la base de la potencia) hasta llegar al numero de exponente 
    potencia *= 2 
print (f"La potencia de 2 elevado a {num} es {potencia}")