import pypass.characters as chars
from pypass.generator import generate


def _allowed():
    return set("".join("".join(group) for group in chars.ALL))


def test_generate_respects_length_and_charset():
    allowed = _allowed()
    for length in (1, 8, 16, 64):
        password = generate(length)
        assert len(password) == length
        assert set(password) <= allowed


def test_generate_default_length():
    assert len(generate()) == 16
