from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        name=faker_ru.first_name(),
        email=faker_ru.email(),
        password=faker_ru.password()
    )