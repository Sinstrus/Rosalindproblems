

DNAfile = open("rosalind_dna.txt","r")
s = DNAfile.read()

def baseCount(DNAseq):
    A = DNAseq.count("A")
    C = DNAseq.count("C")
    G = DNAseq.count("G")
    T = DNAseq.count("T")

    return str(A) + " " + str(C) + " " + str(G) + " " + str(T)

print(baseCount(s))
