from difflib import SequenceMatcher
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein
from __builtin__ import any as b_any

seqrlist = [item.seq for item in SeqIO.parse("rosalind_lcsm.txt",'fasta')]

def longest_string_match(str1,str2):
    Obj = SequenceMatcher(None,str1,str2)
    Match = Obj.find_longest_match(0,len(str1),0,len(str2))
    return str1[Match[0]:Match[0] + Match[-1]]

def findMotif(seqrlist):
    motiflist = []
    for i in range(len(seqrlist)):
        for j in range(len(seqrlist)):
            if i != j:
                candidate = longest_string_match(str(seqrlist[i]),str(seqrlist[j]))
                print "Testing candidate string... " + candidate
                if candidate not in motiflist and len(candidate) > 0 and False not in list(candidate in x for x in seqrlist):
                    print "Candidate substring " + candidate + " matches all strings!"
                    motiflist.append(candidate)

    return list(set(motiflist))

results = findMotif(seqrlist)

max = 0
longest = ""
for item in results:
    if len(item) > max:
        max = len(item)
        longest = item

print longest
