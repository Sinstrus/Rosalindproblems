from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein
import re

def getFileContents(filename):

    DNAfile = open(filename,"r")
    s = Seq(DNAfile.read(),generic_dna)
    DNAfile.close()

    return s

def findHamDist(dnaseq1,dnaseq2):
    count = 0
    if len(dnaseq1) != len(dnaseq2):
        raise ValueError('Cannot calculate. The two sequences are not the same length!')

    for pos in range(len(dnaseq1)):
        if dnaseq1[pos] != dnaseq2[pos]:
            count += 1

    return count

file = getFileContents('rosalind_hamm.txt')
# split = file.split('\n')
seq1 = file.split('\n')[0]
seq2 = file.split('\n')[1]

# print file
# print split
# print seq1
# print seq2

Hamdist = findHamDist(seq1,seq2)

print Hamdist
