fathers = ["Micheal", "Alberto", "Ken"]
graduates = ["Stephanie", "Elias", "James"]

# base case for each parent
# what we know which one could (not) be the parent
# order of [stephanie, elias, james]
m = [False, False, True]
a = [False, True, True]
k = [True, True, False]

condensed = [m,a,k]

for i in range(len(condensed)):
    if (condensed[i].count(True) > 1):
        for j in range(len(condensed[i])):
            initial = condensed[i][j]
            condensed[i][j] = not condensed[i][j]
            if (condensed[i].count(True) < 2):
                print(f"{fathers[i]} is a potential parent of {graduates[j]}\n")
                condensed[i][j] = initial
                break
            condensed[i][j] = initial
    else:
        print(f"{fathers[i]} is a potential parent of {graduates[condensed[i].index(True)]}\n")

#logic works but printed condensed list doesn't correspond to the logic -> will fix later