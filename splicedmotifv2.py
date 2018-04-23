from Bio import SeqIO
from Bio.Seq import Seq

seqrlist = [item for item in SeqIO.parse("rosalind_test.txt",'fasta')]

s = seqrlist[0].seq
t = seqrlist[1].seq

print s
print t


def splicedmotif(s,t):
    loc = -1
    l = []

    for c in t:
        z = s.find(c,loc+1)
        if z > -1:
            l.append(z+1)
            loc = z
        
    if ''.join(s[f-1] for f in l) == t:
        return l

l = splicedmotif(s,t)

print ' '.join(map(str,l))