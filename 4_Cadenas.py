primernombre="Wendy"
apellido="Perez"
languaje="python"
cadena_formateada= "Yo soy %s %s. Yo aprendo %s" %(primernombre,apellido,languaje)
print(cadena_formateada)

radio=10
pi=3.14
area=pi*radio**2
cadena_format="Area de circulo con radio %s es %s" %(radio, area)
print(cadena_format)

librerias = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_cadena = 'The following are python libraries:%s' % (librerias)
print(formated_cadena) 

#Nuevo estilo de formatear cadenas, introducido en Python version 3
a=6
b=7
print("{}+{}={}".format(a,b,a+b))
print("{}-{}={}".format(a,b,a-b))
print("{}*{}={}".format(a,b,a*b))
print("{}/{}={}".format(a,b,b/a))
print("{}%{}={}".format(a,b,a%b))
print("{}//{}={}".format(a,b,a//b))
print("{}**{}={}".format(a,b,a**b))
cadenacirculo="El area del circulo con un radio {} es {}".format(radio,area)
print(cadenacirculo)

#interpolacion con f-strings... las cadenas que comienzan con 
# f pueden inyectar los datos en sus posiciones correspondientes
a2=4
b2=3
print(f'{a2}+{b2}={a2+b2}')
print(f"{a2}-{b2}={a2-b2}")
print(f"{a2}*{b2}={a2*b2}")
print(f"{a2}/{b2}={a2/b2}")
print(f"{a2}%{b2}={a2%b2}")
print(f"{a2}**{b2}={a2**b2}")

#unpacking cadenas de caracteres

a3,b3,c,d,e,f=languaje
print(a3)
print(b3)
print(c)
print(d)
print(e)
print(f)
 #Accediendo a caracteres con listas
print("accediendo a caracteres mediante lista")
letra1=languaje[0]
print(letra1)
letra2=languaje[1]
letra3=languaje[2]
letra4=languaje[3]
letra5=languaje[4]
letra6=languaje[5]
print(letra2)
print(letra3)
print(letra4)
print(letra5)
print(letra6)
#numero determinado de letras
primeras3=languaje[0:3]
ultimas3=languaje[-3:]
otraultimas3=languaje[3:]
print(primeras3)
print(ultimas3)
print(otraultimas3)

#cadenas al reves¡¡¡

saludito="hola mundo fabuloso"
print(saludito[::-1])

challenge="curso de python"
print(challenge.capitalize())
print(challenge.replace("python","codificacion"))
