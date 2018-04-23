from Bio.Seq import Seq
from Bio import SeqIO
import distance

seqrlist = [item for item in SeqIO.parse("rosalind_corr.txt",'fasta')]

Hamm_limit = 1 #max Hamming distance to consider reads to be identical

seq5453 = [x for x in seqrlist if x.id == "Rosalind_5453"][0]
seq5041 = [x for x in seqrlist if x.id == "Rosalind_5041"][0]

print seq5453.seq
print seq5041.seq

# for seqr in seqrlist:
#     dH = distance.hamming(seqr.seq,seq5453.seq)
#
#     if seqr.id != seq5453.id and dH <= Hamm_limit:
#         print seqr.id
#         print dH
