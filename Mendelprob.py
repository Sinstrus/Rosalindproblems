# k + m + n represents a population of an organism
# k = number of homozygous dominant individuals
# m = number of heterozygous individuals
# n = number of homozygous recessive individuals
# sample set given in a text file, e.g. "2 2 2" => k = 2, m = 2, n = 2
#
# Return: The probability that two randomly selected mating organisms will produce
# an individual possessing a dominant allele (and thus displaying the dominant phenotype).
# Assume that any two organisms can mate.
# The question can also be framed as calculating 1.0 - X where X is the probability that two randomly chosen
# individuals will produce a homozygous recessive individual
# POSSIBILITY SPACE
# P(choosing n first) = n/(k+m+n)
# P(choosing n second) = (n-1)/(k+m+n-1)
# P(n/n produce HR individual) = 1.0

# P(choosing n first) = n/(k+m+n)
# P(choosing m second) = m/(k+m+n-1)
# P(n/m produce HR individual) = 0.5

# P(choosing m first) = m/(k+m+n)
# P(choosing n second) = n/(k+m+n-1)
# P(m/n produce HR individual) = 0.5

# P(choosing m first) = m/(k+m+n)
# P(choosing m second) = (m-1)/(k+m+n-1)
# P(m/n produce HR individual) = 0.25

#We can disregard all cases where any k individuals are chosen, as these will never produce HR individuals

#Therefore, in the first case: [n/(k + m + n)] * [(n-1)/(k + m + n - 1)] * 1.0 .... calculated on paper...

# (n*(n-1) + (m*n) + 0.25*m*(m-1))/((k+m+n)*(k+m+n-1)) is the P that randomly chosen
# pair will give a homozygous recessive individual. Therefore to get prob of an individual offspring
# with dominant trait, we subtract this result from 1.0

k = 0
m = 1
n = 1

probDom = 1.0 - ((n*(n-1) + (m*n) + 0.25*m*(m-1))/((k+m+n)*(k+m+n-1)))

print probDom
