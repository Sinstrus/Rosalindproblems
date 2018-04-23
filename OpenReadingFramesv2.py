#this script opens a text/fasta file containing a DNA sequence (string) and detects
#any open reading frames within that sequence

from Bio.Seq import Seq

with open("rosalind_orf.txt","r") as f:
    seq = Seq(''.join(f.read().strip().splitlines()[1:]))

rcseq = seq.reverse_complement()
# if len(seq) % 3 != 0:
#     seq = seq + "N" * (3 - (len(seq) % 3))
ORFlist = []

# print seq.translate(to_stop=False,cds=False)
# print seq.translate(to_stop=False,cds=False).split('*')

for orf in (
            seq.translate(to_stop=False,cds=False).split('*') +
            seq[1:].translate(to_stop=False,cds=False).split('*') +
            seq[2:].translate(to_stop=False,cds=False).split('*') +
            rcseq.translate(to_stop=False,cds=False).split('*') +
            rcseq[1:].translate(to_stop=False,cds=False).split('*') +
            rcseq[2:].translate(to_stop=False,cds=False).split('*')
            ):
    # print orf

    if orf.find("M") >= 0:
        ORFlist.append(orf[orf.find("M"):])

for orf in ORFlist:
    if orf.find("M",1) >= 0:
        ORFlist.append(orf[orf.find("M",1):])

for item in list(set(str(orf) for orf in ORFlist)):
    print item
