from re import finditer
from re import search
from re import match
from sys import argv
from urllib import urlopen

uniprot = "http://www.uniprot.org/uniprot/%s.fasta"
#
# for protein in open('mprt.txt', 'r').read().strip().splitlines():
#
#     # Fetch the protein's fasta file and get rid of newlines.'
#     f = urlopen(uniprot % protein).read().decode('utf-8')
#     f = ''.join(f.splitlines()[1:])
#
#     # Find all the positions of the N-glycosylation motif.
#     locs = [g.start()+1 for g in finditer(r'(?=N[^P][ST][^P])', f)]
#
#     # Print them out, if any.
#     if locs != []:
#         print(protein)
#         print(' '.join(map(str, locs)))

# locs = [g.start()+1 for g in finditer(r'(?=N[^P][ST][^P])', "AAAANASNASAAAANASAAAA")]
# locs = [g.start()+1 for g in finditer(r'(?=N[^P][ST][^P])', "AAAANASNASAAAANASAAAA")] #g is a MatchObject. start() is needed to get the string position of where the pattern matched the given string
# locs = finditer(r'(?=N[^P][ST][^P])', "AAAANASNASAAAANASAAAA") #gives an iterator yielding MatchObject instances where pattern matched


f = urlopen(uniprot % "A2A2Y4").read().decode('utf-8')
# f = urlopen(uniprot % "A2A2Y4").read()
f = ''.join(f.splitlines()[1:])
# f = ''.join(f.splitlines())
print f
