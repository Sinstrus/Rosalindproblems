from Bio.Seq import Seq
from Bio import SeqIO
from collections import Counter

seqrlist = [item for item in SeqIO.parse("rosalindtest.txt",'fasta')]

k = 600
# L = len(max(seqrlist,key=len))
# print L

def overlapgraph(seqrecordlist,k):
     #k = suffix/prefix length
     print "Building overlap graph for k at least %s" % k
     adj_list = []
     for record1 in seqrecordlist:
         suff = record1.seq[-k:]
         xlen = len(suff)
         for record2 in seqrecordlist:
             if record1.id != record2.id and suff in record2.seq:
                 pref = record2.seq[:record2.seq.find(suff) + xlen]
                 if record1.seq[-len(pref):] == pref:
                     # print "Found match! Pairing %s and %s..." % (record1.id, record2.id)
                     adj_list.append([record1,record2,len(pref)])

     return adj_list

def checkgraph(overlapgraphlist):
    """Checks how many times each sequence ID appears in a pair (both as seq1 and
    as seq2). Overlap graph must be a list of 3-element [seq1,seq2,prefix length] lists.
    Outputs a modified list where tuples containing a multiple-pairing sequence
    are removed."""
    listcopy = list(overlapgraphlist)

    warncount = 0

    flatlist1 = [listpair[0].id for listpair in overlapgraphlist]
    flatlist2 = [listpair[1].id for listpair in overlapgraphlist]

    countdict1 = Counter(flatlist1)
    countdict2 = Counter(flatlist2)

    for k,v in countdict1.iteritems():
        if v > 1:
            print 'Warning! The end of sequence %s pairs to the beginning of %s sequences!' % (k,v)
            warncount += 1

    for k,v in countdict2.iteritems():
        if v > 1:
            print 'Warning! The beginning of sequence %s pairs to the end of %s sequences!' % (k,v)
            warncount += 1

    if warncount == 0:
        print "The ends of all sequences pair to, at most, one other sequence."

    return warncount

def buildorderedlist(overlapgraph, W):
    contig = ""
    if W == 0:

        for listpair in overlapgraph:
            #identifies beginning ID seq
            X = listpair[0].id
            for listpair in overlapgraph:
                if listpair[1].id == X:
                    break
                elif listpair == overlapgraph[-1] and listpair[1].id != X:
                    initseq = listpair
        print initseq


maxgraph = overlapgraph(seqrlist,k)
W = checkgraph(maxgraph)

buildorderedlist(maxgraph,W)


# print '\n'.join(listpair[0].id + " " + listpair[1].id + " " + str(listpair[2]) for listpair in maxgraph)
