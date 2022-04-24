
def pow(x):
    return x + 2
    
def add(x, y):
    return x + y

def test_pow():
    assert pow(1) == 1
    assert pow(2) == 4
    assert pow(100) == 10000
    
def test_add():
    assert add(2, 4) == 6
    assert add(1, -4) == -3
    assert add(2, 0) == 2
