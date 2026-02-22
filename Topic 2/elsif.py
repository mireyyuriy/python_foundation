num = 15  # приклад значення для num

if num > 10:
    print("num більше за 10")
else:
    print("num не більше за 10")

x = int(input('Введіть число: '))

if x % 2 == 0 :
    print('число є парним')
else:
    print('число є непарним')

a = input('Введіть число: ')
a = int(a)

if a > 0:
    print('chyslo dodatne')
elif a < 0:
    print('chyslo vydyemne')
else:
    print('thse chyslo null')

money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")

result = None
if result:
    print(result)
else:
    print("Result is None, do something")

user_name = input ('Enter your name: ')

if user_name:
    print(f"Hello {user_name}")
else:
    print('Hello anonym')


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False