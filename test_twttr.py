from twttr import shorten

def test_twttr():
    assert shorten('twitter') == 'twttr'
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TWI'TTER'") == "TW'TTR'"
    assert shorten('TWITTER55,15') == 'TWTTR55,15'

