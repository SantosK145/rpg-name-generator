import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generator import generate_name


def test_generate_name_returns_string():
    name = generate_name()
    assert isinstance(name, str)
    assert len(name) > 0