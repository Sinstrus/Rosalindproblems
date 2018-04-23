# dataset text file is pair of numbers, e.g. "5 3"
#the first number is n <=40 and the second number is k <= 5
# RETURN: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation,
# every pair of reproduction-age rabbits produces a litter of k rabbit pairs
# each new pair of kittens takes a month to reach reproductive age

#if we simulate n = 0, 1, 2, 3... and P expresses the total number of rabbit pairs:
#P1 = P2 = 1
#P3 = P2 + k * P1
#P4 = P3 + k * P2 and so on...

#This is a function that can be defined recursivelyself.

n = 1
k = 1

def totalpairs(months,new_per_birth):
    if months == 1:
        num_pairs = 1
    elif months == 2:
        num_pairs = 1
    else:
        num_pairs = totalpairs(months-1,new_per_birth) + new_per_birth * totalpairs(months-2,new_per_birth)

    return num_pairs

print totalpairs(n,k)
