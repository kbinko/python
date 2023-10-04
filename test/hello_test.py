from hello import hello

def test_default():
    assert hello() == "Hello, World"

def test_argument():    
    assert hello("David") == "Hello, David"
    
def test_loop():
    for name in ["David", "Sarah", "John"]:
        assert hello(name) == f"Hello, {name}"
    
    
    
    