

# Given the Clue the three dads are : Michael, Alberto, Ken
# The three kids are Stephanie, Elias, James


# Possible family members for the three dad.
Michael = ["James"]
Alberto = ["Stephanie", "Elias", "James"]
Ken = ["Elias", "James"]


names = ["Michael", "Ken", "Alberto"]


dads = [Michael, Alberto, Ken]
assigned = []


def checkDuplicates():
    for i in range(len(dads)):
        if (len(dads[i]) == 1 and dads[i][0] not in assigned):
            assigned.append(dads[i][0])
            break

    for j in range(len(dads)):
        if(len(dads[j]) > 1 and dads[i][0] in dads[j]):
            dads[j].remove(dads[i][0])


while len(assigned) < len(dads):
    checkDuplicates()


for i in range(len(dads)):
    print(f"{names[i]}'s kid is {dads[i][0]}")
