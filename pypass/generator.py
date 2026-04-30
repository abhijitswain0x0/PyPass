import random
import pypass.characters as chars


def generate(length=16):
    pool = chars.ALL
    return "".join(random.choice(random.choice(pool)) for _ in range(length))