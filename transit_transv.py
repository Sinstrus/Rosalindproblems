from Bio import SeqIO
from Bio.Seq import Seq
import distance

seqrlist = [item for item in SeqIO.parse("rosalind_tran.txt",'fasta')]

s1 = seqrlist[0].seq
s2 = seqrlist[1].seq

print s1
print s2


def transit_transv(s1,s2):
    tsC = 0
    tvC = 0

    tslist = [("G","A"),("A","G"),("C","T"),("T","C")]

    tvlist = [
        ("G","C"),
        ("G","T"),

        ("A","C"),
        ("A","T"),

        ("C","A"),
        ("C","G"),

        ("T","A"),
        ("T","G"),
        ]

    if len(s1) == len(s2):
        x = len(s1)

    for i in range(x):
        mutfound = 0

        for ts in tslist:
            if s1[i] == ts[0] and s2[i] == ts[1]:
                tsC += 1
                mutfound = 1
            
            if mutfound:
                break
        
        for tv in tvlist:
            if mutfound:
                break
                
            if s1[i] == tv[0] and s2[i] == tv[1]:
                tvC += 1
                mutfound = 1

    return tsC, tvC

tsC, tvC = transit_transv(s1,s2)

print tsC
print tvC
print float(tsC)/tvC