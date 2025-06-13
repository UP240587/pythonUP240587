#1
lista = []
#2
lista = [1, 2, 3, 4, 5, 6, 7]
#3
lista_larga = len(lista)
print(lista_larga)
#4
primer_elemento = lista[0]
item_mediano = lista[len(lista)//2]
item_final = lista[-1]
print("First, middle, last items:", primer_elemento, item_mediano, item_final)
#5
mixed_data_types = ["John Doe", 30, 1.75, "Single", "123 Main St"]
#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#7
print("IT Companies:", it_companies)
#8
print("Number of companies:", len(it_companies))
#9
print("First, middle, last company:", it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])
#10
it_companies[1] = "Alphabet"
print("Modified list:", it_companies)
#11
it_companies.append("Tesla")
print("After adding Tesla:", it_companies)
#12
it_companies.insert(len(it_companies)//2, "Netflix")
print("After inserting Netflix:", it_companies)
#13
it_companies[0] = it_companies[0].upper()
print("After uppercasing first company:", it_companies)
#14
joined_str = '#;  '.join(it_companies)
print("Joined string:", joined_str)
#15
print("Is Google in list?", "Google" in it_companies)
#16
it_companies.sort()
print("Sorted list:", it_companies)
#17
it_companies.reverse()
print("Reversed list:", it_companies)
#18
first_three = it_companies[:3]
print("First three companies:", first_three)
#19
last_three = it_companies[-3:]
print("Last three companies:", last_three)
#20
middle_index = len(it_companies)//2
middle_company = it_companies[middle_index] if len(it_companies) % 2 != 0 else it_companies[middle_index-1:middle_index+1]
print("Middle company/companies:", middle_company)
#21
del it_companies[0]
print("After removing first company:", it_companies)
#22
middle_index = len(it_companies)//2
if len(it_companies) % 2 != 0:
    del it_companies[middle_index]
else:
    del it_companies[middle_index-1:middle_index+1]
print("After removing middle company/companies:", it_companies)
#23
it_companies.pop()
print("After removing last company:", it_companies)
#24
it_companies.clear()
print("After clearing all companies:", it_companies)
#25
del it_companies
# 26-27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
full_stack = joined_list.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print("Joined list:", joined_list)
print("Full stack:", full_stack)