#1
print('Ejercicio 1')
dogdct = {}   
print(dogdct)
#2
print('Ejercicio 2')
dogdct ['Name'] = 'Jake'
dogdct ['Color'] = 'Yellow'
dogdct ['Breed'] = 'Bulldog England'
dogdct ['Legs'] = '4'
dogdct ['Age'] = '34'
print(dogdct)
#3
print('Ejercicio 3')
studentdct = {
    'First name': 'Leonardo',
    'Last name': 'Zamora',
    'Gender': 'male',
    'Age': '19',
    'Material Status': 'Single',
    'Skills': ['Beginer in cybersecutity', 'Beginer in python', 
    'Support and maintenance technician', 'B1 basic in english'],
    'Address': {'State':'Aguascalientes', 
                'City': 'Ags', 
                'Neighborhood': 'Mision de Santa Fe',
                'Street':'Estrella 456'}
}
print(studentdct)
#4
print(len(studentdct))
#5
print(studentdct.get('Skills'))
#6
studentdct['Skills'].extend(['Autodidact', 'Smart'])
print(studentdct)
#7
studntkeys = studentdct.keys()
print(studntkeys)
#8
studentvalues = studentdct.values()
print(studentvalues)
#9
studentlist = studentdct.items()
print(studentlist)
#10
del studentdct['Skills']
print(studentdct)
##11
dogdct = {
    "Nombre": "Firulais",
    "Raza": "Labrador",
    "Edad": 5
}
del dogdct