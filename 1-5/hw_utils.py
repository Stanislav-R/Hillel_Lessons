import random
import string


def generate_password(length, specials, digits):
    random_base = string.ascii_lowercase + string.ascii_uppercase
    if specials:
        random_base += string.punctuation
    if digits:
        random_base += string.digits
    return ''.join(random.choices(random_base, k=length + specials + digits))
