#Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.


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
    