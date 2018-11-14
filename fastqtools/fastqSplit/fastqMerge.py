import os


def fastqMerge(fqs,prefix):
    
    r1 = prefix + "_R1.fastq"
    r2 = prefix + "_R2.fastq"

    fq1s = []
    fq2s = []
    for fq1,fq2 in fqs:
        fq1s.append(fq1)
        fq2s.append(fq2)
    fq1s = " ".join(fq1s)
    fq2s = " ".join(fq2s)
    
    cmd = "cat %s > %s" % (fq1s,r1)
    os.system(cmd)
    cmd = "cat %s > %s" % (fq2s,r2)
    os.system(cmd)

    return r1,r2
