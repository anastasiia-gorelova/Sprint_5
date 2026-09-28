import random


def generate_email():
    return f"user{random.randint(1000, 9999)}@test.ru"

def generate_password():
    return str(random.randint(100000, 999999))

def generate_invalid_email():
    return f"user{random.randint(1000, 9999)}"

def generate_advertisement_title():
    return f"Test advertisement {random.randint(1000, 9999)}"

EXISTING_USER_EMAIL = "qa_existing_user38@gmail.com"
EXISTING_USER_PASSWORD = "existing_user38_password"

ADVERTISEMENT_DESCRIPTION = "Test description"
ADVERTISEMENT_PRICE = "1000"