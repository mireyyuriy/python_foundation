from faker import Faker
import json

fake = Faker("uk_UA")

def get_fake_user ():
    return {
        "name": fake.name(),
        "phone_number": fake.phone_number(),
        "email": fake.email(),
        "password": fake.password()
    }

filename = input("Enter filename >>> ")
ammount = int(input("How many users >>> "))

with open(filename, "w", encoding="utf-8") as file:
    users = []
    for _ in range(ammount):
        users.append(json.dumps(get_fake_user(), ensure_ascii=False))

    file.writelines(users)