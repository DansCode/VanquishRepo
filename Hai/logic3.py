
# Assign height placement based on clues given.
# Example: Assume Charlotte is 0. Benito is not the smallest so we have placeholder set until clues state otherwise
# Leisha is taller than than Benito so we use whatever index Benito is currently at and increment it plus 1

Charlotte = 0
Benito = Charlotte + 1  # 1
Leisha = Benito + 1  # 2
Delia = Leisha + 1  # 3
Weldon = Delia + 1  # 4 o #3
Zina = Weldon + 1  # 5


# Set the variables in a list and sort the order
people = [Charlotte, Zina, Weldon, Delia, Leisha, Benito]

# Create a dictionary to pair their index value with the name of the individual
heightList = {
    Charlotte: "Charlotte",
    Weldon: "Weldon",
    Zina: "Zina",
    Benito: "Benito",
    Delia: "Delia",
    Leisha: "Leisha",
}

# Sort the List in numerical order to indicate shortest to Tallest
people.sort()

# Print the values associate with the integer keys
for i in people:
    print(heightList.get(i))
