import subprocess

def getfileNum(afile):

    cmd = "wc -l %s " % afile
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    n = p.stdout.read()
    Num = int(n.split()[0])
    return Num

if __name__ == "__main__":
    import sys
    getfileNum(sys.argv[1])
