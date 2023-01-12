import pytest
from app import bubble_sort

testdata = [([3, 4, 5, 2, 1], [1, 2, 3, 4, 5])]

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_bubble_sort(sample, expected_output):
    sorted = bubble_sort(sample)

    assert bubble_sort(sample) == expected_output