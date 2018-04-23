from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

def getFileContents(filename):

    DNAfile = open(filename,"r")
    s = Seq(DNAfile.read(),generic_dna)
    DNAfile.close()

    return s

def findSeqPos(dnaseq,subseq):
    pass
    loc = []
    L = len(subseq)
    for base in range(len(dnaseq)):
        if dnaseq[base:base+L] == subseq:
            loc = loc + [base+1,]
    return loc

file = getFileContents("rosalind_subs (1).txt")
# split = file.split('\n')
dnaseq = file.split('\n')[0]
subseq = file.split('\n')[1]

# print file
# print split
# print dnaseq
# print subseq

locList = findSeqPos(dnaseq,subseq)
# print locList

for item in locList:
    if item == locList[-1]:
        print str(item)
    else:
        print str(item) + " ",
