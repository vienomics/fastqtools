import sys
sys.path.append("../")

from fastqtools.fastqSplit.fastqSplit import fastqSplit


def test_fastqSplit():
    fastqSplit("data/test_R1.fastq","data/test_R2.fastq",3,"33")



if __name__ == "__main__":
    test_fastqSplit()
