import sys
sys.path.append("../")

from fastqtools.fastqReader.fastqReader import fastqReader
from fastqtools.readprocess.readprocess import readprocess


fq1 = "data/22_R1.fastq"
fq2 = "data/22_R2.fastq"
fz1 = "data/22_R1.fastq.gz"
fz2 = "data/22_R2.fastq.gz"


def test_readprocess():
    fq = fastqReader(fq1,fq2)
    for f in fq:
        pass

    f.r1.seq  = "AATTAATTCCGGAATCG"
    f.r1.qual = "FFFFFFFF//////"
    f.r2.seq  = "CCGGTTTTAATTAGC"
    f.r2.qual = "FFFFFFFF//////"

    rp = readprocess(f)
    rp.autoadaptremove(True)
    print rp.r1.seq,rp.r2.seq
    print rp.r1.qual,rp.r2.qual
if __name__ == "__main__":
    test_readprocess()
