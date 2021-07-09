#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar si una persona es apta para servicio militar o no
genero=str(input("Por favor indique su genero M/H "))
edad=int(input("Por favor ingrese su edad "))
if genero =="H":
    if edad>=18 and edad<=25:
         print("Ud es apto para servicio militar")
print("Ud no es apto para el servicio militar ")