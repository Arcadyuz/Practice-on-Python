##Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar el valor de la comision respecto a que tanto se venda
# Si la venta es menor a $1000 se le otorga el 3% de comisión al vendedor.
#Si la venta es de $1000 a mas el vendedor recibirá el 5% de comisión.

venta=float(input("Ingrese el valor de venta: "))
if venta>=1000:
    comision=venta*0.05
    print("Su comision de la venta es de: ",comision)
else:
    Comision=venta*0.03
    print("Su comision de la venta es de: ",Comision)