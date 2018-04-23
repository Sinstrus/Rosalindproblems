from Bio.Seq import Seq
from Bio import SeqIO
import distance

seqrlist = [item for item in SeqIO.parse("rosalind_corr.txt",'fasta')]

Hamm_limit = 2 #max Hamming distance to consider reads to be identical

def groupbyHamm(seqrlist, Hamm_limit):
    """Takes a list of seq records
    Makes a copy of the list

    Calculates the Hamming distance between all pairs of sequences
    including reverse_complements and groups them together into a list
    if their Hamming distances from each other are <= Hamm_limit

    If a group is found, those sequences are removed from
    subsequent consideration by adding them to a passlist

    Outputs list_of_groups, which is a list of lists containing seq groups"""

    seqrcopy = list(seqrlist)
    list_of_groups = []
    rcidlist = []
    passlist = []
    for record1 in seqrcopy:
        if record1.id not in passlist:
            # print "%s not in passlist... creating new seqgroup and beginning search..." % record1.id
            seqgroup = []
            seqgroup.append(record1)
            passlist.append(record1.id)
            fwrecord1 = record1.seq
            rvrecord1 = record1.reverse_complement()

            for record2 in seqrcopy:

                if record2.id not in passlist:
                    # print "%s not in passlist... testing..." % record2.id
                    fwrecord2 = record2.seq
                    # print ("%s/%s --> %s"
                    # % (record1.id, record2.id,
                    # min(distance.hamming(fwrecord1,fwrecord2),
                    # distance.hamming(rvrecord1,fwrecord2)))
                    # )

                    dH = distance.hamming(fwrecord1,fwrecord2)
                    dHr = distance.hamming(rvrecord1,fwrecord2)

                    # print dH
                    # print dHr

                    if dH <= Hamm_limit:
                        # print "Pass! Adding %s to seqgroup and passlist" % record2.id
                        seqgroup.append(record2)
                        passlist.append(record2.id)
                    elif dHr <= Hamm_limit:
                        seqgroup.append(record2)
                        passlist.append(record2.id)
                        rcidlist.append(record2.id)

            list_of_groups.append(seqgroup)

    return list_of_groups,rcidlist

def errorcorrect(list_of_grouplists,rcidlist):
    """Takes a list of lists, each of which contains a group of SeqRecords
    that have been grouped together because they are all Hamm_limit distance
    from each other or less. Can contain reverse complements

    Second input is a list of sequence IDs identifying those reads that come from
    the opposite DNA strand relative to the other two reads

    Creates a copy of the given list containing reads all on the same strand

    Iterates through each group of reads and calculates an Err value that is
    the sum of Hamming distance between each read and its sibling reads. Creates
    a new list of tuples that contains this Err value paired with each read

    The bad read is identified by searching for the read in a group with the max
    Err value. This bad read is then put in a tuple together with one of the good
    reads (a seqrecord with minimum Err value). This good read is given the same
    id as the bad read, and this tuple is put into a list

    The bad and good read is printed in '[bad read]->[good read]' format"""

    #makes temporary list with all (-) strand reads reverse-complemented
    tempgrouplist = []
    for grouplist in list_of_grouplists:
        tempseqgroup = []

        for seqr in grouplist:
            if seqr.id in rcidlist:
                RCseqr = seqr.reverse_complement()
                RCseqr.id = seqr.id
                tempseqgroup.append(RCseqr)
            else:
                tempseqgroup.append(seqr)

        tempgrouplist.append(tempseqgroup)

    # for l in list_of_grouplists:
    #     print ' '.join(str(seqr.seq) for seqr in l)
    #
    # print " "
    #
    # for l in tempgrouplist:
    #     print ' '.join(str(seqr.seq) for seqr in l)

    erroridcountlist = []

    for grouplist in tempgrouplist:
        errortuplegrouplist = []

        for seqr1 in grouplist:
            Err = 0

            for seqr2 in grouplist:
                if seqr1.id != seqr2.id:
                    Err += distance.hamming(seqr1.seq,seqr2.seq)

            errortuplegrouplist.append((Err, seqr1))

        erroridcountlist.append(errortuplegrouplist)

    badtogoodlist = []

    for iderrtuplelist in erroridcountlist:
        print max([tuple for tuple in iderrtuplelist],key = lambda x: x[0])
        # print min([tuple for tuple in iderrtuplelist],key = lambda x: x[0])

        badreadrec = max([tuple for tuple in iderrtuplelist],key = lambda x: x[0])[1]
        goodreadrec = min([tuple for tuple in iderrtuplelist],key = lambda x: x[0])[1]

        # print badreadrec.seq
        # print goodreadrec.seq

        if badreadrec.id in rcidlist:
            badreadrecrc = badreadrec.reverse_complement()
            badreadrecrc.id = badreadrec.id

            goodreadrecrc = goodreadrec.reverse_complement()
            goodreadrecrc.id = badreadrec.id

            badtogoodlist.append((badreadrecrc,goodreadrecrc))
        else:
            badtogoodlist.append((badreadrec,goodreadrec))

    return badtogoodlist

list_of_grouplists,rcidlist = groupbyHamm(seqrlist,Hamm_limit)

# for grouplist in list_of_grouplists:
#     print ' '.join(seqr.id for seqr in grouplist)

badtogoodlist = errorcorrect(list_of_grouplists,rcidlist)

for pair in badtogoodlist:
    # oriseq = [x for x in seqrlist if x.id == pair[0].id][0]
    #
    # print str(oriseq.seq)
    # print str(pair[0].seq)
    # print str(pair[1].seq)
    print "%s->%s" % (pair[0].seq,pair[1].seq)
    # for x in seqrlist:
    #     if x.id == pair[0].id:
    #         print distance.hamming(x.seq,pair[1].seq)
