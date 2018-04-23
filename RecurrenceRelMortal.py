#Below is a solution I found online. And it does indeed work.
#"My idea is to keep track of the population of every generation in a list and
#update it through each month. The number of rabbits will be then the sum of this list."

# def fib(month, age):
# 	generation = [0]*age
# 	generation[0], generation[1] = 0,1
# 	for x in range(2,month):
# 		temp = list(generation)
# 		generation[0] = sum(generation[1:]) #number of new born
#
#
# 		for i in range(1,age):
# 			generation[i] = temp[i-1]
# 	return sum(generation)
#
# Y = fib(80,18)
# print Y

# age = 18
# generation = [0]*age
# print generation
# temp = list(generation)
# print temp

month = 83
age = 16

list_of_generations = [0] * age
list_of_generations[0] = 1
print sum(list_of_generations)
list_of_generations[0], list_of_generations[1] = 0,1 #the rest are 0
print sum(list_of_generations)

#we are currently at month 1. On to month 2.

for x in range(2,month):

    old = list(list_of_generations) #make a temp copy of list_of_generations.
    #you must use list() because if list_of_generations is changed, that will automatically also
    #update old to the new form of list_of_generations

    list_of_generations[0] = sum(list_of_generations[1:]) #sum all indices except 0 into the 0 index
    #remember this does not alter any of the other indices
    #this represents all currently alive rabbit pairs (of all ages > 1) producing a newborn rabbit pair

    for i in range(1,age):
        #now we need to move all rabbit pairs up in age by 1
        list_of_generations[i] = old[i-1]

    # print sum(list_of_generations)

print sum(list_of_generations)
