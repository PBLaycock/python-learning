birth_year = input('Birth year: ')
#print(type(birth_year))

age = 2021 - int(birth_year)
#print(type(age))

print(age)

user_weight_lbs = input('Weight in pounds: ')
user_weight_kg = float(user_weight_lbs) / 2.2046226218
print('So you weigh ' + str(round(user_weight_kg, 2)) + ' kilograms')
