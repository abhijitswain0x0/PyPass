import secrets

import pypass.characters as chars


def generate(length=16):
    pool = chars.ALL
    return "".join(secrets.choice(secrets.choice(pool)) for _ in range(length))
