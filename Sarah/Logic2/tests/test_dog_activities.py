import pytest

from models.container import Dogs
from logicProblem2 import create_starting_dogs, loop_multiple_occurences

dogs = create_starting_dogs()

def test_valid_dog():
    for dog in dogs:
        assert isinstance(dog, Dogs)

def test_valid_dog_format():
    for dog in dogs:
        assert (isinstance(dog.name, str) and isinstance(dog.activities, list))

@pytest.mark.parametrize("expected", [
    ("burying", 0),
    ("scratch", 1),
    ("nap", 2),
    ("catch", 3),
    ("walk", 4)
])
def test_valid_output(expected):
    visited = []
    different_dogs = loop_multiple_occurences(visited)
    assert (expected[0] in different_dogs[expected[1]].activities and len(different_dogs[expected[1]].activities) == 1)

def test_valid_activity_in_list():
    list_activities = ["burying", "walk", "nap", "catch", "scratch"]
    for dog in dogs:
        for act in dog.activities:
            assert act in list_activities

def test_valid_list_length():
    visited = []
    different_dogs = loop_multiple_occurences(visited)
    assert len(dogs) == len(different_dogs)

def test_valid_output_names():
    visited = []
    different_dogs = loop_multiple_occurences(visited)
    for i, dog in enumerate(different_dogs):
        assert dogs[i].name == dog.name