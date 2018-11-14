
from ..fastqReader.fastqReader import fastqReader
from getfileNum import getfileNum

def code2score(code):
    return ord(code) - 33

def score2code(score):
    return chr(score + 33) 

def qual20(scores):
    s20 = []
    s30 = []
    for s in scores:
        if s > 20 or s == 20 :
            s20.append(s)
        if s > 30 or s == 30:
            s30.append(s)
    return float(len(s20))/len(scores),float(len(s30))/len(scores)

def fastqStat(fq1,fq2,prefix):

    reads = fastqReader(fq1,fq2)
    scores = ""
    bases = ""
    lineNum = getfileNum(fq1) 
    readsNum = lineNum / 4

    for idx, read in enumerate(reads):
        if idx == 100000:
            break
        scores = scores + read.r1.qual
        scores = scores + read.r2.qual
        bases = bases + read.r1.seq
        bases = bases + read.r2.seq
    ngc = bases.count("G") + bases.count("C")
    gc = round(float(ngc) / len(bases),4)
    scores = [ code2score(s) for s in scores ]
    q20,q30 = qual20(scores)
    qcfile = prefix + ".fastq.qc.tsv"
    fp = open(qcfile,"w")
    cont = """reads\t%s\tpassed 
q20\t%s\tpassed
q30\t%s\tpassed
gc\t%s\tpassed"""% (readsNum,q20,q30,gc)
    fp.write(cont)
    return gc,q20,q30
