import pytest

from models.container import Dogs
from Logic2 import create_default

dogs = create_default  # create new dog objects


def test_valid_default_dogs():
    for dog in dogs:
        for item in dog:
            assert isinstance(item, bool)


def test_valid_generated_dogs():
    for dog in dogs:
        assert isinstance(dogs, Dogs)
