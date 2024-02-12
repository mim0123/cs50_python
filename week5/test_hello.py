from hello import hello 

def test_default():
    hello("David") == "hello, David"


def test_argument():
    assert hello() == "hello, world"