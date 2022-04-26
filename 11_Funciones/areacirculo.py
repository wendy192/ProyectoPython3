
#funcion pra calcular el area de un circulo
def areacirculo(r):
    
    r=float(r)
    pi=3.14
    area=pi*r*r
    print('El area del circulo {0}  es {1}'.format(r,area))
r=input('Ingresa el radio ')
areacirculo(r)


