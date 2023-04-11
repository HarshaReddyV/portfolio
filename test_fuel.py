from fuel import convert, gauge

import pytest

def test_convert():
    assert convert('3/4') == 75
    assert convert('0/100') == 0



def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(100) == 'F'
    assert gauge(75) == '75%'
    assert gauge(99) == 'F'
    assert gauge(45) =='45%'

def test_value():
    with pytest.raises(ValueError):
        convert("harsha")
        convert('1/harsha')
        convert('harsha/1')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
