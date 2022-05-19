def filterSets(sets):
    singleElementSets = []
    singleElementSets.append(sets[sets.index([x for x in sets if len(x) == 1][0])])

    for singleton in singleElementSets:
        for i in range(len(sets)):
            if len(singleton.intersection(sets[i])) == 1 and len(sets[i]) > 1:
                sets[i] = sets[i] - singleton