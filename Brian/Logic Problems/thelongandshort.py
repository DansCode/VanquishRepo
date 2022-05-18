#Six children, need to determine the tallest and shortest Leisha, Benito, Delia, Charlotte, Weldon and Zina


children = ["Leisha", "Benito", "Delia", "Charlotte", "Weldon", "Zina"]
#Weldon > Delia but < Zina
#Leisha > Benito but < Delia and Weldon
#Benito is NOT the shortest
heightlist = [3, 1, 0, 2, 4, 5]
children = [children[i] for i in heightlist]

print("From shortest to tallest")
print(children)