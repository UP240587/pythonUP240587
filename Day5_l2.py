#1
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Lista ordenada:", ages)
min_age = min(ages)
max_age = max(ages)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)
#2
ages.append(min_age)
ages.append(max_age)
print("Lista con edades agregadas:", ages)
#3
ages.sort()  
n=len(ages)
if n%2==0:
    median=(ages[n//2-1]+ages[n//2])/2
else:
    median=ages[n//2]
print("Mediana:", median)
#4
average = sum(ages) / len(ages)
print("Promedio:", average)
#5
range_age=max_age-min_age
print("Rango de edades:",range_age)
#6
diff_min_avg = abs(min_age - average)
diff_max_avg = abs(max_age - average)
print("Diferencia min promedio:", diff_min_avg)
print("Diferencia max promedio:", diff_max_avg)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
#7
n = len(countries)
if n%2==1:
    middle_country=countries[n//2]
else:
    middle_country=countries[n//2-1:n//2+1]
print("País(es) del medio:", middle_country)
#8
half = (n + 1) // 2  
first_half = countries[:half]
second_half = countries[half:]
print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)
country1, country2, country3, *scandic_countries = countries
print("Primer país:", country1)
print("Segundo país:", country2)
print("Tercer país:", country3)
print("Países escandinavos:", scandic_countries)