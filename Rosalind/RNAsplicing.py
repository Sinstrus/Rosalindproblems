import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

seqs = [item.seq for item in SeqIO.parse("rosalind_splc.txt",'fasta')]

DNA = seqs.pop(0)

for intron in seqs:
    # print DNA
    DNA = ''.join(str(DNA).split(str(intron)))

DNA = Seq(DNA,generic_dna)
prot = DNA.translate(to_stop = True)
print prot
