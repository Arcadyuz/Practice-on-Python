#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobará si su promedio de tres calificaciones es mayor o igual a 12,caso contrario reprobará.

nota1=float(input("Ingrese nota 1 "))
nota2=float(input("Ingrese nota 2 "))
nota3=float(input("Ingrese nota 3 "))
promedio=(nota1+nota2+nota3)/3
if promedio>=12:
    print("Felicitaciones ud aprobo el curso")
else:
    print("Ud reprobo el curso")