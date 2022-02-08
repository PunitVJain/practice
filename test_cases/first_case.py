#  python code to test the code.

def add(num_one, num_two):
    return num_one + num_two

def test_add():
    assert add(3, 5) == 8

print(test_add())