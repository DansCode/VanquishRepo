
from models.container import Child


#order of attributes: name, ground, high, harness, water, rockwall
#numbers: 0, 1 -> false, true respectively

#Given the information we know we make a collection based on that knowledge
def create_children():
    a = Child("Abigail", {"ground": False, "high": True, "harness":False, "water": True, "rockwall": False})
    o = Child("Oliver", {"ground": True,"high": False, "harness": False, "water": True, "rockwall": False})
    r = Child("Rosa", {"ground": False,"high": True, "harness": True, "water": False, "rockwall": True})
    b = Child("Blake", {"ground": True,"high": False, "harness": False, "water": False, "rockwall": False})

    children = (a, o, r, b)
    return children

def create_check_cases():
    case_1 = ["high", True, "rockwall", False, "ziplining"]
    case_2 = ["ground", True, "water", False, "cooking"]
    case_3 = ["high", False, "water", True, "kayaking"]
    case_4 = ["high", True, "harness", True, "rock climbing"]

    cases = [case_1, case_2, case_3, case_4]
    return cases

def run_checks(children, check_case, results):

    # item refer to the elements in the subarray which is the "function"
    #                   iter over sublists      iter over items in sublist
    flat_results = [item for sublist in results for item in sublist]

    for i, child in enumerate(children):
        if (child.activities[check_case[0]] == check_case[1] and child.activities[check_case[2]] == check_case[3] and child.name not in flat_results):
            return [child.name, check_case[4]]
        elif (i == len(children)-1):
            return [child.name, "not available"]

def run_cases(children, check_cases):

    results = list()

    for i in range(len(check_cases)):
        results.append(run_checks(children, check_cases[i], results))

    return results

def print_activities(results):
    for result in results:
        print(result)

def main():
    children = create_children()
    check_cases = create_check_cases()

    results = run_cases(children, check_cases)

    print_activities(results)

if __name__ == '__main__':
    main()