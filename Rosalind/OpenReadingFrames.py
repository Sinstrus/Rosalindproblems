#this script opens a text/fasta file containing a DNA sequence (string) and detects
#any open reading frames within that sequence

from Bio.Seq import Seq

with open("rosalind_orf.txt","r") as f:
    seq = Seq(''.join(f.read().strip().splitlines()[1:]))

#dictionary with DNA codons and amino acid translations
codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }

#takes a seq string and codon string
#yields the starting position of every instance of codon in seq
#using list() with this function compiles all yielded positions into a list
def findCodonInstances(seq,codon):
    first = 0
    while True:
        first = seq.find(codon,first)
        if first == -1: return
        yield first
        first += 1 # use first += len(codon) to find non-overlapping matches

#Takes seq and codon and inputs them into findCodonInstances
#Compiles the yielded position integers from findCodonInstances into a sorted list
def codonPositionsSorted(seq,codon):
    return sorted(list(findCodonInstances(seq,codon)))

def translate(ORFseq):
    transeq = ""

    #iterates n over a range from 0 to the length of ORFseq, increasing in 3 each time (0... 3... 6...)
    for n in range(0,len(ORFseq),3):
        if ORFseq[n:n+3] in codontable: #ORFseq[n:n+3] = base n, base n+1, base n+2
            transeq += codontable[ORFseq[n:n+3]]

    # print ORFseq
    # print len(ORFseq)
    # print transeq
    # print len(transeq)

    if len(ORFseq)/len(transeq) == 3:
        return transeq
    else:
        return "TRANSLATION ERROR"


#takes a seq string and outputs a list of ORFs (seq string and [start:stop] position)
#minAAs[integer] input tells the function what minimum amino acid length a sequence requires to be considered an ORF
def findORFs(seq,minAAs):
    ORFlist = []

    starts = codonPositionsSorted(seq,"ATG") #finds all start codon positions

    TAA = codonPositionsSorted(seq,"TAA")
    TGA = codonPositionsSorted(seq,"TGA")
    TAG = codonPositionsSorted(seq,"TAG")

    stops = sorted(TAA + TGA + TAG) #compiles all stop codon positions

    for stoppos in stops:
        for startpos in starts:
            if ((stoppos+2)-(startpos-1))/3 >= minAAs and ((stoppos+2)-(startpos-1))%3 == 0:

                ORFstring = seq[startpos:stoppos+3]
                ORFtrans = translate(ORFstring)
                if ORFtrans.find("*",0,-2) >= 0:
                    continue

                # print ORFstring + " (" + ORFtrans + ")" + " [" + str(startpos+1) + ":" + str(stoppos+3) + "]"
                # if len(ORFtrans) > 50:
                    # ORFlist.append(ORFtrans[0:15] + "..." + ORFtrans[-15:] + " [" + str(startpos+1) + ":" + str(stoppos+3) + "]")
                ORFlist.append(ORFtrans[0:-1])
                # else:
                    # ORFlist.append(ORFtrans + " [" + str(startpos+1) + ":" + str(stoppos+3) + "]")
                    # ORFlist.append(ORFtrans[0:-1])

                # print ORFstring

    return ORFlist

ORFlist = findORFs(seq,1)
ORFlist.sort(key=len,reverse=True)
print "\n".join(ORFlist)

ORFlistRC = findORFs(seq.reverse_complement(),1)
ORFlistRC.sort(key=len,reverse=True)
print "\n".join(ORFlistRC)
