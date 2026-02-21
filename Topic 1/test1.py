price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffe_pack = 4.42

num_croissants = int(input("Введіть кількість круассанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffe_packs = int(input("Введіть кількість упаковок кави: "))

total_cost = num_croissants * price_per_croissant + \
            num_glasses * price_per_glass + \
            num_coffe_packs * price_per_coffe_pack

total_dollars = int(total_cost)
total_cents = int(total_cost * 100)

print (f"Загальна вартість у повних доларах: {total_dollars} доларів")
print(f"Загальна вартість у центах: {total_cents} центів")