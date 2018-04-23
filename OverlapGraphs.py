from Bio.Seq import Seq
from Bio import SeqIO

seqs = [item for item in SeqIO.parse("rosalind_grph.txt",'fasta')]

k = 20

def overlapgraph(seqrecordlist,k):
     #k = suffix/prefix length
     adj_list = []
     for record1 in seqrecordlist:
         for record2 in seqrecordlist:
             if record1.seq != record2.seq and record1.seq[-k:] == record2.seq[:k]:
                 # print record1.seq + " and " + record2.seq
                 # print record1.id + " and " + record2.id
                 adj_list.append((record1.id,record2.id))
     return adj_list

Ograph = overlapgraph(seqs,k)
print '\n'.join(tup[0] + " " + tup[1] for tup in Ograph)
