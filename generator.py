from generator import generate_name

def test_generate_name_returns_string():
    name = generate_name()
    assert isinstance(name, str)
    assert len(name) > 0