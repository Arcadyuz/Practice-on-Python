#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Una tienda ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento el 15% por la compra de mas de 3 docenas y 10% en caso contrario.

cantidad=int(input("Ingrese cuantas docenas lleva "))
costo=float(input("Ingrese el valor de la compra "))
if cantidad > 3:
    descuento=costo*0.15
    valorfinal=costo-descuento
    print("El valor final de su compra con descuento del 15porciento es de ",valorfinal)
else:
    Descuento=costo*0.1
    Valorfinal=costo-Descuento
    print("El valor final de su compra con descuento del 10porciento es de ", Valorfinal)