from models.container import Dogs

# Dogs: Pepper, Ginger, Saber, Bear, Nutmeg
# Activity: Burying, Scratching, Catching. Napping, Walking
# Clues provide the following available activities to the dogs

# pepper = ["burying"]
# ginger = ["scratch", "catch", "nap", "burying"]
# saber = ["catch", "nap", "burying"]
# bear = ["catch", "burying"]
# nutmeg = ["scratch", "walk"]

# Only one activity can be assigned to an individual.

# Dog Class def __init__(self, name, activities):


def create_default():
    # function will create the following dogs

    pepper = Dogs("Pepper", ["burying"])
    ginger = Dogs("Pepper", ["scratch", "catch", "nap", "burying"])
    saber = Dogs("Pepper", ["catch", "nap", "burying"])
    bear = Dogs("Pepper", ["catch", "burying"])
    nutmeg = Dogs("Pepper", ["scratch", "walk"])

    # create dictionary with the following objects

    dogs = [pepper, ginger, saber, bear, nutmeg]


def checkDuplicates():
    for i in range(len(dogs)):
        if (len(dogs[i]) == 1 and dogs[i][0] not in assigned):
            assigned.append(dogs[i][0])
            break

    for j in range(len(dogs)):
        if (len(dogs[j]) > 1 and dogs[i][0] in dogs[j]):
            dogs[j].remove(dogs[i][0])


# recursive function to continue removing the activity until all activities are assigned for.
while len(assigned) < len(dogs):
    checkDuplicates()


for i in range(len(dogs)):
    print(f"{names[i]} is {dogs[i][0]}")
