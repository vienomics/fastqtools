import os
from tools import code2score,score2code
from tools import checkqual
from tools import checkN
from tools import dnaseq
from tools import diffstr

class readprocess():
        
    def __init__(self,read):
        self.r1 = read.r1
        self.r2 = read.r2
        self.filter = False

    def trim(self,head1,tail1,head2,tail2):
        self.r1.seq = self.r1.seq[head1:]
        self.r1.seq = self.r1.seq[:(0-tail1-1)]
        self.r2.seq = self.r2.seq[head2:]
        self.r2.seq = self.r2.seq[:(0-tail2-1)]
        self.r1.qual = self.r1.qual[head1:]
        self.r1.qual = self.r1.qual[:(0-tail1-1)]
        self.r2.qual = self.r2.qual[head2:]
        self.r2.qual = self.r2.qual[:(0-tail2-1)]

    def qual(self,q,percent):
        if checkqual(self.r1.qual,q,percent) and  checkqual(self.r2.qual,q,percent):
            pass
        else:
            self.filter = True

    def nbase(self,percent):
        if checkN(self.r1.seq,percent) or checkN(self.r2.seq,percent):
            self.filter = True 

    def autoadaptremove(self,flag):
        if not flag:
            return
        seed_len = 4 
        rseq2 = dnaseq.reverse(self.r2.seq)
        rseq2 = dnaseq.complent(rseq2)
        rqual2 = dnaseq.reverse(self.r2.qual)
        seed1 = self.r1.seq[:seed_len]
        seed2 = rseq2[-seed_len:]
        r2idx = rseq2.find(seed1)
        r1idx = self.r1.seq.rfind(seed2)
        if r2idx == -1 and r1idx == -1:
            return 
        mis = 0
        mat = seed_len
        if r2idx != -1 :
            for i in range(len(rseq2)):
                try:
                    nucl2 = rseq2[r2idx+seed_len+i]
                    nucl1 = self.r1.seq[seed_len+i]
                except Exception,err:
                    break
                if nucl1 == nucl2:
                    mat = mat + 1
                else:
                    mis = mis + 1
        if float(mis)/(mat+mis) < 0.05: 
            rseq2 = rseq2[r2idx:]
            rqual2 = rqual2[r2idx:]
            self.r2.seq = dnaseq.reverse(dnaseq.complent(rseq2))
            self.r2.qual = dnaseq.reverse(rqual2)
        if r1idx != -1:
            self.r1.seq  = self.r1.seq[:r1idx+seed_len]
            self.r1.qual = self.r1.qual[:r1idx+seed_len]

    def umi(self,umis):
        if not umis:
            return 
        if type(umis) == int:
            umi1 = self.r1.seq[:umis]
            umi2 = self.r2.seq[:umis]
            umistr = "@" + umi1 + ":" + umi2
            self.r1.id = "%s%s" % (umistr,self.r1.id)
            self.r2.id = "%s%s" % (umistr,self.r2.id)
            self.r1.seq = self.r1.seq[umis:]
            self.r2.seq = self.r2.seq[umis:]
            self.r1.qual = self.r1.qual[umis:]
            self.r2.qual = self.r2.qual[umis:]

        if type(umis) == list:
            umi1,mis1 = checkumi(self.r1.seq,umis)
            umi2,mis2 = checkumi(self.r2.seq,umis)
            umistr = "@%s:%s" % (umi1,umi2)
            self.r1.id = "%s%s" % (umistr,self.r1.id)
            self.r2.id = "%s%s" % (umistr,self.r2.id)
            self.r1.seq = self.r1.seq[len(umi1):]
            self.r1.qual = self.r1.qual[len(umi1):]
            self.r2.seq = self.r2.seq[len(umi2):]
            self.r2.qual = self.r2.qual[len(umi2):]

    def length(self,lenMin):
        if len(self.r1.seq) < lenMin or len(self.r2.seq) < lenMin:
            self.filter = True
