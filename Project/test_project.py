from project import get_Date
import datetime
import pytest

def test_get_date():
    assert get_Date('12-12-2023') == datetime.date(2023, 12, 12)
    with pytest.raises(SystemExit):
        assert get_Date('Cat') == SystemExit
        assert get_Date('12-12-2012') == SystemExit
        assert get_Date('12:12:2012') == SystemExit
        assert get_Date('29-02-2011') == SystemExit
        assert get_Date('28-02-2024') == SystemExit




