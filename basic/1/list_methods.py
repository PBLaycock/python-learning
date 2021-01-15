numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 12)
numbers.remove(4)
numbers.pop()
print(numbers)
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)

numbers2 = numbers.copy
#numbers2.append(10)

print(numbers)
print(numbers2)

# remove duplicates
numbers3 = [2, 8, 2, 5, 5, 1, 6, 2, 5]
for index in numbers3:
    for num in numbers3:
        if num == index:
            numbers3.remove(index)
print(list(numbers3))

numbers3 = [2, 8, 2, 5, 5, 1, 6, 2, 5]
uniques = []
for number in numbers3:
    if number not in uniques:
        uniques.append(number)
print(uniques)
