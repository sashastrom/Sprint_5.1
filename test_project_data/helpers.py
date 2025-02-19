import random
import string

def generate_random_email():
    random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_email}@yandextests.ru"
