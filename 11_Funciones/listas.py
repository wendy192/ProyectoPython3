
def listas (frutas):
    frutas=['melon','fresa','limon','uvas','sandia']
    for n in range(len(frutas)):
        una=(frutas[n])
        print('fruta', una)
        #return una 


def sumarizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma

frutas=['melon','fresa','limon','uvas','sandia']
print(listas(frutas))
lista=[1,2,3,4]
print(sumarizar(lista))