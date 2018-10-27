

def fastqWriter(read,prefix):
    """write reads to fastqs

    """
    if read.filter:
        return 
    fq1 = prefix + "_R1.fastq"
    fq2 = prefix + "_R2.fastq"

    fp1 = open(fq1,"a")
    fp2 = open(fq2,"a")

    line1 = read.r1.id + "\n"
    line2 = read.r1.seq + "\n"
    line3 = read.r1.flag + "\n"
    line4 = read.r1.qual + "\n"
    
    fp1.write(line1)
    fp1.write(line2)
    fp1.write(line3)
    fp1.write(line4)
    fp1.close()

    line1 = read.r2.id + "\n"
    line2 = read.r2.seq + "\n"
    line3 = read.r2.flag + "\n"
    line4 = read.r2.qual + "\n"

    fp2.write(line1)
    fp2.write(line2)
    fp2.write(line3)
    fp2.write(line4)
    fp2.close()

