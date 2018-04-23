from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

seqrlist = [item.seq for item in SeqIO.parse("rosalind_lcsm.txt",'fasta')]

def findMotif(seqrlist):
    motiflist = []
    shortseq = min(seqrlist,key=len)
    # print shortseq
    for i in range(len(shortseq),2,-1):
        for j in range(len(shortseq)-i):
            candidate = shortseq[j:j+i]
            # print candidate
            if all(candidate in seqr for seqr in seqrlist):
                # print candidate + " MATCHES ALL SEQUENCES!"
                return candidate

results = findMotif(seqrlist)
print results
#
# max = 0
# longest = ""
# for item in results:
#     if len(item) > max:
#         max = len(item)
#         longest = item
#
# print longest
