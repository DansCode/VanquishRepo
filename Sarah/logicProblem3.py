#list ordered from ascending height
#assume charlotte is shortest

from collections import deque

heightList = deque(['Charlotte'])

#ordered given information
dict1 = {"Delia": 0, "Weldon": 1, "Zina": 2}
dict2 = {"Benito": 0, "Leisha": 1, "Delia": 2, "Weldon": 2}

dictC = [dict2, dict1]

timesAdded = 0

#merge repeating values
reduced = dict()
for val in dictC:
    for key in val:
        if key in reduced:
            reduced[key] += val[key]
            timesAdded += 1
        else:
            reduced[key] = val[key]

#update last key to reflect how many times there was an intersection
updated = dict()
for key in reduced:
    if key is not list(reduced)[-1]:
        updated[key] = reduced[key]
    else:
        updated[key] = reduced[key] + timesAdded

#append to final list
for key in updated:
    heightList.append(key)

print("From shortest to tallest:\n" + str(heightList))