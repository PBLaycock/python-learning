for item in 'Python':
    print(item)
for item in ['Python', 'C++', 'Ruby']:
    print(item)
for item in [1, 2, 3, 4]:
    print(item)

for item in range(5, 15, 2):
    print(item)


prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print(f"total: {total}")
