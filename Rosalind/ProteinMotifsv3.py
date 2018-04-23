

#take text file and acquire each line item, which is a Uniprot ID


#iterate through each Uniprot ID -->
#   download uniprot ID fasta file
#   extract the raw protein sequence
#   search raw protein sequence for Nglyc motif and compile locations into a list
#   if there are no Nglyc sites -->
#       do not print uniprot ID or Nglyc location list
#   else -->
#       print uniprot ID
#       print a string containing each item of the Nglyc list separated by a space (on a single line)
import urllib
from re import finditer

with open("rosalind_mprt.txt") as f:
    IDlist = f.read().strip().splitlines()

# print contents

for ID in IDlist:
    fas = urllib.urlopen("http://www.uniprot.org/uniprot/%s.fasta" % ID).read().splitlines()[1:]
    seq = ''.join(fas)

    Nglyclist = [loc.start()+1 for loc in finditer(r'(?=N[^P][ST][^P])',seq)]

    if Nglyclist != []:
        print ID
        print ' '.join(map(str,Nglyclist))
