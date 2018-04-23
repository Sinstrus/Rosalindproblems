from Bio import SeqIO
from Bio import Entrez
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein
import re
import urllib

Entrez.email = "cnguy7@lsuhsc.edu"

def textfilelines_to_list(filename):
    with open(filename) as file:
        protIDlist = file.readlines()

    protIDlist = [ID.strip() for ID in protIDlist] #strips \n characters

    return protIDlist

def fetchIDs(IDlist):
    seq_record_list = []
    for ID in IDlist:
        # handle = Entrez.efetch(db="protein", id=ID, rettype="fasta", retmode="text")
        handle = urllib.urlopen("http://www.uniprot.org/uniprot/" + ID + ".fasta")
        seq_record = SeqIO.read(handle,"fasta")
        handle.close()

        seq_record_list = seq_record_list + [seq_record,]

    # return list_prot_records
    return seq_record_list

def Nglycsearch(seq_record):
    glyclist = []
    for pos in range(len(seq_record)-3):
        if seq_record.seq[pos] == "N":
            if seq_record.seq[pos+1] != "P" and seq_record.seq[pos+3] != "P":
                if seq_record.seq[pos+2] == "S" or seq_record.seq[pos+2] == "T":
                    glyclist = glyclist + [pos+1,]
    return glyclist

IDlist = textfilelines_to_list("rosalind_mprt.txt")

seq_record_list = fetchIDs(IDlist)

# for seq_record in seq_record_list:
#     print len(seq_record)

# glyclist = Nglycsearch(seq_record_list[2])
# print glyclist

for seq_record in seq_record_list:
    glyclist = Nglycsearch(seq_record)
    # print glyclist
    if len(glyclist) > 0:
        for ID in IDlist:
            if seq_record.id.split("|")[1] in ID:
                print ID

        for item in glyclist:
            if item == glyclist[-1]:
                print str(item).strip()
            else:
                print str(item).strip() + "",
