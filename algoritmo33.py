##Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar el precio del alquiler del auto dependiendo del kilometraje
# 3000 los 300km, de 300 a 1000km hay un adicional de 1500 cada kilometro, si es mas de 1000km cobran 1000 cada kilomero adicional, tener en cuenta el IGV del 18%

kilometros=float(input("Ingrese la cantidad de kilometros recorridos: "))
Km = kilometros-300
if kilometros <= 300:
    Alquiler=3000+(3000*0.18)
    print("Su alquiler es de: ",Alquiler)
if kilometros > 300 and kilometros <= 1000:
    Alquiler=(3000+(1500*Km))+((3000+(1500*Km))*0.18)
    print("Su alquiler es de: ",Alquiler)
if kilometros > 1000:
    Km=kilometros-1000
    Alquiler=(3000+(1000*Km))+((3000+(1000*Km))*0.18)
    print("Su alquiler es de: ",Alquiler)