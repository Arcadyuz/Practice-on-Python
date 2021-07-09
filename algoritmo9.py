#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Defina un algoritmo que permita calcular la nota final de un alumno, teniendo en cuenta que ha realizado 3 evaluaciones y que cada evaluación esta sometida a un peso , el cual es:
#25% 45% 30%

exam1=float(input("Ingrese nota: "))
exam2=float(input("Ingrese nota: "))
exam3=float(input("Ingrese nota: "))
Exam1=exam1*0.25
Exam2=exam2*0.45
Exam3=exam3*0.30
Definitiva=Exam1+Exam2+Exam3
print("Su nota final es de: ",Definitiva)