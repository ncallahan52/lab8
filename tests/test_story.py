from adventure.story import intro
import pytest

@pytest.mark.parametrize(
    # fmt: off
    "input_str, expected_output",
    [
        ('Right', 'right'),
        ('right', 'right'),
        ('RIGHT',  'right'),
        ('Left', 'left'),
        ('left', 'left'),
        ('LEFT',  'left'),
    ],
    # fmt: on
)
def test_intro(input_str, expected_output):
    result = intro(input_str)
    assert expected_output in result.lower()