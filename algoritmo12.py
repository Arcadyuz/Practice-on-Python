#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Tenemos un trabajador gana S/69.23 al día, durante 26 días laborables, nos pide hallar cuanto recibe de sueldo y cuanto se aporta a su seguro pensionario si se sabe 
# que el porcentaje de aporte mensual es el 11.74% el cual esta compuesto por : 10%afap 0.38% admon e inversion de fondo, 1.36% seguro

valordia=69.23
dias=26
aportes= 0.1174
sueldo=valordia*dias
porcentaje_de_aporte=sueldo*aportes
print("Su sueldo de este mes es: ",sueldo, "Y sus aportes son: ",porcentaje_de_aporte)