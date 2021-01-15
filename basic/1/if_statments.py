is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


house_price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2
print(f"Down payment: {down_payment}$")