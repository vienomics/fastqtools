#!/usr/bin/env python
import sys
import os
curdir  = os.path.dirname(os.path.realpath(__file__))
sdir = os.path.join(curdir,"../")
sys.path.append(sdir)
from fastqtools.fastqStat.fastqStat import fastqStat
import os

def main(q1,q2,prefix):
    fqs = fastqStat(q1,q2,prefix)

if __name__ == "__main__":
    from docopt import docopt
    usage = """
    Usage:
        fastqStat.py [options] -1 <fastq1> -2 <fastq2>  -o <prefix>

    Options:
        #basic arguments
        -1,--r1=<fastq>                  R1 fastq         
        -2,--r2=<fastq>                  R2 fastq
        -o,--prefix=<prefix>             ouput prefix

    """
    args = docopt(usage)
    q1 = args["--r1"]
    q2 = args["--r2"]
    prefix = args["--prefix"]
    main(q1,q2,prefix)
