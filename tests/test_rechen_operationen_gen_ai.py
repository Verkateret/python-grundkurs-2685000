# Prompteingabe: 1
# Ich habe folgende Python Funktionen:
# def erhoehe_um_zwei(zahl):
#     return zahl + 2

# def multipliziere_mit_drei(zahl):
#     return zahl * 3

# def subtrahiere_zehn(zahl):
#     return zahl - 10

# def teile_durch_vier(zahl):
#     if zahl == 0:
#         raise ZeroDivisionError("Zahl darf nicht 0 sein")
#     if zahl % 4 != 0:
#         raise ValueError("Zahl muss durch 4 teilbar sein")
#     return zahl / 4
# Erstelle mir dafür im Framework pytest jeweils 5 unit tests. Überprüfe im 
# Speziellen mögliche Fehlerfälle. Teste sowohl integer als auch float eingaben. 
# Beachte dass man float nicht direkt vergleichen kann.

import pytest

from aufgaben_package.rechen_operation import (
    erhoehe_um_zwei,
    multipliziere_mit_drei,
    subtrahiere_zehn,
    teile_durch_vier,
)


def test_erhoehe_um_zwei_mit_positivem_integer():
    assert erhoehe_um_zwei(5) == 7


def test_erhoehe_um_zwei_mit_negativem_integer():
    assert erhoehe_um_zwei(-3) == -1


def test_erhoehe_um_zwei_mit_null():
    assert erhoehe_um_zwei(0) == 2


def test_erhoehe_um_zwei_mit_float():
    assert erhoehe_um_zwei(2.5) == pytest.approx(4.5)


def test_erhoehe_um_zwei_mit_negativem_float():
    assert erhoehe_um_zwei(-1.25) == pytest.approx(0.75)


def test_multipliziere_mit_drei_mit_positivem_integer():
    assert multipliziere_mit_drei(4) == 12


def test_multipliziere_mit_drei_mit_negativem_integer():
    assert multipliziere_mit_drei(-5) == -15


def test_multipliziere_mit_drei_mit_null():
    assert multipliziere_mit_drei(0) == 0


def test_multipliziere_mit_drei_mit_float():
    assert multipliziere_mit_drei(2.5) == pytest.approx(7.5)


def test_multipliziere_mit_drei_mit_negativem_float():
    assert multipliziere_mit_drei(-1.5) == pytest.approx(-4.5)


def test_subtrahiere_zehn_mit_positivem_integer():
    assert subtrahiere_zehn(20) == 10


def test_subtrahiere_zehn_mit_negativem_integer():
    assert subtrahiere_zehn(-5) == -15


def test_subtrahiere_zehn_mit_null():
    assert subtrahiere_zehn(0) == -10


def test_subtrahiere_zehn_mit_float():
    assert subtrahiere_zehn(12.5) == pytest.approx(2.5)


def test_subtrahiere_zehn_mit_negativem_float():
    assert subtrahiere_zehn(-2.5) == pytest.approx(-12.5)


def test_teile_durch_vier_mit_positivem_integer():
    assert teile_durch_vier(8) == 2


def test_teile_durch_vier_mit_negativem_integer():
    assert teile_durch_vier(-12) == -3


def test_teile_durch_vier_mit_float():
    assert teile_durch_vier(8.0) == pytest.approx(2.0)


def test_teile_durch_vier_mit_null_wirft_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        teile_durch_vier(0)


def test_teile_durch_vier_mit_nicht_teilbarer_zahl_wirft_value_error():
    with pytest.raises(ValueError):
        teile_durch_vier(10)