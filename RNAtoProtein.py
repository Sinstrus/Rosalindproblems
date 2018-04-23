from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein
import re

def getFileContents(filename):

    DNAfile = open(filename,"r")
    s = Seq(DNAfile.read(),generic_dna)
    DNAfile.close()

    return s

def nuctoprotein(rnaseq):
    prot = rnaseq.translate(to_stop=False)
    return prot

seq = getFileContents('rosalind_prot.txt')
print seq
# split = file.split('\n')
# dnaseq = file.split('\n')[0]
# seq2 = file.split('\n')[1]

# print file
# print split
# print seq1
# print seq2

prot = nuctoprotein(seq)

print prot
