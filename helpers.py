import random
import string

def generate_email():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) + "@mail.ru"

def generate_invalid_email():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@"