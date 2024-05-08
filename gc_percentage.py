from Bio import SeqIO
from Bio.SeqUtils import GC
import pandas as pd
import os
import glob
filepath="/home/bharath/fastaglob"
fasta_files=glob.glob('%s/*.fasta'%filepath)
length=len(fasta_files)
print(length)
print(fasta_files)
def calculate_GC(fasta):
    seq_obj=SeqIO.read(fasta,'fasta')
    sequence=seq_obj.seq
    print(sequence)
    gc_content=GC(sequence)

    filename=os.path.split(fasta)
    filename=filename[1]
    filename=filename.strip(".fasta")
    print(filename)
    print(gc_content)
for fasta in fasta_files:
    calculate_GC(fasta)
