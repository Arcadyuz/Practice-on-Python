#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Determina su área y volumen de un cilindro, aplicando un radio ingresando su valor por teclado y también su altura.

r=float(input("Ingrese el radio del cilindro: "))
h=float(input("Ingrese la altura del cilindro: "))
pi=3.1416
SuperficieCilindro= 2*pi*r*(r+h)
volumenCilindro= pi*r*r*h
print("La superficie del cilindro es: ",SuperficieCilindro, "Y su volumen es: ",volumenCilindro)