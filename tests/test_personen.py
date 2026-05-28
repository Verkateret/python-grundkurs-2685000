import pytest
from aufgaben_package.personen import Person

def test_person_init():
    person = Person("Alice", 25)
    assert person.name == "Alice"
    assert person.alter == 25

def test_person_str():
    string = str(Person("Bob", 38))
    assert string == "Bob (38)"
