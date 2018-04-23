from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

def getFileContents(filename):

    DNAfile = open(filename,"r")
    s = Seq(DNAfile.read(),generic_dna)
    DNAfile.close()

    return s

def findSeqPos(dnaseq,subseq):
    pass
    

filename = "rosalind_rna.txt"

RNAseq = getFileContents(filename).transcribe()
print RNAseq
