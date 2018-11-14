from collections import OrderedDict

def code2score(code):
    return ord(code) - 33

def score2code(score):
    return chr(score + 33)

def checkqual(qual,q_thread,percent):
    filters = []
    for q in qual:
        q = code2score(q)
        if q >= q_thread:
            filters.append(1)
        else:
            filters.append(0)

    per = float(filters.count(0))/len(filters)
    if per >= percent:
        return 0
    return 1

def checkN(seq,percent):
    filters = []
    for q in seq:
        if q == "N":
            filters.append(1)
        else:
            filters.append(0)

    per = float(filters.count(1))/len(seq)

    if per >= percent:
        return 1
    return 0

class dnaseq:

    @staticmethod
    def reverse(seq):
        seq = seq[::-1]
        return seq

    @staticmethod
    def complent(seq):
        comdict = {"A":"T","C":"G","G":"C","T":"A","N":"N"}
        seq = "".join([comdict[s] for s in seq])
        return seq


def diffstr(str1,str2):
    mis = 0
    for c1,c2 in zip(str1,str2):
        if c1==c2:
            continue
        mis = mis + 1
    return mis

def checkumi(seq,umis):
    checklist = []
    for umi in umis:
        misnum = diffstr(seq,umi)
        checklist.append([umi,misnum])
    checklist = sorted( checklist, key=lambda x:x[0] )    
    umi,mis = checklist[0]
    return umi,mis


def seeding(seq1,seq2,seed_len=10,seed_max=3,seed_step=1):
    """ find seed candidates return seeds and locus.
    """
    seeds = OrderedDict()
    for i in range(0,len(seq1)-seed_len+1,seed_step):
        seed = seq1[i:i+seed_len]
        seeds[i] = seed
    
    seeds_found = OrderedDict()
    for idx1,seed in seeds.items():
        rcseed = dnaseq.complent(dnaseq.reverse(seed))
        r2idx = seq2.rfind(rcseed)
        if r2idx != -1:
            seeds_found[idx1] = [r2idx,seed]


    choose_step = len(seeds_found)  / seed_max + 1
    seed_choosed = {}
    ks = seeds_found.keys()
    for i in range(0,len(seeds_found),choose_step):
        idx1 = ks[i]
        seed_choosed[idx1] = seeds_found[idx1]


    return seed_choosed

#print seeding("TTTGAGATTTGAAGTATTTGAATTATTTAATTAAAAAATAGTTTTTTATTTGATTAATTTTAAAAAATTATTTTAATTATTTGATTTTTGGTTTGTATTTATTGAGGTGTTATATTATTTTTATTTTTATTTTTAAATTTATAGCTCGGA","NTAAATTTAAAAATAAAAATAAAAATAATATCACACCTCAATAAATACAAACCAAAAAACAAATAATTCAAATAATTTTTTAAAATTAATCAAATACAAAACTATTTTTTAATTAAATAATTCCAATACTTCAAATCTCAAAAGATCGAC")

def enlong_and_find_common(seq1,seq2,seed_choosed,mismatchMax=5):
    """return best common sequences.  

    """
    commons = []
    for idx1,seeditem in seed_choosed.items():
        r2idx,seed = seeditem
        i = 0
        common_seq = seed
        mismatch = 0
        match = 0
        for i in range(max(len(seq1),len(seq2))):
            try:
                r1idx_ = idx1 + len(seed) + i 
                r2idx_ = r2idx -i - 1
                nc1 = seq1[r1idx_]
                nc2 = seq2[r2idx_]
            except Exception,err:
                r1idx_ = r1idx_ - 1
                r2idx_ = r2idx_ + 1
                break
            
            if mismatch > mismatchMax:
                break
            if r2idx_ == -1:
                break
            if nc1 == dnaseq.complent(nc2):
                common_seq = common_seq + nc1
                match = match + 1
            else:
                common_seq = common_seq + nc1
                mismatch = mismatch + 1
        commons.append([common_seq,idx1,r1idx_,r2idx_+1,r2idx+len(seed)])

    commons = sorted(commons,key=lambda x: -len(x[0]))
    if not commons:
        return 
    return commons[0]


#seeds =  seeding("TTTGAGATTTGAAGTATTTGAATTATTTAATTAAAAAATAGTTTTTTATTTGATTAATTTTAAAAAATTATTTTAATTATTTGATTTTTGGTTTGTATTTATTGAGGTGTTATATTATTTTTATTTTTATTTTTAAATTTATAGCTCGGA","NTAAATTTAAAAATAAAAATAAAAATAATATCACACCTCAATAAATACAAACCAAAAAACAAATAATTCAAATAATTTTTTAAAATTAATCAAATACAAAACTATTTTTTAATTAAATAATTCCAATACTTCAAATCTCAAAAGATCGAC")

#print enlong_seed("TTTGAGATTTGAAGTATTTGAATTATTTAATTAAAAAATAGTTTTTTATTTGATTAATTTTAAAAAATTATTTTAATTATTTGATTTTTGGTTTGTATTTATTGAGGTGTTATATTATTTTTATTTTTATTTTTAAATTTATAGCTCGGA","NTAAATTTAAAAATAAAAATAAAAATAATATCACACCTCAATAAATACAAACCAAAAAACAAATAATTCAAATAATTTTTTAAAATTAATCAAATACAAAACTATTTTTTAATTAAATAATTCCAATACTTCAAATCTCAAAAGATCGAC",seeds)

def checking_adaptor(seq1,seq2,common,threadhold=0.95):
    
    c = len(common[0])
    r1 = common[1]
    r2 = common[3]
    ratio = float(c) / (r1+r2+c)
    if ratio > threadhold:
        return common


#seeds =  seeding("TTTGAGATTTGAAGTATTTGAATTATTTAATTAAAAAATAGTTTTTTATTTGATTAATTTTAAAAAATTATTTTAATTATTTGATTTTTGGTTTGTATTTATTGAGGTGTTATATTATTTTTATTTTTATTTTTAAATTTATAGCTCGGA","NTAAATTTAAAAATAAAAATAAAAATAATATCACACCTCAATAAATACAAACCAAAAAACAAATAATTCAAATAATTTTTTAAAATTAATCAAATACAAAACTATTTTTTAATTAAATAATTCCAATACTTCAAATCTCAAAAGATCGAC")

#com = enlong_and_find_common("TTTGAGATTTGAAGTATTTGAATTATTTAATTAAAAAATAGTTTTTTATTTGATTAATTTTAAAAAATTATTTTAATTATTTGATTTTTGGTTTGTATTTATTGAGGTGTTATATTATTTTTATTTTTATTTTTAAATTTATAGCTCGGA","NTAAATTTAAAAATAAAAATAAAAATAATATCACACCTCAATAAATACAAACCAAAAAACAAATAATTCAAATAATTTTTTAAAATTAATCAAATACAAAACTATTTTTTAATTAAATAATTCCAATACTTCAAATCTCAAAAGATCGAC",seeds)

#print checking_adaptor("TTTGAGATTTGAAGTATTTGAATTATTTAATTAAAAAATAGTTTTTTATTTGATTAATTTTAAAAAATTATTTTAATTATTTGATTTTTGGTTTGTATTTATTGAGGTGTTATATTATTTTTATTTTTATTTTTAAATTTATAGCTCGGA","NTAAATTTAAAAATAAAAATAAAAATAATATCACACCTCAATAAATACAAACCAAAAAACAAATAATTCAAATAATTTTTTAAAATTAATCAAATACAAAACTATTTTTTAATTAAATAATTCCAATACTTCAAATCTCAAAAGATCGAC",com)


def autocutadaptor(seq1,seq2):
    seeds = seeding(seq1,seq2)
    common = enlong_and_find_common(seq1,seq2,seeds)
    if not common:
        return 
    common = checking_adaptor(seq1,seq2,common)
    return common


#print autocutadaptor("AGTGTTTTGGGAGGTTAAGGTAGGATAATATAGTAAGATTTTGTTTTTATTAAAAGTTTAAAATTTTAAAAAAATGTATTGGGTGTGGTTGTGTATGTTTGTAGTTTTAGTTATTTAGGAGGTTGAGAGATCGGAAGAGCACACGTCTGA","CTCAACCTCCTAAATAACTAAAACTACAAACATACACCACCACACCCAATACATTTTTTTAAAATTTTAAACTTTTAATAAAAACAAAATCTTACTATATTATCCTACCTTAACCTCCCAAATCACTAGATCGGAAAAGCGTCGTATAGG")


