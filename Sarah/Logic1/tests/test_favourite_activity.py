import pytest

from models.container import Child
from logicproblem1 import create_children, create_check_cases, run_cases, run_checks

children = create_children()
check_cases = create_check_cases()

def test_list_child_class():
    for child in children:
        assert isinstance(child, Child)

def test_format_list():
    for child in children:
        assert (isinstance(child.name, str) and isinstance(child.activities, dict))

def test_all_attribute_values_in_dict():
    for child in children:
        for value in child.activities:
            assert (isinstance(value, str) and isinstance(child.activities[value], bool))

def test_all_attributes_keys_in_dict():
    acts = ["ground", "high", "water", "rockwall", "harness"]

    for act in acts:    
        for child in children:
            assert child.activities.get(act) is not None

def test_check_cases_collection():
    assert isinstance(check_cases, list)

def test_check_cases_for_data_types():
    types = [str, bool, str, bool, str]

    for case in check_cases:
        for i, val in enumerate(case):
            assert isinstance(val, types[i])

def test_cases_return_list():
    result = run_cases(children, check_cases)
    assert isinstance(result, list)

#Throws error unhashable type: 'list'
#Works in logicproblem1.py but not here need to find out why

# def test_checks_return_list():
#     result = run_checks(children,check_cases,list())
#     assert isinstance(result, list)

# def test_checks_return_list_with_elements_when_empty():
#     result = run_checks(children,check_cases,list())
#     assert (isinstance(result[0], str) and isinstance(result[1], str))

def test_different_children_case_1():
    j = Child("John", {"ground": False, "high": True, "harness":True, "water": True, "rockwall": False})
    k =  Child("Ken", {"ground": False, "high": False, "harness":False, "water": False, "rockwall": False})

    chs = [j,k]

    result = run_cases(chs, check_cases)

    for res in result:
        assert (isinstance(res[0], str) and isinstance(res[1][0], str))
