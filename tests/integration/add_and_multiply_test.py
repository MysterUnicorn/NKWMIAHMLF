from src.add import add
from src.multiply import multiply

def test_added_strings_multiplied_by_numbers():
    # Given
    strings = ["hello", " ", "world"]
    numbers = [2,3]
    # When
    actual = multiply(add(*strings), *numbers)
    # Then
    assert actual == "hello world" * 6
    