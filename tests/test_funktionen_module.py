import pytest

from genai_beispiele.funktionen_module import ping_pong, listen_invertieren, hoechster_wert_unabhaengig_vom_vorzeichen

def test_ping():
	assert ping_pong(3) == "Ping"
	assert ping_pong(6) == "Ping"
	assert ping_pong(9) == "Ping"


def test_pong():
	assert ping_pong(5) == "Pong"
	assert ping_pong(10) == "Pong"
	assert ping_pong(20) == "Pong"


def test_ping_pong():
	assert ping_pong(15) == "Ping Pong"
	assert ping_pong(30) == "Ping Pong"
	assert ping_pong(45) == "Ping Pong"


def test_number():
	assert ping_pong(1) == 1
	assert ping_pong(2) == 2
	assert ping_pong(4) == 4


def test_listen_invertieren():
	assert listen_invertieren([1, 2, 3]) == [3, 2, 1]
	assert listen_invertieren([]) == []
	assert listen_invertieren([42]) == [42]


def test_hoechster_wert_unabhaengig_vom_vorzeichen():
	# erwartet wird der höchste Betrag als positiver Wert
	assert hoechster_wert_unabhaengig_vom_vorzeichen([-5, 3]) == 5
	assert hoechster_wert_unabhaengig_vom_vorzeichen([-2, -8]) == 8
	assert hoechster_wert_unabhaengig_vom_vorzeichen([0, -1]) == 1
	assert hoechster_wert_unabhaengig_vom_vorzeichen([5, -7, 6]) == 7
