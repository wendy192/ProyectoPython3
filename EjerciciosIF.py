#Ejercicios de if
#Determinar el mayor entre dos numeros, tomando en cuenta si son iguales
"""
print("Determina el mayor de dos numeros")

x= int(input("ingresa el primer numero  "))
y= int(input("ingresa el segundo numero  "))

if x<y:
    print("el numero mayor es ",y)
elif y<x:
    print("el numero mayor es ",x)
else:
    print("los numeros son iguales")
"""
###################
#Requerir al usuario que ingrese un día de la semana e 
#imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, 
#otro mensaje diferente si es sábado o domingo. 
#Si el día ingresado no es ninguno de esos, imprimir otro mensaje
"""
print("Dia de la semana")
print("Escoge uno de los siguientes dias de la semana, ingresa su numero ")
#le doy a escoger al usuario con numeros para evitar los posibles problemas con las mayusculas
#y los acentos, ese tema aun no le he aprendido
str=1,2,3,4,5,6,7

print("1.-Lunes")
print("2.-Martes")
print("3.-Miercoles")
print("4.-Jueves")
print("5.-Viernes")
print("6.-Sabado")
print("7.-Domingo")
dia=input(">>> ")
if (dia=="1"):
    print("Escogiste el mejor dia, unicia la semana con lunes ")
elif (dia=="5"):
    print("Escogiste el dia viernes")
elif (dia=="6"):
    print("Escogiste el dia de descanso sabroso, sabado")
elif (dia=="7"):
    print("Elegiste el dia soleado, domingo")
else: 
    print("No escogiste ningun dia chevere¡¡")
"""
###################
#Escribir un programa que, dado un número entero, muestre su valor absoluto.
# Nota: para los números positivos su valor absoluto es igual al número
# (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto 
# es el número multiplicado por -1 (el valor absoluto de -52 es 52).
"""
from re import X
from socket import NI_NUMERICHOST


print("valor absoluto")
x= int(input("ingresa el numero "))
if (x>0):
    print("El valor absoluto es ",x)
else: 
    print("El valor absoluto del negativo es ",x*-1)
"""
####################
#Solicitar al usuario que ingrese los nombres de dos personas, 
#los cuales se almacenarán en dos variables. 
# A continuación, imprimir “coincidencia” si los nombres de ambas personas 
#comienzan con la misma letra ó si terminan con la misma letra.
#Si no es así, imprimir “no hay coincidencia”
"""
import string


print("Nombres de personas")
nom1=str(input("ingrese el primer nombre >> "))
nom2=str(input("ingrese el segundo nombre >> "))
string = nom1
string=nom2
if (nom1[0:1]==nom2[0:1]):
    print("Son tocayos de letra inicial ¡¡¡")
elif(nom1[-1]==nom2[-1]):
    print ("Son tocayos de letra final¡¡")
else:
    print("No hay coincidencias. Siga participando")

"""
#################################
#Crear un programa que permita al usuario elegir un candidato por el cual votar. 
#Las posibilidades son: 
#candidato A por el partido rojo, 
#candidato B por el partido verde, 
#candidato C por el partido azul. 
#Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje 
# “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
#Si el usuario ingresa una opción que no corresponde a ninguno de 
# los candidatos disponibles, indicar “Opción errónea”.

"""

print("Elegir candidatos")
print("Elige por letra, uno de los siguientes candidatos")
print("a) CandidatoR")
print("b) CandidatoV")
print("c) CandidatoA")
a=str
b=str
c=str
x=input(" >> ")

if (x=="a"):
    print("Has elegido al candidato del partido Rojo ")
elif(x=="b"):
    print("Elegiste al partido Verde ")
elif(x=="c"):
    print("Has elegido al candidato del partido Azul")
else: ("Opcion erronea")
"""

