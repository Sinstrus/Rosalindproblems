s = """
ATTAGACCTG
GCCGGAATAC
CCTGCCGGAA
AGACCTGCCG
""".split()

def overlap(a,b):
    """This function iterately checks progressively larger chunks of the end
    of string a and the beginning of string b, adding the character index l
    to a list if they do match.

    Then returns the greatest index l in the table, if the table has at least one
    index. This means only the greatest length overlap is kept for later
    The minimum overlap needed for a successful l find is half the length
    of the shorter sequence. This could be easily decreased to an arbitrarily
    small value, but this would be dangerous for very small fragments
    """
    candidates_overlaps = [l for l in range(min(len(a),len(b))/2, min(len(a),len(b))) if a[-l:] == b[:l]]

    return max(candidates_overlaps) if len(candidates_overlaps)>0 else 0

def extend(consensus,remaining_reads):
    """While the table of remaining reads is greater than 0:

    1. Make a table of tuples that contain (i) overlap lengths for the current consensus and all
    remaining reads #0,2,0,0,0,67... and (ii) each read itself
    e.g. [(0,"ATGGA"),(34,"GGGTTTAGAGAGGTAGAG..."),(0,"AAGGTGAG")]

    2. Pick out the tuple that contains the greatest overlap length and the
    corresponding read. This is done using the max() function with
    key = lambda x: x[0]. i.e. the max function is only testing the first element
    of each tuple to determine the max value. Otherwise, max would not work

    3. If the best overlap length is 0, then break out of the while loop

    4. Otherwise, if best overlap length is not 0, then take out that best overlap
    read from the list of remaining reads

    5. And add to the end of the consensus the portion of the best overlap read
    starting from overlap length, e.g. best_overlap[overlap_length]

    When while loop is finished, return the consensus that has been built
    """
    while len(remaining_reads)>0:
        overlap_length, best_overlap = max( [(overlap(consensus,b), b) for b in remaining_reads], key = lambda x: x[0] )
        if overlap_length == 0:
            break
        remaining_reads.remove(best_overlap)
        consensus += best_overlap[overlap_length:]
    return consensus

print revcomp(
                extend(

                    revcomp(s[0]), map(revcomp,s[1:])

                )

            )[:-len(s[0])] + extend(s[0], s[1:])

"""The above code first performs the extend function with the first read given as
consensus and the reads of the reads as the remaining_reads list. I'm not sure why
the author uses the reverse_complement here


"""
