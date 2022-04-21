#num=[0,1,2,3,4,5,6,7,8,9,10]
#for x in num:
 #   print(x,'x',x,'=',x*x)
"""  
list=['Python','Numpy','Pandas','Django','Flask']
for x in list:
    print(x)

list=list(range(101))
print(list)
for x in list:
    print('x =',x)
    suma=x*(x+1)/2
    print('suma=',int(suma))

#list=list(range(0,10,2)) 
#print(list)
num=list(range(2,101,2))
print(num)
for x in range(2,51):
    pares=x*(x+1)
   
    print('suma de pares para el par numero',x, 'la suma es',pares)

paises  = [
  'Afganistán' ,
  'Albania' ,
  'Argelia' ,
  'Andorra' ,
  'Angola' ,
  'Antigua y Barbuda' ,
  'Argentina' ,
  'Armenia' ,
  'Australia' ,
  'Austria' ,
  'Azerbaiyán' ,
  'Bahamas' ,
  'Baréin' ,
  'Bangladés' ,
  'Barbados' ,
  'Bielorrusia' ,
  'Bélgica' ,
  'Belice' ,
  'Benín' ,
  'Bután' ,
  'Bolivia' ,
  'Bosnia y Herzegovina' ,
  'Botsuana' ,
  'Brasil' ,
  'Brunéi' ,
  'Bulgaria' ,
  'Burkina Faso' ,
  'Burundí' ,
  'Camboya' ,
  'Camerún' ,
  'Canadá' ,
  'Cabo Verde' ,
  'República Centroafricana' ,
  'chad' ,
  'Chile' ,
  'china' ,
  'Colombia' ,
  'Comoras' ,
  'Congo (Brazzaville)' ,
  'Congo' ,
  'Costa Rica' ,
  "Costa de Marfil" ,
  'Croacia' ,
  'Cuba' ,
  'Chipre' ,
  'República Checa' ,
  'Dinamarca' ,
  'Yibuti' ,
  'Dominica' ,
  'República Dominicana' ,
  'Timor Oriental (Timor Timur)' ,
  'Ecuador' ,
  'Egipto' ,
  'El Salvador' ,
  'Guinea Ecuatorial' ,
  'Eritrea' ,
  'Estonia' ,
  'Etiopía' ,
  'Fiyi' ,
  'Finlandia' ,
  'Francia' ,
  'Gabón' ,
  'Gambia, La' ,
  'Georgia' ,
  'Alemania' ,
  'Gana' ,
  'Grecia' ,
  'Granada' ,
  'Guatemala' ,
  'Guinea' ,
  'Guinea-Bisáu' ,
  'Guyana' ,
  'Haití' ,
  'Honduras' ,
  'Hungría' ,
  'Islandia' ,
  'India' ,
  'Indonesia' ,
  'Irán' ,
  'Irak' ,
  'Irlanda' ,
  'Israel' ,
  'Italia' ,
  'Jamaica' ,
  'Japón' ,
  'Jordania' ,
  'Kazajistán' ,
  'Kenia' ,
  'Kiribat' ,
  'Corea del Norte' ,
  'Corea del Sur' ,
  'Kuwait' ,
  'Kirguistán' ,
  'Laos' ,
  'Letonia' ,
  'Líbano' ,
  'Lesoto' ,
  'Liberia' ,
  'Libia' ,
  'Liechtenstein' ,
  'Lituania' ,
  'Luxemburgo' ,
  'Macedonia' ,
  'Madagascar' ,
  'Malaui' ,
  'Malasia' ,
  'Maldivas' ,
  'Malí' ,
  'Malta' ,
  'Islas Marshall' ,
  'Mauritania' ,
  'Mauricio' ,
  'México' ,
  'Micronesia' ,
  'Moldavia' ,
  'Mónaco' ,
  'Mongolia' ,
  'Marruecos' ,
  'Mozambique' ,
  'Birmania' ,
  'Namibia' ,
  'Nauru' ,
  'Nepal' ,
  'Países Bajos' ,
  'Nueva Zelanda' ,
  'Nicaragua' ,
  'Níger' ,
  'Nigeria' ,
  'Noruega' ,
  'Omán' ,
  'Pakistán' ,
  'Palau' ,
  'Panamá' ,
  'Papúa Nueva Guinea' ,
  'Paraguay' ,
  'Perú' ,
  'Filipinas' ,
  'Polonia' ,
  'Portugal' ,
  'Catar' ,
  'Rumania' ,
  'Rusia' ,
  'Ruanda' ,
  'San Cristóbal y Nieves' ,
  'Santa Lucía' ,
  'San Vicente' ,
  'Samoa' ,
  'San Marino' ,
  'Sao Tomé y Príncipe' ,
  'Arabia Saudita' ,
  'Senegal' ,
  'Serbia y Montenegro' ,
  'Seychelles' ,
  'Sierra Leona' ,
  'Singapur' ,
  'Eslovaquia' ,
  'Eslovenia' ,
  'Islas Salomón' ,
  'Somalia' ,
  'Sudáfrica' ,
  'España' ,
  'Sri Lanka' ,
  'Sudán' ,
  'Surinam' ,
  'Suazilandia' ,
  'Suecia' ,
  'Suiza' ,
  'Siria' ,
  'Taiwán' ,
  'Tayikistán' ,
  'Tanzania' ,
  'Tailandia' ,
  'Togo' ,
  'Tonga' ,
  'Trinidad y Tabago' ,
  'Túnez' ,
  'Turquía' ,
  'Turkmenistán' ,
  'Tuvalu' ,
  'Uganda' ,
  'Ucrania' ,
  'Emiratos Árabes Unidos' ,
  'Reino Unido' ,
  'Estados Unidos' ,
  'Uruguay' ,
  'Uzbekistán' ,
  'Vanuatu' ,
  'Ciudad del Vaticano' ,
  'Venezuela' ,
  'Vietnam' ,
  'Yemen' ,
  'Zambia' ,
  'Zimbabue' ,
]
  
subcadena = 'ia'
paises_con_ia = [var_lista #se define la variable que va a contener la sublista resultante
#tambien se crea la variable var_lista que aun no entiendo bien como va a funcionar
for var_lista in paises #inicializamos el bucle, var_lista aqui cumple la funcion de ser una de apoyo para el for, en lugar de inicializarla antes como en los otros lenguajes de programacion
    if subcadena in var_lista]#el for va a iterar en cada uno de los elementos de la lista paises y pregunta 
    #si la subcadena definida arriba se encuetra entre los elementos de var_lista
    #Si es correcto, entonces imprime el contenido de la lista paises con ia
print(paises_con_ia)



"""
#frutas=['banana', 'orange', 'mango', 'lemon'] 
fruta=['platano']
#alreves=[numero
#for numero in frutas
    print(frutas[::-1])
    #print(frutas)
    ]
#greeting = 'Hello, World!'
#print(greeting[::-1]) # !dlroW ,olleH

