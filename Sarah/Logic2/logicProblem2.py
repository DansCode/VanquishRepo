from models.container import Dogs

# names = ["Pepper", "Ginger", "Saber", "Bear", "Nutmeg"]

# pepper = ["burying"]
# ginger = ["scratch", "catch", "nap", "burying"]
# saber = ["catch", "nap", "burying"]
# bear = ["catch", "burying"]
# nutmeg = ["scratch", "walk"]

visited = []

def create_starting_dogs():
    pepper = Dogs("Pepper",  ["burying"])
    ginger = Dogs("Ginger",  ["scratch", "catch", "nap", "burying"])
    saber = Dogs("Saber",  ["catch", "nap", "burying"])
    bear = Dogs("Bear",  ["catch", "burying"])
    nutmeg = Dogs("Nutmeg",  ["scratch", "walk"])

    dogs = [pepper, ginger, saber, bear, nutmeg]
    return dogs

def removeMultipleOccurences(dogs):
    curr = ""
    for i in range(len(dogs)):
        if (len(dogs[i].activities) == 1 and dogs[i].name not in visited):
            curr = dogs[i].activities[0]
            visited.append(dogs[i].name)
            break

    for j in range(len(dogs)):
        if (len(dogs[j].activities) > 1 and curr in dogs[j].activities):
            dogs[j].activities.remove(curr)

def print_values(dogs):
    for dog in dogs:
        print(dog)

def main():
    dogs = create_starting_dogs()
    while len(visited) < len(dogs):
        removeMultipleOccurences(dogs)

    print_values(dogs)

if __name__ == '__main__':
    main()