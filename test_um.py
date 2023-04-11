from um import count

def test_count():
    assert count('um i am um harsha') == 2
    assert count('um i am um harsha and i have umbrella') == 2
    assert count('UM UMbrella um') == 2
    assert count('um, hummer is a um nice car') == 2
