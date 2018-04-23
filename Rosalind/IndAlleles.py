import math


def bernoulli(n,k,p):
    """gives the probability that EXACTLY k successes will occur
    given n events, each having a probability of success p"""
    return ( math.factorial(n)/(math.factorial(k) * math.factorial(n-k)) ) * (p**k) * (1-p)**(n-k)

k = 6 #generation number. Total individuals = 2**k
n = 16 #check probability that AT LEAST n AaBb organisms belong to generation k
#probability that any given individual will be AaBb in any generation will be 0.5 * 0.5 = 0.25
#I don't completely understand why that probability doesn't change between generations, but it intuitively makes some sense

def Tomcheck(total,at_least_n):

    probs = 1 - sum(bernoulli(total,k,0.25) for k in range(0,at_least_n))
    return probs

print Tomcheck(2**k,n)
