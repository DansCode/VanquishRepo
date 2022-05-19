
grads=["Stephanie","James","Elias"]

dads=["Ken","Alberto","Michael"]

def merge(grads,dads):
 answer=[]
 for y in range(len(grads)):
     a=grads[y]
     b=dads[y]
     temp=[a,b]
     answer.append(temp)
 return answer
     
print(merge(grads,dads))
