from Bio import SeqIO

seqrlist = [item.seq for item in SeqIO.parse("rosalindtest.txt",'fasta')]
