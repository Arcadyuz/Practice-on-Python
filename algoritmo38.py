#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Diseñar un algoritmo que calcule el valor de R de acuerdo a la siguiente relación:
#R = (A*B) / (C*D) Si X * Y > 0
#R = (A+B) / (C+D) Si X * Y = 0
#R = (A+B) - (C+D) Si X * Y < 0
A=float(input("Ingrese el valor de A: "))
B=float(input("Ingrese el valor de B: "))
C=float(input("Ingrese el valor de C: "))
D=float(input("Ingrese el valor de D: "))
X=float(input("Ingrese el valor de X: "))
Y=float(input("Ingrese el valor de Y: "))
if X*Y > 0:
    R=(A*B) / (C*D)
    print("El valor de R es de: ",R)
if X*Y == 0:
    R=(A+B)/ (C+D)
    print("El valor de R es de: ",R)
if X*Y < 0:
    R=(A+B)-(C+D)
    print("El valor de R es de: ",R)