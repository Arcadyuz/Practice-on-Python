#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Un alumno desea saber cual será su calificación final en la materia de Matemáticas, dicha calificación se compone por 3 porcentajes , a su vez cada porcentaje tiene cierta cantidad de notas, primero diremos los siguiente:
#parciales 55% examen final 30% trabajos 15%

examenes=float(input("Ingrese nota: "))
examenfinal=float(input("Ingrese nota: "))
trabajos=float(input("Ingrese nota: "))
Exam=examenes*0.55
Finalexam=examenfinal*0.30
Trabajos=trabajos*0.15
Notafinal=Exam+Finalexam+Trabajos
print("Su nota final es de: ",Notafinal)