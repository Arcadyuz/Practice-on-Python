#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# En un salón de clase nos pide diseñar un algoritmo que permita determinar el porcentaje de varones y el porcentaje de mujeres
#Cantidad de Niños 78 - Niñas 43.

niños=int(input("Ingrese la cantidad de niños en el salon: "))
niñas=int(input("Ingrese la cantidad de niñas en el salon: "))
total=niños+niñas
varones=(niños/total)*100
mujeres=(niñas/total)*100
print("El porcentaje de varones es: ",varones, "y el de mujeres es: ",mujeres)
