#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Si el monto excede  500.000 la empresa invierte el 50% del monto de la compra, pedir prestado el 30% al banco y el 20% lo pagara con credito solicitado al fabricante
#Si no excede el valor, la empresa invierte el 70%, 25% credito al banco y 5% al fabricante

Montodecompra=float(input("Ingrese el valor total de la compra: "))
if Montodecompra>= 500000:
    Inversion=Montodecompra*0.5
    Banco=Montodecompra*0.30
    fabricante=Montodecompra*0.2
    print("Los valores correspondientes son: ",Inversion, "Para inversion" ,Banco, "de prestamo con el banco y ", fabricante, "de deuda con el fabricante ")
else:
    inversion=Montodecompra*0.7
    banco=Montodecompra*0.25
    Fabricante=Montodecompra*0.05
    print("Los valores correspondientes son ",inversion, "Para inversion ",banco, "de deuda con el banco y ",Fabricante, " de deuda con el fabricante")