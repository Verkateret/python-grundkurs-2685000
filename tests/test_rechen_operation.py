import pytest
from aufgaben_package.rechen_operation import erhoehe_um_zwei, multipliziere_mit_drei, subtrahiere_zehn, teile_durch_vier

def test_erhoehe_um_zwei_positive():
    assert erhoehe_um_zwei(3) == 5

def test_erhoehe_um_zwei_negative():
    assert erhoehe_um_zwei(-1) == 1
    assert erhoehe_um_zwei(-5) == -3

def test_multipliziere_mit_drei_positive():
    assert multipliziere_mit_drei(2) == 6
    assert multipliziere_mit_drei(5) == 15

def test_multipliziere_mit_drei_negative():
    assert multipliziere_mit_drei(-2) == -6
    assert multipliziere_mit_drei(-3) == -9

def test_subtrahiere_zehn_positive():
    assert subtrahiere_zehn(15) == 5
    assert subtrahiere_zehn(4) == -6

def test_subtrahiere_zehn_negative():
    assert subtrahiere_zehn(-5) == -15
    assert subtrahiere_zehn(-1) == -11

def test_teile_durch_vier_positive():
    assert teile_durch_vier(12) == 3
    assert teile_durch_vier(36) == 9

def test_teile_durch_vier_negative():
    assert teile_durch_vier(-8) == -2

def test_teile_durch_vier_not_divisible():
    with pytest.raises(ValueError):
        teile_durch_vier(5)
