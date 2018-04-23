# dataset text file is formatted as a fasta, see below
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT


#parse text file using SeqIO into a list of SeqRecords



from Bio import SeqIO
from Bio.SeqUtils import GC

seqlist = [record for record in SeqIO.parse("rosalind_gc.txt","fasta")]

max = 0
for record in seqlist:
    if GC(record.seq) > max:
        max = GC(record.seq)
        recordmax = record

print recordmax.id
print max
