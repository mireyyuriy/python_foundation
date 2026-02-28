from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Розраховує кількість днів між заданою датою і поточною датою.

    Args:
        date (str): Рядок дати у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').

    Returns:
        int: Кількість днів від заданої дати до поточної.
             Від'ємне значення, якщо задана дата пізніша за поточну.

    Raises:
        ValueError: Якщо рядок дати має неправильний формат.
    """
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Неправильний формат дати: '{date}'. Очікується формат 'РРРР-ММ-ДД'.")

    today = datetime.today().date()
    delta = today - given_date

    return delta.days



# Приклад використання
if __name__ == "__main__":
    test_dates = ["2020-01-01", "2026-12-31", "2026-02-26", "invalid-date"]

    for d in test_dates:
        try:
            result = get_days_from_today(d)
            print(f"get_days_from_today('{d}') = {result} днів")
        except ValueError as e:
            print(f"Помилка: {e}")





#Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), 
#яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. 
#Вона буде повертати випадковий набір чисел у межах заданих параметрів, 
#причому всі випадкові числа в наборі повинні бути унікальні.

import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> list:
    random_set = {}
    if min < 1 or max > 1000:
        return []
    if min > max:
        return []
    
    available_numbers = max - min + 1
    if quantity < 1 or quantity > available_numbers:
        return []
    
    # Генерація унікальних випадкових чисел
    random_set = random.sample(range(min, max + 1), quantity)
    # Повертаємо відсортований список
    return sorted(random_set)


lottery_numbers = get_numbers_ticket(1, 49, 15)
print("Ваші лотерейні числа:", lottery_numbers)

import random

def get_numbers_ticket(min, max, quantity):
    """
    Генерує набір унікальних випадкових чисел для лотереї.
    
    Args:
        min: мінімальне число (не менше 1)
        max: максимальне число (не більше 1000)
        quantity: кількість чисел (між min і max включно)
    
    Returns:
        Відсортований список унікальних випадкових чисел або пустий список при помилці.
    """
    if min < 1 or max > 1000 or quantity < min or quantity > max or min >= max:
        return []
    
    return sorted(random.sample(range(min, max + 1), quantity))


# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


import re

def normalize_phone(phone_number: str) -> str:
    # 1. Забрати всі символи, крім цифр
    digits = re.sub(r'\D', '', phone_number)

    # 2. Якщо номер уже починається з '380' → просто додамо '+'
    if digits.find('380',0) == 0:
        return '+' + digits

    # 3. Якщо номер починається з '0' (мобільний / міський без коду країни)
    if digits.find('0',0) == 0:
        return '+38' + digits

    # 4. Якщо чомусь інший варіант (рідкі випадки) – вважаємо, що це локальний номер без 0
    #    і просто додаємо '+38' попереду.
    return '+38' + digits

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


from datetime import datetime, timedelta

def get_upcoming_birthdays(users:list) -> list:
    today = datetime.today()
    result = []

    for user in users:
        # Парсимо дату народження (рік з поля не використовуємо як поточний)
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d")
        birthday_this_year = bday.replace(year=today.year)

        # Якщо в цьому році ДН вже минув — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця в днях від сьогодні
        delta_days = (birthday_this_year - today).days

        # Цікавлять лише дні від 0 до 7 включно
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            # Якщо дата привітання припадає на вихідний (сб/нд) — переносимо на понеділок
            # weekday(): 0=Пн, ..., 5=Сб, 6=Нд [web:12]
            if congratulation_date.weekday() >= 5:
                # Додаємо 1 або 2 дні до понеділка
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days=days_to_monday)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result

users = [
    {"name": "John Doe", "birthday": "1985.02.27"},
    {"name": "Jane Smith", "birthday": "1990.02.28"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)