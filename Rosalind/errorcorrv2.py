from Bio.Seq import Seq
from Bio import SeqIO
import distance

from string import maketrans
def reverse_complement(s):
    return s.translate(maketrans('ACTG','TGAC'))[::-1]

seqrlist = [str(item.seq).strip() for item in SeqIO.parse("rosalind_corr.txt",'fasta')]

# print '\n'.join(seqr for seqr in seqrlist)

Hamm_limit = 1

def findCorrectReads(seqrlist):
    # correctReads = [s2 for s2 in seqrlist for s1 in seqrlist if s1.id != s2.id and s1.seq == s2.seq]

    correctReads = []
    passlist = []
    C = 0
    for j,s1 in enumerate(seqrlist):
        if C > 2000000:
            print "WARNING! TIME-OUT!"
            break
        if s1 not in passlist:

            for k,s2 in enumerate(seqrlist):
                C += 1
                # print C
                if j != k and s2 not in passlist:
                    # print "Comparing %s and %s..." % (repr(s1),repr(s2))
                    if s1 == s2 or reverse_complement(s1) == s2:
                        # print "Match!"

                        if s1 not in passlist:
                            # print "Adding %s to correctReads" % repr(s1)
                            correctReads.append(s1)
                            passlist.append(s1)

                        if s2 not in passlist:
                            # print "Adding %s to correctReads" % repr(s2)
                            correctReads.append(s2)
                            passlist.append(s2)

    remaining_reads = [seqr for seqr in seqrlist if seqr not in correctReads]

    return correctReads,remaining_reads

def errorCorrection(correctReads,remaining_reads):

    T = 0

    for s in remaining_reads:
        for c in correctReads:
            dH = distance.hamming(s,c)
            dHrev = distance.hamming(s,reverse_complement(c))
            if dH > 0 and dH <= Hamm_limit:
                print "%s->%s" % (s,c)
                T += 1
            elif dHrev > 0 and dHrev <= Hamm_limit:
                print "%s->%s" % (s,reverse_complement(c))
                T += 1

    print "%s read corrections were made" % T

correctReads,remaining_reads = findCorrectReads(seqrlist)

errorCorrection(correctReads,remaining_reads)

# print '\n'.join(str(s.seq) for s in correctReads)
print len(seqrlist)
print len(correctReads)
print len(remaining_reads)
