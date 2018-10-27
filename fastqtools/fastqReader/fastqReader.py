import gzip

class fq():

    def __init__(self,id,seq,flag,qual):
        self.id = id
        self.seq = seq
        self.flag = flag
        self.qual = qual


class fastqReader():

    def __init__(self,fq1,fq2):
        self.fq1 = open(fq1)
        if fq1.endswith(".gz"):
            self.fq1 = gzip.open(fq1)
        self.fq2 = open(fq2)
        if fq2.endswith(".gz"):
            self.fq2 = gzip.open(fq2)
        self.filter=False

    def __iter__(self):
        return self

    def next(self):

        id1 = self.fq1.readline().strip("\n")
        id2 = self.fq2.readline().strip("\n")
        if not id1 or not id2 :
            raise StopIteration
        seq1 = self.fq1.readline().strip("\n")
        flag1 = self.fq1.readline().strip("\n")
        qual1 = self.fq1.readline().strip("\n")

        seq2 = self.fq2.readline().strip("\n")
        flag2 = self.fq2.readline().strip("\n")
        qual2 = self.fq2.readline().strip("\n")

        r1 = fq(id1,seq1,flag1,qual1)
        r2 = fq(id2,seq2,flag2,qual2)

        self.r1 = r1
        self.r2 = r2
        
        return self
