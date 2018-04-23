import random
from Bio import SeqIO

seqlist = [record.seq for record in SeqIO.parse('rosalind_cons.txt','fasta')]

# # seqlist = []
# # for item in rawlist:
# #     if ">" not in item:
# #         seqlist.append(item)
#
# print seqlist

consensuslist = [''] * len(seqlist[0])
# print consensuslist
for i in range(len(seqlist[0])):
    maxcount = 0
    countdict = {
                    "A":0, "C":0, "G":0, "T":0
                    }

    temp = ''.join(seq[i] for seq in seqlist)
    countdict["A"] = temp.count("A")
    countdict["C"] = temp.count("C")
    countdict["G"] = temp.count("G")
    countdict["T"] = temp.count("T")
    #
    # print countdict.values()
    # print max(countdict.values())

    maxcount = max(countdict.values())

    maxbaselist = [k for k,v in countdict.iteritems() if v == maxcount]
    # print maxbaselist

    consensuslist[i] = random.choice(maxbaselist)

# print consensuslist
print ''.join(consensuslist)
