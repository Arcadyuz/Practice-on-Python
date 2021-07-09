#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Diseñar un algoritmo que permita aplicar un descuento en el supermercado de tal forma permita visualizar el monto a pagar después de aplicar dicho procedimiento

descuento=float(input("Por favor ingrese el valor de descuento: "))
costo=float(input("Por favor ingrese el valor de la compra: "))
descuento= descuento/100
valorcondescuento=costo*descuento
total= costo-valorcondescuento
print("Su valor a pagar con descuento es: ",valorcondescuento)
print("El valor a pagar es de: ", total)