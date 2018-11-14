import os
from tools import code2score,score2code
from tools import checkqual
from tools import checkN
from tools import dnaseq
from tools import diffstr
from tools import autocutadaptor
class readprocess():
        
    def __init__(self,read):
        self.r1 = read.r1
        self.r2 = read.r2
        self.filter = False
        self.adaptor = False
    def trim(self,head1,tail1,head2,tail2):
        self.r1.seq = self.r1.seq[head1:]
        self.r1.qual = self.r1.qual[head1:]
        if not tail1 == 0:
            self.r1.seq = self.r1.seq[:(0-tail1)]
            self.r1.qual = self.r1.qual[:(0-tail1)]
        self.r2.seq = self.r2.seq[head2:]
        self.r2.qual = self.r2.qual[head2:]
        if not tail2 == 0:
            self.r2.seq = self.r2.seq[:(0-tail2)]
            self.r2.qual = self.r2.qual[:(0-tail2)]

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
        out = autocutadaptor(self.r1.seq,self.r2.seq)
        if not out:
            return 
        consus,r1start,r1end,r2start,r2end = out
        self.r1.seq = self.r1.seq[r1start:r1end]
        self.r1.qual = self.r1.qual[r1start:r1end]
        self.r2.seq = self.r2.seq[r2start:r2end]
        self.r2.qual = self.r2.qual[r2start:r2end]
        self.adaptor = True
        
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
