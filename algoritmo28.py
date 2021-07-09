#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar el total de compra teniendo en cuenta el descuento que se le aplica por canttidad de articulos comprados
cantidad=int(input("Ingrese la cantidad de articulos "))
costo=8
costototal=costo*cantidad
IGV=costototal*0.18
total=costototal+IGV
if costototal>=70:
    descuento=total*0.05
    totaldesc=total-descuento
    print("El valor de su compra es de: ",totaldesc)
else:
    print("El valor de su compra es de: ",total)