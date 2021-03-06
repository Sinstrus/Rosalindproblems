from Bio import SeqIO
from Bio.Seq import Seq

seqrlist = [item for item in SeqIO.parse("aaaaa.txt",'fasta')]

s = seqrlist[0].seq
t = seqrlist[1].seq

def splicedmotif(s,t):
    loc = -1
    l = []

    for c in t:
        z = s.find(c,loc+1)
        if z > -1:
            l.append(z)
            loc = z
        
    if ''.join(s[f] for f in l) == t:
        return l

l = splicedmotif(s,t)

print l