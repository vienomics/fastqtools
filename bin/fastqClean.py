#!/usr/bin/env python
import sys
import os
curdir  = os.path.dirname(os.path.realpath(__file__))
sdir = os.path.join(curdir,"../")
sys.path.append(sdir)
from multiprocessing import Pool
from fastqtools.fastqReader.fastqReader import fastqReader
from fastqtools.fastqReader.fastqWriter import fastqWriter
from fastqtools.readprocess.readprocess import readprocess
import os

def readclean(read,qual,head1,tail1,head2,tail2,n_percent,autoadapt,umis,min_length):
    r = readprocess(read)
    r.qual(qual,qual_percent)
    r.trim(head1,tail1,head2,tail2)
    r.nbase(n_percent)
    r.autoadaptremove(auto_adapt)
    r.umi(umis)
    r.length(min_length)
    return r

def main(r1,r2,prefix,qual,head1,tail1,head2,tail2,n_percent,autoadapt,umis,min_length):
    i = 0
    filts = []
    reads = fastqReader(r1,r2)
    tmp_name = "tmp.%s" % os.getpid()
    for read in reads:
        read = readclean(read,qual,head1,tail1,head2,tail2,n_percent,autoadapt,umis,min_length)
        fastqWriter(read,tmp_name)
    cmd = "mv %s_R1.fastq %s_R1.clean.fastq" % (tmp_name,prefix)
    os.system(cmd)
    cmd = "mv %s_R2.fastq %s_R2.clean.fastq" % (tmp_name,prefix)
    os.system(cmd)
    

if __name__ == "__main__":
    from docopt import docopt
    usage = """
    Usage:
        fastqClean.py [options] -1 <fastq1> -2 <fastq2>  -o <prefix>

    Options:
        #basic arguments
        -1,--r1=<fastq>             R1 fastq         
        -2,--r2=<fastq>             R2 fastq
        -o,--prefix=<prefix>        ouput prefix

        #quality filtering
        --min-qual=<quality>          minimum base quality [default: 15]
        --min-qual-percent=<num>           minimum base quality percentage [default: 0.3]
        --max-nbase-percent=<num>    max N-base percentage [default: 0.1]
        
        #length filtering
        --min-length=<num>           minimum read length [default: 80]
 
        #overlap filtering 
        #--overlap=<num>          minimum overlapped bases [default:11]

        #trimming 
        --trim1-head=<num>          trim r1 num base from R1 head [default: 0]
        --trim1-tail=<num>          trim r1 num base from R1 tail [default: 0]
        --trim2-head=<num>          trim r2 num base from R2 head [default: 0]
        --trim2-tail=<num>          trim r2 num base from R2 tail [default: 0]
        
        #adapter
        --auto-adapt-trim                auto adapt trim throgh r1/r2 overlap recommended

        #umi format
        --umi=<length|file>         umi1 length or file has umi-barcode file.

    """
    args = docopt(usage)
    q1 = args["--r1"]
    q2 = args["--r2"]
    prefix = args["--prefix"]
    qual = int(args["--min-qual"])
    qual_percent = float(args["--min-qual-percent"])
    n_percent = float(args["--max-nbase-percent"])
    min_length = int(args["--min-length"])
    head1 = int(args["--trim1-head"])
    head2 = int(args["--trim2-head"])
    tail1 = int(args["--trim1-tail"])
    tail2 = int(args["--trim2-tail"])
    auto_adapt = args["--auto-adapt-trim"]
    umi = args["--umi"]
    main(q1,q2,prefix,qual,head1,tail1,head2,tail2,n_percent,auto_adapt,umi,min_length)
