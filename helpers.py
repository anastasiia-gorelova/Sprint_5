
import random


def generate_email():
    return f"user{random.randint(1000, 9999)}@test.ru"


def generate_password():
    return str(random.randint(100000, 999999))


def generate_invalid_email():
    return f"user{random.randint(1000, 9999)}"


def generate_advertisement_title():
    return f"Test advertisement {random.randint(1000, 9999)}"
