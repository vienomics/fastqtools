

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

    per = float(filters.count(1))/len(filters)
    if per >= percent:
        return 1
    return 0

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
