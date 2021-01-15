customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer["age"])
# print(customer("random")) Error

print(customer.get("name"))
print(customer.get("random"))

print(customer.get("birthdate", "Jan 1 1980"))

customer["name"] = "John Apple"
print(customer["name"])

numbers_to_words = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
output = ""
user_input = input("Phone: ")
for ch in user_input:
    output += numbers_to_words.get(ch, "!") + " "

print(output)


