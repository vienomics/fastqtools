#!/usr/bin/env python

ndict = {
    "A":"T",
    "T":"A",
    "C":"G",
    "G":"C",
    "N":"N"
}

def RC(seq):
    seq = seq[::-1]
    seq = "".join([ndict[s] for s in seq])
    print seq
    return seq


if __name__ == "__main__":
    import sys
    from docopt import docopt
    usage ="""
    Usage:
        RC.py <seq>

    Reverse and complement Seq which contains ATCGN
    """

    args = docopt(usage)
    seq = args["<seq>"]
    RC(seq)


