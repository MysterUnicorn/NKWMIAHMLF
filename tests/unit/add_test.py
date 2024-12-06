import pytest
from src.add import add


test_data = [ # input array, expected result
    ([], 0),
    ([1], 1),
    ([1,2], 3),
    ([1,1,1,1,1,1,1,1], 8),
    ([1.1,1.1], 2.2),
    (["hello", " ", "world"], "hello world",)
    ]


@pytest.mark.parametrize("input,expected", test_data)
def test_add_happy_path(input, expected): 
    # When
    actual = add(*input)
    # Then
    assert expected == actual  

def test_adding_string_to_number():
    # Given 
    input = ["hello", 1, "world"]
    # Then
    with pytest.raises(TypeError, match="Innapropiate addand types."):
        # When
        actual = add(*input)
