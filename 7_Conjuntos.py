it_co={"facebook","google","microsoft","apple","ibm","oracle","amazon"}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
edad=[22,19,24,25,26,24,25,24]
print("Ejercicios de conjuntos en Python")
"""#print(len(it_co))
it_co.add("Twitter")
it_co.update(["firefox","discord"])
#it_co.clear()
#it_co.pop()
#print(it_co)
C=A.union(B)
#C=A.intersection(B)
D=B.union(A)
C.update(D)
print(D)
print("Son A y B conjuntos disjuntos?",B.isdisjoint(A))
print("Cual es la diferencia simetrica entre A y B", B.symmetric_difference(A))
"""
#Convierta las edades en un conjunto y compare la longitud
#de la lista y el conjunto, ¿cuál es más grande?
cjtoEdad=set(edad)
print("Longitud de lista ", len(edad))
print("Longitud de conjunto ", len(cjtoEdad))
print(cjtoEdad)

