names = ['John', 'Bob', 'Mosh', 'Sarah', 'Marry']
print(names)
print(names[0])
print(names[-2])
print(names[2:-1])
print(names[2:])


numbers = [1, 6, 83, 2, 6, 7, 6]

max_num = max(numbers)
print(max_num)

max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)
