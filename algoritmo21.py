#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#solucion de ecuacion de 2do grado
#a= 2, b=5, c=1

a=float(input("Ingrese el valor de la variable a: "))
b=float(input("Ingrese el valor de la variable b: "))
c=float(input("Ingrese el valor de la variable c: "))
raiz1=(-b+((b*b)-(4*a*c))**0.5)/(2*a)
raiz2=(-b-((b*b)-(4*a*c))**0.5)/(2*a)
print("las raices son: ",raiz1,raiz2)