#!/usr/bin/env python


def main():
    pass



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
        -q,-qual=<quality>          minimum base quality [default: 15]
        --q-percent=<num>           minimum base quality percentage [default: 0.3]
        -n,--nbase-percent=<num>    max N-base percentage [default: 0.1]
        
        #length filtering
        -l,--length=<num>           minimum read length [default: 80]
 
        #overlap filtering 
        -e,--overlap=<num>          minimum overlapped bases [default:11]

        #trimming 
        --trim1-head=<num>          trim r1 num base from R1 head [default: 0]
        --trim1-tail=<num>          trim r1 num base from R1 tail [default: 0]
        --trim2-head=<num>          trim r2 num base from R2 head [default: 0]
        --trim2-tail=<num>          trim r2 num base from R2 tail [default: 0]
        
        #adapter
        --adapt1                    adapter1 not supported currently
        --adapt2                    adapter2 not supported currently
        --auto-adapt                auto adapt trim throgh r1/r2 overlap recommended

        #umi format
        --umi=<length|file>         umi1 length or file has umi-barcode file.

        # correction 
        --diff-score=<socre>        correct base if diff-score more than score. [default: 20]

    """
    args = docopt(usage)
