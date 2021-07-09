#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# En un supermercado se hace una promoción mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar. Si el número escogido 
# es menor que 74, se aplicará un descuento del 15% en relación al total de la compra, si es mayor e igual a 74 el descuento aplicado será del 20%. 
# Obtener cuanto dinero se le descuenta.

numero=int(input("Ingrese el numero obtenido "))
compra=float(input("Ingrese el valor de la compra "))
if numero>=74:
    descuento=compra*0.2
    total=compra-descuento
    print("Felicidades ud obtuvo un descuento del 20% en su compra ",total)
else:
    Descuento=compra*0.15
    Total=compra-Descuento
    print("Felicidades ud obtuvo un descuento del 15% en su compra ",Total)