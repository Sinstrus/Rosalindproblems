# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
probsDom = [1.0, 1.0, 1.0, 0.75, 0.5, 0]

with open("rosalind_iev.txt","r") as f:
    contents = f.read().strip().split(' ')
    data = map(int,contents)

# print data

offspring = [0] * 6
for i in range(0,len(data)):
    # print data[i]
    # print probs[i]
    offspring[i] = (2 * data[i] * probs[i])

# print offspring
print sum(offspring)
