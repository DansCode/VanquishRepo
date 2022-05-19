import pytest

from models.container import Dogs
from logicProblem2 import create_starting_dogs

dogs = create_starting_dogs()

def test_valid_dog():
    for dog in dogs:
        assert isinstance(dog, Dogs)