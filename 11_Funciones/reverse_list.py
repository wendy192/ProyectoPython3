def reverse_list(lst):
   # lst=['uno','dos','tres','cuatro','cinco']
    for n in range(len(lst)):
        element=lst[-n]
        print('El elemento n={0} es {1}  '.format(n,element))

colores=['blanco','rojo','verde','azul', 'amarillo']
reverse_list(colores)
