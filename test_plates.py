from plates import is_valid

def test_cap():
    assert is_valid('HR0551') == False
    assert is_valid('HR1551') == True
    assert is_valid('VR7689') == True
    assert is_valid('HARSHA') == True
    assert is_valid('CATER') == True
    assert is_valid('CHLOE') == True



def test_low():
    assert is_valid('hr5515') == True
    assert is_valid('harsha') == True
    assert is_valid('h') == False

def test_num():
    assert is_valid('2655152') == False
    assert is_valid('1867299') == False
    assert is_valid('26haHa') == False
    assert is_valid('2656ha') == False
    assert is_valid('Hr0552') == False
    assert is_valid('Hr055H') == False
    assert is_valid('Hr155H') == False
    assert is_valid('$$155H') == False
    assert is_valid('@@155H') == False
    assert is_valid('2') == False

def test_alpha():
    assert is_valid('harsha') == True
    assert is_valid('23hars') == False
    assert is_valid('23') == False
    assert is_valid('Ha') == True
    assert is_valid('_HA') == False
    assert is_valid('_2r') == False
    assert is_valid('HA') == True
    assert is_valid('33') == False
    assert is_valid("AA") == True
    assert is_valid("Bt") == True
    assert is_valid("tt") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("TEEKAY") == True
    assert is_valid("CS50") == True
    assert is_valid("B2MEN") == False
    assert is_valid("2GREAT") == False


