"""

def  generar_nombre_completo ():
        nombre = 'Asabeneh' 
        apellido  = ' Yetayeh ' 
        espacio = ' ' 
        nombre_completo = nombre + espacio + apellido 
        print ( nombre_completo )
generar_nombre_completo () 

def  sumar_dos_numeros ():
     num_uno  =  2
     num_dos  =  3 
     total  =  num_uno  +  num_dos 
     print ( total )

sumar_dos_numeros ()

def saludos(nombre):
        mensaje=nombre+'Bienvenidos'
        return mensaje
print (saludos ('FUlanita '))

def sumar_diez(num):
        diez=10
        return num+ diez
print(sumar_diez(90))


def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))
"""
def pesoobjeto(masa,gravedd=9.81):
        peso=str(masa*gravedd)+'N'
        return peso
print('El peso de un objeto en Newtons es ', pesoobjeto(100,1.62     ))
