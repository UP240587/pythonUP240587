#Level 2
fruitptl = ('Strawberry', 'Banana', 'Mango', 'Pineapple', 'Apple', 'Orange')
vegetablestpl = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animalProductstpl = ('Jam', 'Sausage', 'Milk', 'Chesse', 'Cream', 'Meat')
foodStuffTpl = fruitptl + vegetablestpl + animalProductstpl
print(foodStuffTpl[0:8] + foodStuffTpl[9:])
print(foodStuffTpl[3:-3])
del foodStuffTpl
print ('La fruta banana esta en el tuple (Fruits)? ','Banana' in fruitptl)



nordicCountries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia es un pais Nordico? ', 'Estonia' in nordicCountries)
print('Iceland es un pais Nordico? ', 'Iceland' in nordicCountries)
#REVISADO
print("Revisado")