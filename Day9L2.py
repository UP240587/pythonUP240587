#Level 2
print('Ejercicio 1 nivel 2')
calAlumno = int(input('Ingresa tu calificación: '))
if calAlumno > 80 and calAlumno <= 100:
    print('Felicidades tu calificacion es A')
elif calAlumno < 80 and calAlumno >= 70:
    print('Tu calificacion es B')
elif calAlumno < 70 and calAlumno >= 60:
    print('Tu calificacion es C')
elif calAlumno < 60 and calAlumno >= 50:
    print('Tu calificacion es D')
elif calAlumno < 50:
    print('Tu calificacion es F suerte para la proxima vez')
else:
    print('Error tu calificacion no es valida') 
Autumn = {'September', 'Septiembre', 'October', 'Octubre', 'November', 'Noviembre'}
Winter = {'Dicember', 'Diciembre', 'January', 'Enero', 'February', 'Febrero'}
Spring = {'March', 'Marzo', 'April', 'Abril', 'May', 'Mayo'}
Summer = {'June', 'Junio', 'July', 'Julio', 'Agust', 'Agosto'}
month = input('Ingresa un mes para decirte la estacion del año: ')
if month in Autumn:
    print('La estacion del año es Otoño')
elif month in Winter:
    print('La estacion del año es Invierno')
elif month in Spring:
    print('La estacion del año es Primavera')
elif month in Summer:
    print('La estacion del año es Verano')
else:
    print('Error: el mes que ingreso no es valido por favor ingrese uno empezando con mayuscula y lo demas en minusculas')
print('Ejercicio 2 lvl 2')
fruit = input('Ingresa el nombre de una fruta (todo en minusculas): ')
fruits = ['banana', 'orange', 'mango', 'lemon']
print('La lista actual de frutas es: ', fruits)
if fruit in fruits:
    print('Esta fruta ya esta en la lista')
else:
    fruits.append(fruit)
    print('La lista se a actualizado a: ', fruits)