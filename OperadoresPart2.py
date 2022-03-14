#Realice los sigientes ejercicios
#1.Declara tu edad como variable entera
#2.Declara tu altura como una variable flotante
#3.Declarar una variable que almacene un número complejo
#4.Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y 
# calcule el área de este triángulo (área = 0,5 xbxh)
"""
edad= 45
estatura=1.6
complex=1+3j
print("Calcular el area de un triangulo")
base= input("ingrese base =")
altura=input("ingrese altura=")
area=float(base)*float(altura)*0.5
print("el area es= ", area)
"""

#5.Escriba un script que solicite al usuario que ingrese el lado a, 
# el lado b y el lado c del triángulo. 
# Calcula el perímetro del triángulo (perímetro = a + b + c).
"""
print("Calcular el perimetro de un triangulo ")
ladoA=input("Ingrese el valor del lado A= ")
ladoB=input("Ingrese el valor del lado B= ")
ladoC=input("ingrese el valor del lado C= ")

peri=float(ladoA)+float(ladoB)+float(ladoC)
print("el perimetro del triangulo es ", peri)
"""
#6.Obtenga la longitud y el ancho de un rectángulo usando el prompt. 
# Calcula su área (área = largo x ancho) 
# y perímetro (perímetro = 2 x (largo + ancho))
"""
print("Calcula el area y perimetro de un rectangulo")
largo=input("Ingresa el largo del retangulo ")
ancho=input("ingresa el ancho del rectangulo ")
area=float(largo)*float(ancho)
peri=2*(float(ancho)+float(largo))

print("el preimetro del rectangulo es ", peri)
print("El area del rectangulo es ", area)
"""
#7. Obtenga el radio de un círculo usando el prompt. 
# Calcula el área (área = pi xrxr) y 
# la circunferencia (c = 2 x pi xr) donde pi = 3,14
"""
print("Calcular el area y circunferncia de un circulo, dado el radio")
r=input("Ingrese el valor del radio ")
pi=3.14
area=pi*float(r)**2
circun= 2*pi*float(r)

print("El area del circulo es ", area)
print("La circunferencia del circulo es ", circun)
"""
#8. Calcule la pendiente, la intersección x y la intersección y de y = 2x -2
# Despejando manualmente x en funcion de y, tenemos que x=(y+2)/2
# inicializo las variables x y y a cero para obtener las intersecciones
"""
x0=float(0)
y0=float(0)

#defino la funcion y cuando x=0 como 
fny= 2*x0-2

#defino la funcion x cuando y=0 como 
fnx=(y0+2)/2

#Calculo la pendiente m, dados los puntos obtenidos
m= (float(fny)-float(y0))/(float(x0)-float(fnx))

#imprimo
interseccX="La interseccion con el eje x es ("
interseccY="La interseccion con el eje y es ("
coma=" , "
parentesisfinal=")"
print ("Intersecciones en los ejes de la ecuacion y=2x-2")
print(interseccX+str(fnx)+coma+str(y0)+parentesisfinal)
print(interseccY+str(x0)+coma+str(fny)+parentesisfinal)
print("La pendiente de la ecuacion y=2x-2 es ", m)

#Calculando la pendiente de cualesquiera dos puntos m=(y2-y1)/(x2-x1)
print("Calcular la pendiente dados dos puntos cualquiera")
#Solicitamos los valores del primer punto (x1,y1)
x1=input("ingresa el valor de x en el primer punto>> ")
y1=input("Ingresa el valor de y en el primer punto>> ")

#Solicitamos los valores del segundo punto (x2,y2)
x2=input("Ingresa el valor de x en el segundo punto>> ")
y2=input("ingresa el valor de y en el segundo punto>> ")

#Implementamos la formula de la pendiente m
m2=(float(y2)-float(y1))/(float(x2)-float(x1))

#Imprimo
print("La pendiente de la recta con los puntos dados es ", m2)
"""
#9.La pendiente es (m = y2-y1/x2-x1). 
# Encuentre la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6,10)
"""
from cmath import sqrt


print("Pendiente y Distancia euclidiana")

x1=2
y1=2
x2=6
y2=10
m=(float(y2)-float(y1))/(float(x2)-float(x1))
d=((x2-x1)**2-(y2-y1)**2)
distancia=sqrt(d)
print("La pendiente es ",m)
print("La distancia es ", distancia)
"""
#Calcula el valor de y (y = x^2 + 6x + 9). 
# Trate de usar diferentes valores de x 
# y descubra en qué valor de x y será 0
"""
x=input("Ingrese el valor de x>> ")
y=(float(x)**2)+(6*float(x))+9
print("El valor de y es ", str(y))
"""
#Encuentre la longitud de 'python' y 'dragon' y 
# haga una declaración de comparación falsa.

p=len("PYTHON")
d=len("dragon")
comp=p<d
print(comp)
print(len("python")<len("dragon"))
#Use un operador para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'
py="python"
drag="dragon"
print(drag.find("on"))