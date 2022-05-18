#order of attributes: name, ground, high, harness, water, rockwall
#numbers: 0, 1 -> false, true respectively

#Given the information we know we make a collection based on that knowledge
children = (("Abigail",1,1,1,1,0), ("Oliver",1,0,0,1,0), ("Rosa",0,1,1,0,1), ("Blake",1,0,0,0,0))

#could also store boolean type True False
#implement using dictionary?

for i in range(len(children)):
    #for ziplining
    #if high true and rockwall false then ziplining
    if (children[i][2] == 1 and children[i][5] == 0):
        print(f"{children[i][0]} likes ziplining")
        continue
    #for cooking
    #if ground true and water false cooking
    elif (children[i][1] == 1 and children[i][4] == 0):
        print(f"{children[i][0]} likes cooking")
        continue
    #for kayaking
    #if high false and water true like kayaking
    elif (children[i][2] == 0 and children[i][4] == 1):
        print(f"{children[i][0]} likes kayaking")
        continue
    #for rock climbing
    #if high true and rockwall true like rock climbing
    elif (children[i][2] == 1 and children[i][5] == 1):
        print(f"{children[i][0]} likes rock climbing")
        continue

   