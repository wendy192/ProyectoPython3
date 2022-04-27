def pendiente (a,b):
    a=float(a)
    b=float(b)
    m=(-1)*(a/b)
    print('el valor de la pendiente es {0}'.format(m))

print('si tu ecuacion es de la forma ax+by+c=0')
a=input('ingresa el valor de a ')
b=input('ingresa el valor de b ')
pendiente(a,b)