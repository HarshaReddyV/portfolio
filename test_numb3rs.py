from numb3rs import validate

def test_validate():
    assert validate('cat') == False
    assert validate('127.127.1.1') == True
    assert validate('1.1.1.1') == True
    assert validate('1') == False
    assert validate('543.1.1.1') == False