#La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. 
# Escriba una función que calcule el conjunto de soluciones de una 
# ecuación cuadrática, solve_quadratic_eqn
# 
from cmath import sqrt


def solvequadratic(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    if a!=0:
        x1=((-1)*b+sqrt((b**2)-4*a*c))/2*a
        x2=((-1)*b-sqrt((b**2)-4*a*c))/2*a
        print('las soluciones a la ecuacion que planteaste es x1={0} y x2={1}'.format(x1,x2))
    else:
        print('La ecuacion no tiene solucion porque a=0')
print('Solucion a la ecuacion cuadratica de la forma ax´2+by+c=0')
a=input('Ingresa el valor de coheficiente a ')
b=input('Ingresa el valor del coheficiente b ')
c=input('Ingresa el valor del coheficiente c ')
solvequadratic(a,b,c)