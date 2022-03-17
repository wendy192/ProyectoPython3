"""
print(True)
print(False)
print("Suma: ", 1+2)
print("Resta: ", 8-5)
print("Multiplicación: ", 5*4)
print("Division: ",7/2)
print("Division sin residuo: ",7//2)
print("Division con residuo: ", 7//3)
print("Modulo: ",3%2)
print("Exponente: ",2**3)
"""
print("Numero flotante, PI:", 3.14)
print("Numero flotante, gravity:", 9.81)
#numeros complejos
print("Numeros complejos: ",1+1j)
print("Multiplicacion numeros complejos: ", (1+1j)*(1-1j))

a=3
b=2

total=a+b
diff=a-b
producto=a*b
division=a/b
remainder=a%b
floor_division=a//b
exponencial=a**b

print(total)
print("a+b= ", total)
print("a-b= ",diff)
print("a*b= ", producto)
print("a/b= ",division)
print("a % b= ", remainder)
print("a//b= ",floor_division)
print("a**b= ", exponencial)

print("==Suma, resta, Multiplicacion, Division, Modulo==")
#Declarar valores ty organizarlos juntos

numUno=3
numDos=4

#Operaciones Aritmeticas
total=numUno+numDos
diff=numDos-numUno
producto= numUno*numDos
div= numDos/numUno
residuo=numDos%numUno

print("total = ", total)
print("diferencia= ", diff)
print("producto= ", producto)
print("Division= ", div)
print("residuo= ", residuo)

#Calculo del area del un circulo
radio=10
areaCirculo=3.14*radio**2
print("El area del circulo es= ", areaCirculo)

#calculando el area de un rectangulo
largo=10
ancho=20
areaRectangulo=largo*ancho
print("El area de un rectangulo es ", areaRectangulo)

#Calculando el peso de un objeto
masa=75
gravedad=9.81
peso= masa*gravedad
print(peso, "N")

#Calcular la densidad de una masa
volumen = 0.075
densidad= masa/volumen

#Operadores
print(3>2)
print(3<=2)
print(3<2)
print(2<3)
print(3==2)
print(3!=2)
print(len("mango")==len("aguacate"))
print(len("mango")!=len("aguacate"))
print(len("mango")<len("aguacate"))
print(len("leche")!=len("carne"))
print(len("leche")==len("carne"))