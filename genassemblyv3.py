from Bio.Seq import Seq
from Bio import SeqIO
from collections import Counter
import time

start_time = time.time()

seqrlist = [item for item in SeqIO.parse("rosalind_long.txt",'fasta')]

k = 30
# L = len(max(seqrlist,key=len))
# print L

def overlapgraph(seqrecordlist,k):
     #k = suffix/prefix length
     print "Building overlap graph for k at least %s" % k
     id_list = []
     seq_list = []
     for record1 in seqrecordlist:
         maxxlen = 0
         suff = record1.seq[-k:]
         xlen = len(suff)
         for record2 in seqrecordlist:
             if record1.id != record2.id and suff in record2.seq:
                 pref = record2.seq[:record2.seq.find(suff) + xlen]
                 if record1.seq[-len(pref):] == pref and maxxlen == 0:
                     print "Found match of %s bases! Pairing %s and %s..." % (len(pref), record1.id, record2.id)
                     maxxlen = len(pref)
                     id_list.append([record1.id,record2.id,len(pref)])
                     seq_list.append([record1.seq,record2.seq,len(pref)])
                 elif record1.seq[-len(pref):] == pref and len(pref) > maxxlen:
                     print "Found longer match of %s bases! Pairing %s and %s instead" % (len(pref), record1.id,record2.id)
                     maxxlen = len(pref)
                     # print repr(adj_list[-1])
                     del id_list[-1]
                     del seq_list[-1]
                     id_list.append([record1.id,record2.id,len(pref)])
                     seq_list.append([record1.seq,record2.seq,len(pref)])
                     # print repr(adj_list[-1])

     return id_list,seq_list

def checkgraph(overlapgraphlist):
    """Checks how many times each sequence ID appears in a pair (both as seq1 and
    as seq2). Overlap graph must be a list of 3-element [seq1,seq2,prefix length] lists."""
    listcopy = list(overlapgraphlist)

    warncount = 0

    flatlist1 = [listpair[0] for listpair in overlapgraphlist]
    flatlist2 = [listpair[1] for listpair in overlapgraphlist]

    countdict1 = Counter(flatlist1)
    countdict2 = Counter(flatlist2)

    print "Checking each sequence record for multiple pairings..."

    for k,v in countdict1.iteritems():
        if v > 1:
            print 'Warning! The end of sequence %s pairs to the beginning of %s sequences!' % (k,v)
            warncount += 1

    for k,v in countdict2.iteritems():
        if v > 1:
            print 'Warning! The beginning of sequence %s pairs to the end of %s sequences!' % (k,v)
            warncount += 1

    if warncount == 0:
        print "Pass! The ends of all sequences pair to, at most, one other sequence."

    for seqid in flatlist1:
        if seqid not in flatlist2:
            print "End of sequence %s pairs once but no sequences pair to beginning of %s (likely starting sequence)" % (seqid,seqid)
            startseqid = seqid

    for seqid in flatlist2:
        if seqid not in flatlist1:
            print "Beginning of sequence %s pairs once but no sequences pair to end of %s (likely ending sequence)" % (seqid,seqid)
            endseqid = seqid

    return warncount, startseqid, endseqid

def checkexhaustion(ori_seqrlist,overlapgraphlist):
    """Checks whether every sequence in the dataset has been successfully
    paired in the overlap graph list"""

    print "Checking that every sequence in dataset has been successfully paired..."
    warncount = 0

    for record in ori_seqrlist:
        for pairlist in overlapgraphlist:
            if record.id in pairlist:
                break
            elif record.id not in pairlist and pairlist == overlapgraphlist[-1]:
                print "Sequence %s does not pair to any other sequences!"
                warncount += 1

    if warncount == 0:
        print "Pass! All sequences in dataset are paired to at least one other sequence"

def buildorderedlist(overlapgraph, W, startseqid, endseqid):
    C = 0
    copylist = list(overlapgraph)
    #first set startseqid to be the first index of orderedlist
    orderedlist = [startseqid]
    if W == 0:
        print "Building ordered list of ids..."
        print "%s..." % orderedlist[0]
        while orderedlist[-1] != endseqid and C < 1000:
            for listpair in copylist:
                C += 1
                if listpair[0] == orderedlist[-1]:
                    print "...%s" % listpair[1]
                    orderedlist.append(listpair[1])
                    copylist.remove(listpair)

    return orderedlist

def buildcontig(ordered_id_list,seqrecordlist,startseqid):
    """Receives a list of sequence IDs ordered according to the overlap graph
    Progressively builds a full-length contig from the sequences corresponding
    to each ID."""

    contig = ""

    for ID in ordered_id_list:
        for seqrecord in seqrecordlist:
            if ID == seqrecord.id and ID != startseqid:
                addseq = seqrecord.seq[seqrecord.seq.find(contig[-30:]) + 30:]
                # print "...%s" % repr(addseq)
                contig = contig + addseq

            elif ID == seqrecord.id and ID == startseqid:
                # print "Starting with...\n%s" % seqrecord.seq
                contig = "%s" % seqrecord.seq

    return contig

id_list,seq_list = overlapgraph(seqrlist,k)
W,startseqid,endseqid  = checkgraph(id_list)
checkexhaustion(seqrlist,id_list)
olist = buildorderedlist(id_list,W,startseqid,endseqid)
contig = buildcontig(olist,seqrlist,startseqid)
print contig

print "\n!!Script took %s seconds!!" % (time.time() - start_time)

# print '\n'.join(listpair[0].id + " " + listpair[1].id + " " + str(listpair[2]) for listpair in maxgraph)
