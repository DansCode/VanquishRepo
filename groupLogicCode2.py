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
        for otherdog in dogs:
            if otherdog is not dog:
                otherdog = otherdog.difference(dog)
                print(otherdog)
    
maxlength = max([len(i) for i in dogs])

while maxlength != 1:
    refactorAll()
    maxlength = max([len(i) for i in dogs])

print(dogs)
print("this ran")