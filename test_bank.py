from bank import value

def test_hello():
    assert value('hello') == 0

def test_upper():
    assert value('HELLO') == 0

def test_hi():
    assert value('hi') == 20

def test_mate():
    assert value('mate') == 100