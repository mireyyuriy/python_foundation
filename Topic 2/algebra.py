name = "Taras"
age = 22
has_driver_license = True

if name and age >= 18 and has_driver_license:
    print(f'User {name} can rent a car')


num = int(input("Vvedyt chyslo: "))

length = len(str(num))

if length == 2 and num % 2 == 0:
    print("parne dvuznachne chislo")
else:
    print("Ni")

num = int(input())

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

x = int(input("X: "))
y = int(input("Y: "))

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

result = y / x

if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("Перша чверть")
    else:  # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:  # x < 0, y > 0
        print("Друга чверть")
    else:  # x < 0, y < 0
        print("Третя чверть")

