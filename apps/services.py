import random
import string


def generate_code(length):
    characters = string.ascii_letters + string.digits
    invite_code = ''.join(random.choice(characters) for _ in range(length))
    return invite_code
