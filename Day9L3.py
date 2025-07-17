#Level 3
print('Ejercicio 1 nivel 3')
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
print(person)
print('problematica 1: Conseguir las keys de enmedio de skills')
midskillskeys = len(person.get('skills'))//2
print('Las habilidades de enmedio son ', person['skills'][midskillskeys])
print('problematica 2: Checar si la persona tiene de habilidad el uso de python')
if 'Python' in person['skills']:
    print('Si la persona tiene la habilidad de Python en: habilidades: ', person['skills'])
else:
    print('La persona no tiene la habilidad de Python en sus habilidades')
print('''Problematica 3: revisar si la persona tiene solo las habilidades de JavaScript y React devolver
      que la persona es un front end developer, si la persona tiene la hablidad de Node, Python, MongoDB
      devolver que la persona es un backend developer, 
      si la persona tiene las habilidades Node and MongoDB devolver es un fullstack developer, 
      si no devolver unknown title.
      ''')
frontDev = 'JavaScript' in person['skills'] and 'React' in person['skills']
backendDev = 'Node,' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']
fullstackDev = 'React' in person['skills'] and 'Node' in person['skills']  and 'MongoDB' in person['skills']
if frontDev == True and len(person['skills']) == 2 :
    print("El programador es un (Front end developer)")
elif backendDev == True and len(person['skills']) == 3:
    print('El programador es un (Backend developer)')
elif fullstackDev == True:
    print('El programador es un (Fullstack developer)')
else:
    print('unknown title')
print('''Problematica 4 y ultima:
Si la persona esta casada y vive en findlandia deolver la informacion en el siguiente orden 
(Nombre, Apellido, donde vive, y si esta casado)      
''')
if person['is_marred'] == True and 'Finland' in person['country']:
    print('''
     Asabeneh Yetayeh vive en Finland, el es casado
    ''')
else:
    print('Una de las condiciones no coinciden')
print("revisado")