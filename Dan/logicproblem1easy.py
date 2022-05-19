abigail = {"cook","kayak","zipline"}
oliver = {"cook","kayak"}
rosa = {"zipline","rockclimb"}
blake = {"cook"}

people = [abigail,oliver,rosa,blake]

def filterSets(sets):
    singleElementSets = []
    singleElementSets.append(sets[sets.index([x for x in sets if len(x) == 1][0])])

    for singleton in singleElementSets:
        for i in range(len(sets)):
            if len(singleton.intersection(sets[i])) == 1 and len(sets[i]) > 1:
                sets[i] = sets[i] - singleton


while max([len(x) for x in people]) != 1:
    filterSets(people)

print(f"abigail: {people[0]}\noliver: {people[1]}\nrosa: {people[2]}\nblake: {people[3]}")
