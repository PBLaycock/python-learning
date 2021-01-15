user_weight = input("Weight: ")
user_weight_unit = input("Lbs or Kg: ")

converted_user_weight = "unknown"

weight_unit = user_weight_unit.lower()

if weight_unit == "lbs":
    converted_user_weight = round(float(user_weight) / 2.20462262, 2)
elif weight_unit == "kg":
    converted_user_weight = round(float(user_weight) * 2.20462262, 2)
else:
    'Weight type entered incorrectly, please enter "lbs" or "kg"'

print(f"You are {converted_user_weight} {weight_unit}.")
