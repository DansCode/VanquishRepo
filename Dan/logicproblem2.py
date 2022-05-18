Pepper = {"burying"}
Ginger = {"scratch", "catch", "nap", "burying"}
Saber = {"catch", "nap", "burying"}
Bear = {"catch", "burying"}
Nutmeg = {"scratch", "walk"}

dogs = [Pepper, Ginger, Saber, Bear, Nutmeg]

length1dogs = []
def refactorAll():
    for i in range(len(dogs)):
        if len(dogs[i]) == 1 and dogs[i] not in length1dogs:
            length1dogs.append(dogs[i])

    for i in range(len(length1dogs)):
        for y in range(len(dogs)):
            if dogs[y] not in length1dogs:
                dogs[y] = dogs[y] - length1dogs[i]
    
    
maxlength = max([len(i) for i in dogs])
while maxlength != 1:
    refactorAll()
    maxlength = max([len(i) for i in dogs])

print("Pepper: {},\nGinger: {},\nSaber: {},\nBear: {},\nNutmeg: {}"
.format(dogs[0],dogs[1],dogs[2],dogs[3],dogs[4]))