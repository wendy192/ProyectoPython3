
def agregaitem(lst):
    #lst=['a','b','c', 'd','e']
    n=len(lst)
    letra=input('escribe la letra que quieres ingresar ')
    letra=str(letra)
    lst.insert(n+1,letra)
    print(lst)

lst=['j','k','l','m']
print(agregaitem(lst))






