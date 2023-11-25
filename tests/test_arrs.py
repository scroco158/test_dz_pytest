from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], -100, 100) == []
    assert arrs.my_slice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],None, -7) == [0, 1, 2]
