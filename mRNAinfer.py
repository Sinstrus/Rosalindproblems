
aacodon = {
            "M":1, "A":4, "I":3, "L":6, "V":4,
            "F":2, "W":1, "Y":2,
            "N":2, "C":2, "Q":2, "S":6, "T":4,
            "D":2, "E":2,
            "R":6, "H":2, "K":2,
            "G":4, "P":4
            } # remember that there are three stop codons!

with open("rosalind_mrna.txt","r") as f:
    protseq = ''.join(line.rstrip() for line in f)


# print protseq
codoncount = [aacodon[residue] for residue in protseq]

prod = 1
for x in codoncount:
    prod = (prod * x) % 1000000

prod = (prod * 3) % 1000000 #for stop codon

print prod
