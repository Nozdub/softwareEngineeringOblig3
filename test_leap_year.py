from leap_year import is_leap_year


def test_check_if_year_is_divisible_by_4():
    assert bool(is_leap_year(4)) == True
    assert bool(is_leap_year(8)) == True
    assert bool(is_leap_year(16)) == True


def test_check_if_year_is_not_divisible_by_100():
    assert bool(is_leap_year(100)) == False
    assert bool(is_leap_year(300)) == False
    assert bool(is_leap_year(500)) == False


def test_check_if_year_is_divisible_by_400():
    assert bool(is_leap_year(400)) == True
    assert bool(is_leap_year(1200)) == True
    assert bool(is_leap_year(1600)) == True


def test_check_if_year_is_not_divisible_by_4000():
    assert bool(is_leap_year(4000)) == False


