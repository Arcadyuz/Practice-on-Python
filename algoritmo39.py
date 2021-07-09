#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar grado de eficiencia de una empleadoa base de cuantos tornillos produce
Tornillos=int(input("Ingrese la cantidad de tornillos hechos: "))
if Tornillos < 300:
    print("Tiene una eficiencia de grado 1")
if Tornillos >= 300 and Tornillos < 1000:
    print("Tiene una eficiencia de grado 2")
if Tornillos >= 1000:
    print("Tiene una eficiencia de grado 3")