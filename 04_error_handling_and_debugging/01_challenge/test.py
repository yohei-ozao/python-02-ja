from mystery_function import mystery_function

def test_mystery_function():
    assert mystery_function([1, 2, 3, 4, 5]) == [1, 4, 3, 16, 5]
    assert mystery_function([10, 21, 32, 43, 54]) == [100, 21, 1024, 43, 2916]
    assert mystery_function([]) == []
    assert mystery_function([1, 3, 5]) == [1, 3, 5]
    print("All tests passed!")

test_mystery_function()
