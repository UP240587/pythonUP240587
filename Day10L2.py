#Level 2
# 1
print("\n\n\nLEVEL 2")
print("\n1. Sum of all numbers 0-100:")
total = 0
for i in range(101):
    total += i
print(f"The sum of all numbers is {total}.")

# 2. Sum of evens and odds 0-100
print("\n2. Sum of evens and odds 0-100:")
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")
