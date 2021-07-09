#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# hallar el sueldo neto y descuento provisional de un trabajador, tener en cuenta que si un cargo administrativo se le descontará el 12% del sueldo bruto, 
# y si es operativo se le descontara el 17%.

cargo=input("¿Que cargo tiene en la empresa? A/O: ")
sueldo=float(input("Ingrese su sueldo "))
if cargo == "A":
    descuento=sueldo*0.12
    sueldoneto=sueldo-descuento
    print("Su sueldo neto es de: ",sueldoneto)
if cargo == "O":
    Descuento=sueldo*0.17
    Sueldoneto=sueldo-Descuento
    print("Su sueldo neto es de: ",Sueldoneto)