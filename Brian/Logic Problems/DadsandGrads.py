#Michael, Ken, James, Alberto, Elias and Stephanie
#3 are High school grads and 3 are dads
#Match grads with their dads based on the following:
#Clue 1: Stephanie went to senior prom with Michael's son
#Clue 2: Elias and James play baseball. One of them is Alberto's son
#Clue 3: Michael and Elias are not related




daughters = "Stephanie" #Stephanie is a female so is a daughter
sons = ["Elias", "James"] #Elias and James play baseball so are sons
grads = [daughters, sons] #Stephanie went to prom and Elias and James played baseball so all are grads
dads = ["Michael", "Alberto", "Ken"] #Michael and Alberto are listed as having sons and due to the above Ken is the last possible dad

print("Dads and Grads are:")
dads_grads = {
    dads[2]: daughters, #Ken and Stepahnie are related because of clue 1 and clue 3
    dads[0]: sons[1],   #Michael and James are related because of clue 1 and clue 3
    dads[1]: sons[0]    #Elias and Alberto are related because of clue 2 and 3
}

print(dads_grads)
