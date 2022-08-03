from random import randint

from data.data import Person
from faker import Faker

fake_ru = Faker('ru_Ru')

def generated_person():
    yield Person(
        first_name=fake_ru.first_name(),
        last_name=fake_ru.last_name(),
        middle_name=fake_ru.middle_name(),
        email=fake_ru.email(),
        current_address=fake_ru.address(),
        permanent_address=fake_ru.address(),
        age=randint(18, 60),
        salary=randint(10000, 60000),
        department=fake_ru.job(),
    )