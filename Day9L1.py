#Level 1
print('Exercise 1 Level 1')
yearsold = int(input("Enter your age: "))
if yearsold >= 18:
    print('You are old enough to learn to drive.')
else:
    print('You need 3 more years to learn to drive.')
#2
print('Ejercicio 2 nivel 1:')
print('Mi edad es de ', yearsold)
yourage = int(input("Ingresa tu edad: "))
print('Quien es mayor')
if yearsold == yourage:
    print('Somos de la misma edad'), ('Los dos tenemos: ', yearsold, 'años')
elif yearsold > yourage:
    print('Yo soy mayor que tu por',yearsold - yourage, 'años')
else:
    print('Eres mayor que yo por', yourage - yearsold, 'años')
print('Ejercicio 3 nivel 1:')
a = int(input('Ingresa un numero: '))
b = int(input('Ingresa otro numero: '))
print('Que numero es mayor')
if a == b:
    print('Ambos numeros son iguales'),('Los dos son de un valor de', a)
elif a > b:
    print('El primer numero es mayor que el segundo por ', a - b)
else:
    print('El segundo numero es mayor que el primero por ', b - a)