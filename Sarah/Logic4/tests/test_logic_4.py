from typing import List
import pytest

from models.container import Father, Graduate
from logicProblem4 import create_fathers, create_graduates, create_info_cases, decide_father_graduates

fathers = create_fathers()
graduates = create_graduates()
info_cases = create_info_cases()

def test_create_father_method_type():
    for father in fathers:
        assert isinstance(father, Father)

def test_create_father_method_attribute():
    for father in fathers:
        assert isinstance(father.name, str)

def test_create_graduate_method_type():
    for graduate in graduates:
        assert isinstance(graduate, Graduate)    
        
def test_create_graduate_method_attribute():
    for graduate in graduates:
        assert isinstance(graduate.name, str)

def test_create_info_case_method_type():
    for info_case in info_cases:
        assert isinstance(info_case, list)    
        
def test_create_info_case_method_sub_list_type():
    for info_case in info_cases:
        for val in info_case:
            assert isinstance(val, bool) 

#need to run pytest --capture=fd ?
def test_decide_father_graduates_function(capfd):
    decide_father_graduates(info_cases, graduates, fathers)
    out, err = capfd.readouterr()
    assert out == """Micheal is the father of James

Alberto is the father of Elias

Ken is the father of Stephanie

"""
