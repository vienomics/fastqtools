from ..fastqReader.fastqReader import fastqReader
from ..fastqReader.fastqWriter import fastqWriter
from getfileNum import getfileNum
from collections import OrderedDict

def fastqSplit(fq1,fq2,splitNum,prefix):
    """split Fastq in to small ones to accelerate downstreaming analysis...

    """
    lineNum1 = getfileNum(fq1)
    lineNum2 = getfileNum(fq2) 
    if lineNum1 != lineNum2 :
        return 
    isfastq =  lineNum1 % 4 
    if  isfastq :
        return 
    batchSize = lineNum1 /  ( splitNum * 4 )
    reads = fastqReader(fq1,fq2)
    j = 1
    fqs = OrderedDict()
    fqName = prefix + "-" +str(j)
    fqs[fqName] = [fqName+"_R1.fastq",fqName+"_R2.fastq"]
    for idx,read in enumerate(reads):
        idx = idx + 1
        fastqWriter(read,fqName)
        if idx % batchSize == 0:
            j = j + 1
            if j > splitNum : j = splitNum
            fqName = prefix + "-" +str(j)
            fqs[fqName] = [fqName+"_R1.fastq",fqName+"_R2.fastq"]
    return fqs
