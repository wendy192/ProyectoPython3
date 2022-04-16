"""
person={
"first_name":"Wendy",
"apellido":"perez",
'edad':250,
'pais':'Mexico',
'casada':False,
'skills':['java','php','sql','react'],
'direccion':{
    'calle':'Street 33',
    'codigopostal':555882
}
}

#person['puesto']='instructor'
#person['skills'].append('HTML')

person['first_name']='Eyob'
person['edad']=333
print(person)
"""
perro={}
perro['nombre']='firulais'
perro['raza']='labrador'
perro['patas']='largas'
perro['edad']='88'

estudiante={}
estudiante['nombre']='fulanito'
estudiante['apellido']='lopez'
estudiante['sexo']='masculino'
estudiante['skills']=['python','HTML','java','SQL']
estudiante['pais']='Mexico'
estudiante['ciudad']='CDMX'
#print(len(estudiante))
#estudiante['skills'].append('CSS')
#
llaves=estudiante.keys()
print(llaves)
# del perro
del estudiante['nombre']
print(estudiante)
