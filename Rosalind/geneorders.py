import itertools
import math

N = 6

l = list(range(1,N+1))

A = list(itertools.permutations(l))

# print A
P = str(math.factorial(len(l)))
A = '\n'.join(str(tup).replace(",","").replace("(","").replace(")","") for tup in A)

with open("output.txt","w") as f:
    f.write(P + "\n" + A)
