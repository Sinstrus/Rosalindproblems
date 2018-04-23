from Bio.Seq import Seq
from Bio import SeqIO
from collections import Counter

seqrlist = [item for item in SeqIO.parse("rosalindtest.txt",'fasta')]

X = seqrlist[3].id

print
