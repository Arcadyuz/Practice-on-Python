#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Diseñar un algoritmo que al momento de ingresar tres números, indicar si hay números iguales y números diferentes, 
# de ser así verificar si están ordenados ascendentemente, descendentemente o desordenados.

Numero1=float(input("Ingrese un numero: "))
Numero2=float(input("Ingrese un numero: "))
Numero3=float(input("Ingrese un numero: "))
if Numero1 != Numero2 and Numero1 != Numero3 and Numero2 != Numero3:
    print("Todos los numeros son diferntes y estan en desorden")
else:
    if Numero3 > Numero2 and Numero2 > Numero1:
        print("Todos los numeros son diferentes y estan en orden ascendente")
    if Numero1 > Numero2 and Numero2 > Numero3:
        print("Todos los numeros son diferentes entre ellos y estan en orden descendente")
if Numero1 == Numero2  and Numero1 == Numero3:
    print("Todos los numeros son iguales entre ellos y al ser iguales no tienen orden")