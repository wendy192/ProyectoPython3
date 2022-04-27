def seasons (mes):
    mes=int(mes)
    primavera=(3,4,5)
    verano=(6,7,8)
    otoño=(9,10,11)
    invierno=(1,2,12)
   
    if mes in primavera:
        print('el mes es primavera')
    if mes in verano:
        print('es verano')
    if mes in otoño:
        print(' es otoño')
    if mes in invierno:
        print('es invierno')
    
mes=input('ingresa mes ')
seasons(mes)