def say_hello():
    print("Hello world")

say_hello()
say_hello()

def print_max(a: int, b: int):
    if a > b:
        print (a, "maksymalno")
    elif a == b:
        print (a, "dorivnue", b)
    else:
        print (b, "maksymalno")

print_max(3,4)

x = 5
y = 7
print_max(x,y)

def greet(name: str) -> str:
    return f"Pryvit, {name}"

greeting = greet ("Oleksiy")
print (greeting)


def is_even(num: int) -> bool:
    return num % 2 == 0

check_even = is_even(4)
print(check_even)

def modify_list(lst: list) -> list:
    lst = lst.copy()
    lst.append(4)
    return lst

my_list = [1, 2, 3]
print (modify_list(my_list))
print(my_list)  # виведе: [1, 2, 3]


def string_to_codes(string: str) -> dict:
    codes = {}
    for ch in string:
        if ch not in codes:
            codes[ch] = ord(ch)
    return codes

result = string_to_codes("Hello world!")
print(result)


def greet(name, message="Привіт"):
    print(f"{message}, {name}!")

# використовує значення за замовчуванням для message
greet("Олексій")  

# передача власного значення для message
greet("Марія", message="Добрий день")  

def say(message, times=1):
    print(message * times)

say('Привіт') 
say('Світ', 5)

def real_cost(base: int, discount: float = 0) -> float:
    return base * (1 - discount)

price_bread = 15
price_butter = 50
price_sugar = 60

current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)
print(f'Нова вартість хліба: {current_price_bread}')
print(f'Нова вартість масла: {current_price_butter}')
print(f'Нова вартість цукру: {current_price_sugar}')


def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25)


def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)

example_function(1, 2, 3, name="Alice", age=25)

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

person_info = {"name": "Alice", "age": 25}
greet(**person_info)


def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок

print(factorial(5)) # виведе 120


def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

print(fibonacci(10)) # виведе 55


def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))