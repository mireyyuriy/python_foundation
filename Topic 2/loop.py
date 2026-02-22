fruit = 'apple'
for char in fruit:
    print(char)


alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")


some_iterable = ["a", "b", "c"]

for i in some_iterable:
    print(i)

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)


user_input = input("Vvedyt ryadok: ")

total_chars = len(user_input)

space_count = 0

for char in user_input:
    if char == " ":
        space_count += 1

print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")

k = 0
while k < 10:
    k += 1
    print(k)

a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1

while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break

for i in range(2, 10):
    print(i)

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)


list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)



numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key, val in numbers.items():
    print(key, val)


val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")

age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number")