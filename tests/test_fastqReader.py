import sys
sys.path.append("../")

from fastqtools.fastqReader.fastqReader import fastqReader 


fq1 = "data/22_R1.fastq"
fq2 = "data/22_R2.fastq"
fz1 = "data/22_R1.fastq.gz"
fz2 = "data/22_R2.fastq.gz"


def test_fastqReader():
    fq = fastqReader(fq1,fq2)
    for f in fq:
        pass

    print f.r1.seq,f.r2.seq

def test_fastqReader2():
    fq = fastqReader(fz1,fz2)
    for f in fq:
        pass
    print f.r1.seq,f.r2.seq




if __name__ == "__main__":
    test_fastqReader()
