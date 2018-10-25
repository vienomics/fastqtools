


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
        -q,-qual=<quality>          minimum base quality
        -n,--nbase=<num>            max N-base num
       
        #length filtering
        -l,--length=<num>           minimum read length
 
        #overlap filtering 
        -e,--overlap=<num>          minimum overlapped bases

        #trimming 
        --trim1-head=<num>          trim r1 num base from R1 head
        --trim1-tail=<num>          trim r1 num base from R1 tail
        --trim2-head=<num>          trim r2 num base from R2 head
        --trim2-tail=<num>          trim r2 num base from R2 tail
        
        #adapter
        --adapt1                    adapter1
        --adapt2                    adapter2
        --auto-adapt                auto adapt trim throgh r1/r2 overlap 

        #umi format
        --umi1=<length|file>        umi1 length from 5' or file has umi-barcode of R1-fastq
        --umi2=<length|file>        umi2 length form 5' or file has umi-barcode of R2-fastq

        # correction 
        --diff-score=<socre>        correct base if diff-score more than score.


    """
    args = docopt(usage)
