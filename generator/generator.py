from data.data import Person
from faker import Faker

fake_ru = Faker('ru_Ru')

def generated_person():
    yield Person(
        full_name=fake_ru.first_name() + " " + fake_ru.last_name() + " " + fake_ru.middle_name(),
        email=fake_ru.email(),
        current_address=fake_ru.address(),
        permanent_address=fake_ru.address()
    )