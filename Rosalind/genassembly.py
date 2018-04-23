from Bio.Seq import Seq
from Bio import SeqIO

seqrlist = [item for item in SeqIO.parse("rosalindtest.txt",'fasta')]

k = 20
L = len(max(seqrlist,key=len))
print L

def overlapgraph(seqrecordlist,k):
     #k = suffix/prefix length
     print "Building overlap graph for k = %s" % k
     adj_list = []
     for record1 in seqrecordlist:
         for record2 in seqrecordlist:
             if record1.seq != record2.seq:
                 Obj = SequenceMatcher(None,record1.seq,record2.seq)
                 Match = Obj.find_longest_match(1,len(record1),0,len(record2)-1)
                 # print Match[-1]
                 a = Match[0]
                 b = Match[1]
                 le = Match[-1]
                 if record1.seq[a:a+le] == record2.seq[0:le]:
                     print "Breaking out of loop..."
                     adj_list.append((record1.id,record2.id))
                     break

     return adj_list

# max = 0
# for t in range(k,L):
#     Ograph = overlapgraph(seqrlist,t)
#
#     if len(Ograph) > max:
#         maxgraph = Ograph
#         max = len(Ograph)

maxgraph = overlapgraph(seqrlist,k)

print '\n'.join(tup[0] + " " + tup[1] for tup in maxgraph)
