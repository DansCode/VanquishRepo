from models.container import Father, Graduate

def create_fathers():
    micheal = Father("Micheal")
    alberto = Father("Alberto")
    ken = Father("Ken")

    fathers = [micheal, alberto, ken]
    return fathers

def create_graduates():
    stephanie = Graduate("Stephanie")
    elias = Graduate("Elias")
    james = Graduate("James")

    graduates = [stephanie, elias, james]
    return graduates

# base case for each parent
# what we know which one could (not) be the parent
# order of [stephanie, elias, james]
def create_info_cases():
    m = [False, False, True]
    a = [False, True, True]
    k = [True, True, False]

    condensed = [m,a,k]
    return condensed

def decide_father_graduates(info_case, graduates, fathers):
    for i in range(len(info_case)):
        if (info_case[i].count(True) > 1):
            for j in range(len(info_case[i])):
                initial = info_case[i][j]
                info_case[i][j] = not info_case[i][j]
                if (info_case[i].count(True) < 2):
                    print(f"{fathers[i]} is the father of {graduates[j]}\n")
                    info_case[i][j] = initial
                    break
                info_case[i][j] = initial
        else:
            print(f"{fathers[i]} is the father of {graduates[info_case[i].index(True)]}\n")


def main():
    graduates = create_graduates()
    fathers = create_fathers()

    info_cases = create_info_cases()

    decide_father_graduates(info_cases, graduates, fathers)

if __name__ == '__main__':
    main()

