
Pepper = {"burying"}
Ginger = {"scratch", "catch", "nap", "burying"}
Saber = {"catch", "nap", "burying"}
Bear = {"catch", "burying"}
Nutmeg = {"scratch", "walk"}

dogs = [Pepper, Ginger, Saber, Bear, Nutmeg]
length1dogs = []

def refactorAll():
    for dog in dogs:
        if len(dog) == 1 and dog not in length1dogs:
            length1dogs.append(dog)
    
    for dog in length1dogs:
        for i in range(len(dogs)):
            if dogs[i] is not dog:
                dogs[i] = dogs[i].difference(dog)
    
maxlength = max([len(i) for i in dogs])

while maxlength != 1:
    refactorAll()
    maxlength = max([len(i) for i in dogs])

print(dogs)
print(length1dogs)
#this works but doesn't keep track of the dog names...
#could be updated to add some dict with dog names