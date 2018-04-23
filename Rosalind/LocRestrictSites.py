import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

seqs = [item.seq for item in SeqIO.parse("rosalind_revp.txt",'fasta')]

def scanRes(seq,window):
    pos_len = []
    # print seq
    for i in range(len(seq)-(window-1)):
        if seq[i:i+window] == seq[i:i+window].reverse_complement():
            pos_len.append("{} {}".format(i+1,window))

    return pos_len

minwindow = 4
maxwindow = 12

reslist = [scanRes(seqs[0],w) for w in range(minwindow,maxwindow+1)]
flatreslist = [item for sublist in reslist for item in sublist]

print flatreslist

print '\n'.join(flatreslist)
