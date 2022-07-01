import random

from data.data import Person, Password
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        name=faker_ru.first_name(),
        email=faker_ru.email()
    )

def generated_password():
    yield Password(
        password=''.join((random.choice('12345abcdxyzpqr') for i in range(5)))
    )


