import datetime
import random
import string
from faker import Faker


def generate_password(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def get_current_time():
    return datetime.datetime.now()


def generate_students(counter):
    faker = Faker()
    return [faker.name() for _ in range(counter)]