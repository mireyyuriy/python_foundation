text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']


list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'


clean = '   spacious   '.strip()
print(clean) # spacious

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) 


print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook
print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))


url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)


url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)


width = 5
for num in range(12):
    print(f'{num:^20} {num**2:^10} {num**3:^10}')


import re

text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)

if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено.")


import re

text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Знайдено:", match.group())


import re

text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print("Електронна адреса:", match.group())

