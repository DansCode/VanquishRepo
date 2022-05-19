from librarymodule import filterSets
Michael = {"James"}
Ken = {"Stephanie", "Elias", "James"}
Alberto = {"Elias", "James"}
dads = [Michael,Ken,Alberto]
while max([len(x) for x in dads]) != 1:
    filterSets(dads)
print(f"michael: {dads[0]}\nken: {dads[1]}\nalberto: {dads[2]}")