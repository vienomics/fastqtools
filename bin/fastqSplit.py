#!/usr/bin/env python
import sys
import os
curdir  = os.path.dirname(os.path.realpath(__file__))
sdir = os.path.join(curdir,"../")
sys.path.append(sdir)
from fastqtools.fastqSplit.fastqSplit import fastqSplit
import os

def main(q1,q2,num,prefix):
    fqs = fastqSplit(q1,q2,num,prefix)
    print fqs

if __name__ == "__main__":
    from docopt import docopt
    usage = """
    Usage:
        fastqClean.py [options] -1 <fastq1> -2 <fastq2>  -o <prefix>

    Options:
        #basic arguments
        -1,--r1=<fastq>                  R1 fastq         
        -2,--r2=<fastq>                  R2 fastq
        -o,--prefix=<prefix>             ouput prefix
        -n,--splitNum=<int>              split num for raw fastq [default: 2]

    """
    args = docopt(usage)
    print args
    q1 = args["--r1"]
    q2 = args["--r2"]
    prefix = args["--prefix"]
    num = int(args["--splitNum"])
    main(q1,q2,num,prefix)
