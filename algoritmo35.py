#El promedio de practicas de un curso se calcula con base en cuatro practicas calificadas de las cuales se elimina la nota menor y se promedian las 3 notas mas altas. 
# Diseñe un algoritmo que determine la nota eliminada y el promedio de practicas de un estudiante.
#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
nota1=float(input("Ingrese nota 1 "))
nota2=float(input("Ingrese nota 2 "))
nota3=float(input("Ingrese nota 3 "))
nota4=float(input("Ingrese nota 4 "))
if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    Notafinal = (nota2+nota3+nota4)/3
    print("Su nota final es de: ",Notafinal)
if nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    Notafinal = (nota1+nota3+nota4)/3
    print("Su nota final es de: ",Notafinal)
if nota3< nota1 and nota3 < nota2 and nota3 < nota4:
    Notafinal = (nota1+nota2+nota4)/3
    print("Su nota final es de: ",Notafinal)
if nota4 < nota1 and nota4 < nota2 and nota4 <nota3:
    Notafinal = (nota1+nota2+nota3)/3
    print("Su nota final es de: ",Notafinal)