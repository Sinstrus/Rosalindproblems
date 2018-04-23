from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

def getFileContents(filename):

    DNAfile = open(filename,"r")
    s = Seq(DNAfile.read(),generic_dna)
    DNAfile.close()

    return s

filename = "rosalind_revc.txt"

RCdna = getFileContents(filename).reverse_complement()
print RCdna
