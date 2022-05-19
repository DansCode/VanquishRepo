def filterSets(sets):
    singleElementSets = []
    for each in [x for x in sets if len(x) == 1]:
        singleElementSets.append(sets[sets.index(each)])

    for singleton in singleElementSets:
        for i in range(len(sets)):
            if len(singleton.intersection(sets[i])) == 1 and len(sets[i]) > 1:
                sets[i] = sets[i] - singleton