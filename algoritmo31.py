##Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar el pago total de horas de trabajos 
# Teniendo en cuenta el numero de horas diurnas y nocturnas que trabajo un empleado 
# durante el día elaborar un algoritmo que calcule cuanto debe pagársele si se le debe descontar un 1% si gana mas de $600.

tarifadiurna=50
tarifanocturna=80
horasdiurnas=float(input("Ingrese el numero de horas diurnas laboradas: "))
horasnocturnas=float(input("Ingrese el numero de horas nocturnas laboradas: "))
pagodiurno=tarifadiurna*horasdiurnas
pagonocturno=tarifanocturna*horasnocturnas
pagototal=pagodiurno+pagonocturno
if pagototal>600:
    descuento=pagototal*0.01
    pagodesc=pagototal-descuento
    print("Su pago es de: ",pagodesc)
else:
    print("Su pago es de: ",pagototal)