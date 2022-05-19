clue1 = ["delia", "weldon", "zina"]
clue2 = ["benito","leisha", "delia", "weldon"]
clue3 = ["*","benito"]

people = ["leisha", "benito", "delia", "charlotte", "weldon", "zina"]
metaclue = [clue3,clue2,clue1]

compiledClue = []

for i in range(len(metaclue)-1):
    intersection = set(metaclue[i]).intersection(set(metaclue[i+1]))
    
    for each in metaclue[i]:
        if each not in compiledClue:
            compiledClue.append(each)
    for each in metaclue[i+1]:
        if each not in intersection and each not in compiledClue:
            compiledClue.append(each)
    

for person in people:
    if person not in compiledClue:
        compiledClue[compiledClue.index("*")] = person


print(compiledClue)
    