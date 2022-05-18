names = ["Pepper", "Ginger", "Saber", "Bear", "Nutmeg"]

pepper = ["burying"]
ginger = ["scratch", "catch", "nap", "burying"]
saber = ["catch", "nap", "burying"]
bear = ["catch", "burying"]
nutmeg = ["scratch", "walk"]

dogs = [pepper, ginger, saber, bear, nutmeg]
visited = []

def removeMultipleOccurences():
    curr = ""
    for i in range(len(dogs)):
        if (len(dogs[i]) == 1 and dogs[i][0] not in visited):
            curr = dogs[i][0]
            visited.append(curr)
            break

    for j in range(len(dogs)):
        if (len(dogs[j]) > 1 and curr in dogs[j]):
            dogs[j].remove(curr)

while len(visited) < len(dogs):
    removeMultipleOccurences()

for i in range(len(dogs)):
    print(f"{names[i]} is {dogs[i][0]}")