import pytest
from src.multiply import multiply


test_data = [ # input array, expected result
    ([], 1),
    ([2], 2),
    ([3,2], 6),
    ([2,2,2,2,2, 2,2,2,2,2], 1024),
    (["hello", 2, 2], "hellohellohellohello",)
    ]


@pytest.mark.parametrize("input,expected", test_data)
def test_muliply_happy_path(input, expected): 
    # When
    actual = multiply(*input)
    # Then
    assert expected == actual  

def test_multiply_floats():
    # Given
    inputs = [1.1, 1.1]
    # When
    actual = multiply(*inputs)
    # Then
    assert pytest.approx(actual) == 1.21

def test_multiplying_string_to_float():
    # Given 
    input = ["hello", 1.1, "world"]
    # Then
    with pytest.raises(TypeError, match="Innapropiate multiplicand types."):
        # When
        actual = multiply(*input)
