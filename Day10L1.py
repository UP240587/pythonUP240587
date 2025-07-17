#Level1
#1
print("0 al 10:")
print("For loop:")
for i in range(11):
    print(i, end=" ")
print("While loop:")
i = 0
while i <= 10:
    print(i, end=" ")
    i += 1
#2
print("10 al 0:")
print("For loop:")
for i in range(10, -1, -1):
    print(i, end=" ")
print("While loop:")
i = 10
while i >= 0:
    print(i, end=" ")
    i -= 1
#3
print("\n\n3. Triangle pattern:")
for i in range(1, 8):
    print('#' * i)

# 4.
print("\n4. 8x8 grid:")
for i in range(8):
    print('# ' * 8)

# 5
print("\n5. Multiplication pattern:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6
print("\n6. Iterate through list:")
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)

# 7
print("\n7. Even numbers 0-100:")
for i in range(0, 101, 2):
    print(i, end=" ")

# 8
print("\n\n8. Odd numbers 0-100:")
for i in range(1, 101, 2):
    print(i, end=" ")

#Level 3

print("\n\nLEVEL 3")
print("\n1. Countries containing 'land':")
"""
from data.countries import countries
land_countries = [country for country in countries if 'land' in country.lower()]
print(land_countries)
"""

# 2. Reverse fruit list
print("\n2. Reverse fruit list:")
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in reversed(fruits):
    reversed_fruits.append(fruit)
print(reversed_fruits)