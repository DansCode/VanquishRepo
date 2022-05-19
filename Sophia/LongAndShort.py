hint1=["Delia","Weldon","Zina"]
hint2=["Benito","Liesha","Delia"]
hint3=["Charlotte","Benito"]

heights=hint3+hint2+hint1
noDuplicate=[]
for i in heights:
 if i not in noDuplicate:
  noDuplicate.append(i)

noDuplicate.reverse()
print(noDuplicate)
